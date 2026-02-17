import inspect
import logging
import os
import sys
import time
import traceback


class CustomFormatter(logging.Formatter):
    """Custom formatter for console logs that applies colored output
    based on the log level (DEBUG, INFO, ERROR)."""
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    base_format = "%(asctime)s | %(levelname)s | %(message)s"

    formats = {
        logging.DEBUG: ''.join([grey, base_format]),
        logging.INFO: ''.join([yellow, base_format]),
        logging.ERROR: ''.join([red, base_format])
    }

    def format(self, record):
        """Overrides the default format method to apply custom styling.

        Args:
            record: The log record to format.

        Returns:
            formatted_log: The formatted log string.
        """
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# ... imports remain ...

class Logger:
    """Adds functionality like log file separation, colored console output,
    and automatic function/file tagging."""

    def __init__(self, name="PTS", session_name=None, base_log_dir=None, subdir=None):
        """
        Args:
            name: logger name.
            session_name: custom session folder name (e.g., 'GAP_2026_02_17_12_47_33').
            base_log_dir: override root logs directory; defaults to '<repo_root>/logs'.
            subdir: optional child folder inside session (e.g., 'windows' or 'linux').
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        if getattr(self.logger, "_logger_initialized", False):
            # Allow subsequent instances to reuse the same logger but update paths if requested
            if session_name or subdir or base_log_dir:
                self._apply_path_overrides(session_name, base_log_dir, subdir)
            return

        self.logger._logger_initialized = True

        self.log_path = None
        self.stream_handler = None
        self.logger.propagate = False

        # Allow environment overrides
        self._env_session_name = os.getenv("LOG_SESSION_NAME")
        self._env_base_log_dir = os.getenv("LOG_ROOT")

        self._session_name = session_name
        self._base_log_dir = base_log_dir
        self._subdir = subdir

        self.logger_init()

    def _compute_base_log_dir(self):
        cur_file = os.path.abspath(__file__)
        ui_dir = os.path.dirname(cur_file)
        test_automation_dir = os.path.dirname(ui_dir)
        workspace_root = os.path.dirname(test_automation_dir)
        return os.path.join(workspace_root, "logs")

    def _compute_session_name(self):
        if self._env_session_name:
            return self._env_session_name
        if self._session_name:
            return self._session_name
        log_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
        return f"{log_time}_logs"

    def _apply_path_overrides(self, session_name=None, base_log_dir=None, subdir=None):
        """Reconfigure file handlers to a new path if requested."""
        if session_name:
            self._session_name = session_name
        if base_log_dir:
            self._base_log_dir = base_log_dir
        if subdir is not None:
            self._subdir = subdir

        base_dir = self._env_base_log_dir or self._base_log_dir or self._compute_base_log_dir()
        os.makedirs(base_dir, exist_ok=True)

        session_dir = os.path.join(base_dir, self._compute_session_name())
        os.makedirs(session_dir, exist_ok=True)

        final_path = session_dir
        if self._subdir:
            final_path = os.path.join(session_dir, self._subdir)
            os.makedirs(final_path, exist_ok=True)

        # Reconfigure handlers pointing to new file paths
        self.reconfigure_file_handlers(final_path)

    def logger_init(self):
        """Creates the session log directory (with optional subdir) and sets up handlers."""
        base_dir = self._env_base_log_dir or self._base_log_dir or self._compute_base_log_dir()
        os.makedirs(base_dir, exist_ok=True)

        session_name = self._compute_session_name()
        session_dir = os.path.join(base_dir, session_name)
        os.makedirs(session_dir, exist_ok=True)

        final_path = session_dir
        if self._subdir:
            final_path = os.path.join(session_dir, self._subdir)
            os.makedirs(final_path, exist_ok=True)

        self.setup_logger_file(final_path)

    def setup_logger_file(self, path, device=''):
        if getattr(self.logger, "_handlers_initialized", False):
            # Already configured. If new path differs, reconfigure.
            if self.log_path != path:
                self.reconfigure_file_handlers(path)
            return self.logger

        self.logger._handlers_initialized = True
        self.log_path = path

        log_format = "%(asctime)s | %(levelname)s | %(message)s"
        formatter = logging.Formatter(log_format)

        if device:
            device = f"{device}_"

        debug_path = os.path.join(self.log_path, f"{device}debug.log")
        error_path = os.path.join(self.log_path, f"{device}error.log")
        info_path = os.path.join(self.log_path, f"{device}info.log")
        warning_path = os.path.join(self.log_path, f"{device}warning.log")

        # File handlers
        self._debug_handler = logging.FileHandler(debug_path)
        self._debug_handler.setLevel(logging.DEBUG)
        self._debug_handler.setFormatter(formatter)
        self.logger.addHandler(self._debug_handler)

        self._error_handler = logging.FileHandler(error_path)
        self._error_handler.setLevel(logging.ERROR)
        self._error_handler.setFormatter(formatter)
        self.logger.addHandler(self._error_handler)

        self._info_handler = logging.FileHandler(info_path)
        self._info_handler.setLevel(logging.INFO)
        self._info_handler.setFormatter(formatter)
        self.logger.addHandler(self._info_handler)

        self._warning_handler = logging.FileHandler(warning_path)
        self._warning_handler.setLevel(logging.WARNING)
        self._warning_handler.setFormatter(formatter)
        self.logger.addHandler(self._warning_handler)

        # Console
        if not self.stream_handler:
            self.stream_handler = logging.StreamHandler(sys.stdout)
            self.stream_handler.setLevel(logging.DEBUG)
            self.stream_handler.setFormatter(CustomFormatter())
            self.logger.addHandler(self.stream_handler)

        self.logger.propagate = False
        return self.logger

    def reconfigure_file_handlers(self, new_path):
        """Move file handlers to a new directory, keep console handler."""
        self.log_path = new_path
        log_format = "%(asctime)s | %(levelname)s | %(message)s"
        formatter = logging.Formatter(log_format)

        def _reset_handler(old_handler_attr, filename, level):
            old = getattr(self, old_handler_attr, None)
            if old:
                self.logger.removeHandler(old)
                try:
                    old.close()
                except Exception:
                    pass
            h = logging.FileHandler(os.path.join(self.log_path, filename))
            h.setLevel(level)
            h.setFormatter(formatter)
            self.logger.addHandler(h)
            setattr(self, old_handler_attr, h)

        _reset_handler("_debug_handler", "debug.log", logging.DEBUG)
        _reset_handler("_error_handler", "error.log", logging.ERROR)
        _reset_handler("_info_handler", "info.log", logging.INFO)
        _reset_handler("_warning_handler", "warning.log", logging.WARNING)

    def set_session(self, project_name, timestamp=None, subdir=None):
        """
        Switch that logger to a '<project>_<timestamp>' session directory,
        optionally with a child subdir ('windows'/'linux').

        Args:
            project_name: e.g., 'GAP'
            timestamp: override timestamp if desired; defaults to now.
            subdir: optional child folder.
        """
        if not timestamp:
            timestamp = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
        session = f"{project_name}_{timestamp}"
        self._apply_path_overrides(session_name=session, subdir=subdir)
        # also expose for helpers that rely on logger.log_path
        setattr(self.logger, "log_path", self.log_path)
        return self.log_path

    def cleanup_logger(self, name):
        """Removes all log handlers from the logger.

        Args:
            name: The logger's name to clean up.
        """
        self.logger = logging.getLogger(name)
        while self.logger.handlers:
            if isinstance(self.logger.handlers[0], logging.StreamHandler):
                self.stream_handler = None
            self.logger.removeHandler(self.logger.handlers[0])

    def get_logger(self, name):
        """Sets or updates the logger instance by name.

        Args:
            name: Logger name.
        """
        self.logger = logging.getLogger(name)

    def function_property(self):
        """Gets the caller's function name and file name for context-aware logging.

        Returns:
            function_name: Name of the calling function.
            file_name: Name of the file where the function is defined.
        """
        function = inspect.currentframe().f_back.f_back.f_code
        function_name = function.co_name
        filename = os.path.splitext(function.co_filename.split('/')[-1])[0]
        return function_name, filename

    def info(self, message, *args):
        """Logs an INFO-level message with context.

        Args:
            message: The message format string.
            *args: Arguments for formatting.
        """
        function_name, filename = self.function_property()
        if args:
            message = message % args
        self.logger.info("%s | %s | %s", filename, function_name, message)

    def debug(self, message, *args):
        """Logs a DEBUG-level message with context.

        Args:
            message: The message to log.
            *args: Arguments for formatting.
        """
        function_name, filename = self.function_property()
        if args:
            message = message % args
        self.logger.debug("%s | %s | %s", filename, function_name, message)

    def error(self, message, *args):
        """Logs an ERROR-level message with context and full traceback.

        Args:
            message: The error message to log.
            *args: Arguments for formatting.
        """
        function_name, filename = self.function_property()
        if args:
            message = message % args
        self.logger.error("%s | %s | %s", filename, function_name, message)
        self.logger.error(traceback.format_exc())

    def warning(self, message, *args):
        """Logs a WARNING-level message with context.

        Args:
            message: The warning message to log.
            *args: Arguments for formatting.
        """
        function_name, filename = self.function_property()
        if args:
            message = message % args
        self.logger.warning("%s | %s | %s", filename, function_name, message)
