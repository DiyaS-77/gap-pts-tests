import time
import libraries.bluetooth.constants as constants


class GapHandler:
    """GAP (Generic Access Profile) PTS automation handler.

    This class maps PTS WIDs (Work Item IDs) to corresponding Bluetooth
    actions executed on the Implementation Under Test (IUT) via the
    RemoteBluetoothProxy interface.
    """

    def __init__(self, remote_bt, logger):
        """Initialize the GAP handler.

        Args:
            remote_bt: RemoteBluetoothProxy instance controlling the DUT
            logger: Logger instance used for debugging and status logging
        """
        self.remote_bt = remote_bt
        self.log = logger

    def handle(self, wid, **kwargs):
        """Dispatch incoming WID to the appropriate handler function.

        Args:
            wid: Work Item ID received from PTS
            **kwargs: Optional parameters from PTS

        Returns:
            True if operation succeeded, False otherwise
        """
        try:
            wid_number = int(str(wid).strip())
        except Exception:
            self.log.error("Invalid WID received: %r", wid)
            raise NotImplementedError
        handler_name = f"handle_wid_{wid_number}"
        self.log.info("Resolving GAP handler: %s", handler_name)
        handler = getattr(self, handler_name, None)
        if handler is None:
            self.log.warning("No GAP handler implemented for WID %s", wid_number)
            raise NotImplementedError
        self.log.info("Executing GAP handler for WID %s", wid_number)
        success = handler(**kwargs)
        self.log.info("WID %s completed with result: %s", wid_number, success)
        return success

    def handle_wid_53(self):
        """Enable General Discoverable Connectable Advertising.
        Used in connectable advertising validation test cases.
        """
        self.remote_bt.stop_advertising()
        success = self.remote_bt.general_discoverable_advertise(connectable=True)
        time.sleep(0.3)
        return bool(success)

    def handle_wid_52(self):
        """Enable connectable undirected advertising.
        Ensures the IUT is advertising and accepting connections.
        """
        self.remote_bt.stop_advertising()
        self.log.info("Enabling connectable undirected advertising")
        self.remote_bt.general_discoverable_advertise(connectable=True)
        time.sleep(0.3)
        return True

    def handle_wid_20(self):
        """Enable non-connectable undirected advertising.
        Used for observer-only and broadcast scenarios.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.start_advertising("pts_general", "non_connectable")()
        if not success:
            self.log.error("Failed to enable non-connectable advertising")
        return bool(success)

    def handle_wid_21(self):
        """Enable connectable advertising.
        Allows incoming LE connections.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.start_advertising("pts_general", "connectable")()
        if success:
            self.log.info("Connectable advertising started")
        else:
            self.log.error("Connectable advertising failed")
        return bool(success)

    def handle_wid_47(self):
        """Enable broadcast advertising.
        Used for broadcast and observer test scenarios.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.start_advertising("pts_broadcast", "broadcast")()
        return bool(success)

    def handle_wid_79(self):
        """Enable broadcast advertising using NRPA (Non-Resolvable Private Address).
        Used for privacy-related broadcast validation.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.start_advertising("pts_broadcast", "broadcast",
                                      random_addr_key="nrpa")()
        return bool(success)

    def handle_wid_12(self):
        """Start LE discovery (scanning).
        Used in discovery and observer procedures.
        """
        success = self.remote_bt.start_le_discovery()
        return bool(success)

    def handle_wid_13(self):
        """Start LE discovery and allow time for scan results."""
        self.remote_bt.start_le_discovery()
        time.sleep(0.5)
        return True

    def handle_wid_23(self):
        """Start General Discovery Procedure.
        Used for discovering nearby Bluetooth devices.
        """
        self.remote_bt.start_discovery()
        time.sleep(0.5)
        return True

    def handle_wid_10(self):
        """Verify that PTS device was discovered.

        Returns:
            True if PTS device found, False otherwise
        """
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        if found:
            self.log.info("PTS device discovered")
        else:
            self.log.error("PTS device not discovered")
        return found

    def handle_wid_78(self):
        """Initiate LE connection to PTS device.

        Returns:
            True if connection successful
        """
        self.log.info("Initiating LE connection")
        success = self.remote_bt.le_scan_connect(constants.pts_address)
        return bool(success)

    def handle_wid_77(self):
        """Disconnect active LE connection with PTS device."""
        self.remote_bt.disconnect(constants.pts_address)
        return True

    def handle_wid_100(self):
        """Initiate pairing in Non-Bondable mode.
        Used in non-bondable pairing validation.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.set_pairable(False)
        if not success:
            return False
        success = self.remote_bt.pair(constants.pts_address)
        return bool(success)

    def handle_wid_108(self):
        """Initiate pairing in Bondable mode.
        Used in bonding validation test cases.
        """
        self.remote_bt.power_on_adapter()
        success = self.remote_bt.set_pairable(True)
        if not success:
            return False

        success = self.remote_bt.pair(constants.pts_address)
        return bool(success)

    def handle_wid_208(self):
        """Initiate pairing after enabling pairable mode.
        Used in security test procedures.
        """
        self.remote_bt.set_pairable(True)
        success = self.remote_bt.pair(constants.pts_address)
        return bool(success)

    def handle_wid_135(self):
        """Remove bonding information of PTS device.
        Used for cleanup between bonding test cases.
        """
        self.remote_bt.unpair_device(constants.pts_address)
        return True

    def handle_wid_24(self):
        """Advertise using Local Name AD structure.

        GAP/ADV test case validation for Complete Local Name.
        """
        success = self.remote_bt.start_advertising(
            advertisement_data_key="local_name",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_35(self):
        """Advertise using Service UUID AD structure.
        Used in service UUID validation test cases.
        """
        success = self.remote_bt.start_advertising(
            advertisement_data_key="service_uuid",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_1003(self):
        """Confirm numeric comparison during LE Secure Connections pairing.

        Returns:
            Always True (auto-confirm)
        """
        self.log.info("Confirming numeric comparison")
        return True

    def handle_wid_2004(self):
        """Confirm Secure Connections numeric comparison."""
        time.sleep(1)
        return True

    def handle_wid_1302(self):
        """Start Connectionless Slave Broadcast and Synchronization Train.
        Used in CSB synchronization test cases.
        """
        success = self.remote_bt.start_csb_and_sync_train()
        return bool(success)

    def handle_wid_20115(self):
        """Disconnect from PTS device."""
        self.remote_bt.disconnect(constants.pts_address)
        return True

    def handle_wid_25(self):
        """Advertise using Flags AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="flags",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_26(self):
        """Advertise using Manufacturer Specific Data AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="manufacturer",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_27(self):
        """Advertise using TX Power Level AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="tx_power",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_29(self):
        """Advertise using PPCI AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="ppci",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_56(self):
        """Advertise using Service Solicitation AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="service_solicit",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_57(self):
        """Advertise using Service Data AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="service_data",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_149(self):
        """Advertise using Appearance AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="appearance",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_152(self):
        """Advertise using Public Target Address AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="public_target",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_153(self):
        """Advertise using Random Target Address AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="random_target",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_154(self):
        """Advertise using Advertising Interval AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="adv_interval",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_173(self):
        """Advertise using URI AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="uri",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_243(self):
        """Advertise using LE Supported Features AD structure."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="le_features",
            advertisement_param_key="connectable"
        )
        return bool(success)

    def handle_wid_5(self):
        """Enable Non-Discoverable and Non-Connectable advertising."""
        success = self.remote_bt.start_advertising("pts_non_discoverable", "non_connectable")()
        return bool(success)

    def handle_wid_11(self):
        """Stop discovery and confirm device is not discoverable.
        Used when PTS verifies that the IUT does not discover devices.
        """
        try:
            self.remote_bt.stop_discovery()
        except Exception as error:
            self.log.error(error)
        return True

    def handle_wid_14(self):
        """Verify that the PTS device was discovered during scanning."""
        devices = self.remote_bt.get_discovered_devices()
        found = any(
            d["address"].lower() == constants.pts_address.lower()
            for d in devices
        )
        self.remote_bt.stop_discovery()
        return bool(found)

    def handle_wid_30(self):
        """Enable Limited Discoverable Connectable advertising.
        Used in limited discoverable connectable validation.
        """
        self.remote_bt.stop_advertising()
        success = self.remote_bt.start_advertising(
            advertisement_data_key="pts_limited",
            advertisement_param_key="connectable"
        )()
        return bool(success)

    def handle_wid_31(self):
        """Disable discoverable mode.
        Used to validate non-discoverable behavior.
        """
        success = self.remote_bt.set_discoverable_mode(False)
        return bool(success)

    def handle_wid_32(self):
        """Enable Limited Discoverable mode."""
        success = self.remote_bt.set_limited_discoverable()
        return bool(success)

    def handle_wid_33(self):
        """Enable General Discoverable mode."""
        success = self.remote_bt.set_discoverable_mode(True)
        return bool(success)

    def handle_wid_34(self):
        """Disable discoverable mode for connectability validation."""
        success = self.remote_bt.set_discoverable_mode(False)
        return bool(success)

    def handle_wid_36(self):
        """Start discovery and verify PTS device is found.
        Used in BR/EDR and LE dual-mode discovery validation.
        """
        success = self.remote_bt.start_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        return bool(found)

    def handle_wid_49(self):
        """Enable Limited Discoverable Non-Connectable advertising."""
        success = self.remote_bt.start_advertising("pts_limited", "non_connectable")()
        return bool(success)

    def handle_wid_50(self):
        """Enable discoverable and connectable advertising."""
        self.remote_bt.set_discoverable_mode(True)
        success = self.remote_bt.start_advertising("pts_general", "connectable")()
        return bool(success)

    def handle_wid_51(self):
        """Enable General Discoverable Non-Connectable advertising."""
        self.remote_bt.stop_advertising()
        success = self.remote_bt.general_discoverable_advertise(
            connectable=False
        )
        time.sleep(0.3)
        return bool(success)

    def handle_wid_54(self):
        """Enable General Discoverable Non-Connectable advertising."""
        self.remote_bt.set_discoverable_mode(True)
        success = self.remote_bt.start_advertising("pts_general", "non_connectable")()
        return bool(success)

    def handle_wid_55(self):
        """Enable Limited Discoverable Non-Connectable advertising."""
        self.remote_bt.start_advertising("pts_limited", "non_connectable")()
        success = self.remote_bt.start_advertising("pts_general", "non_connectable")()
        return bool(success)

    def handle_wid_59(self):
        """Enable Limited Discoverable Non-Connectable advertising."""
        self.remote_bt.set_discoverable_mode(True)
        success = self.remote_bt.start_advertising("pts_limited", "non_connectable")()
        return bool(success)

    def handle_wid_60(self):
        """Enable Directed Connectable advertising."""
        success = self.remote_bt.start_advertising("pts_directed_advertise", "connectable_directed")()
        return bool(success)

    def handle_wid_72(self):
        """Enable Non-Discoverable Connectable advertising."""
        self.remote_bt.set_discoverable_mode(False)
        success = self.remote_bt.start_advertising("pts_general", "connectable")()
        return bool(success)

    def handle_wid_74(self):
        """Enable Non-Discoverable Connectable advertising."""
        success = self.remote_bt.start_advertising(
            advertisement_data_key="pts_non_discoverable",
            advertisement_param_key="connectable"
        )()
        time.sleep(0.3)
        return bool(success)

    def handle_wid_75(self):
        """Enable Non-Discoverable Connectable advertising."""
        success = self.remote_bt.start_advertising(
            advertisement_data_key="pts_non_discoverable",
            advertisement_param_key="connectable"
        )()
        time.sleep(0.3)
        return bool(success)

    def handle_wid_76(self):
        """Enable Limited Discoverable Connectable advertising."""
        success = self.remote_bt.start_advertising(
            advertisement_data_key="pts_limited",
            advertisement_param_key="connectable"
        )()
        time.sleep(0.3)
        return bool(success)

    def handle_wid_86(self):
        """Discover and connect to PTS device.
        Used in name discovery and connection validation.
        """
        success = self.remote_bt.start_le_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        if not found:
            return False
        success = self.remote_bt.connect(constants.pts_address)
        return bool(success)

    def handle_wid_90(self):
        """Enable Connectable advertising using NRPA."""
        success = self.remote_bt.start_advertising("pts_general", "connectable", random_addr_key="nrpa")()
        return bool(success)

    def handle_wid_91(self):
        """Enable General Discoverable Connectable advertising."""
        success = self.remote_bt.general_discoverable_advertise(
            connectable=True
        )
        return bool(success)


    def handle_wid_102(self):
        """Discover, connect, and pair with PTS device."""
        self.remote_bt.set_pairable(True)
        success = self.remote_bt.start_le_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        if not found:
            return False
        success = self.remote_bt.connect(constants.pts_address)
        if not success:
            return False
        success = self.remote_bt.pair(constants.pts_address)
        return bool(success)

    def handle_wid_104(self):
        """Set device to Non-Bondable mode."""
        success = self.remote_bt.set_pairable(False)
        return bool(success)

    def handle_wid_105(self):
        """Enable discoverable, connectable, and pairable modes."""
        self.remote_bt.set_discoverable_mode(True)
        self.remote_bt.set_connectable(True)
        self.remote_bt.set_pairable(True)
        return True

    def handle_wid_118(self):
        """Disconnect and remove bonding information."""
        self.remote_bt.disconnect(constants.pts_address)
        success = self.remote_bt.unpair_device(constants.pts_address)
        return bool(success)

    def handle_wid_121(self):
        """Enable Non-Connectable advertising."""
        success = self.remote_bt.start_advertising("pts_general", "non_connectable")()
        return bool(success)

    def handle_wid_122(self):
        """Enable Discoverable Non-Connectable advertising."""
        self.remote_bt.set_discoverable_mode(True)
        success = self.remote_bt.start_advertising("pts_general", "non_connectable")()
        return bool(success)

    def handle_wid_146(self):
        """Perform discovery and verify PTS device found."""
        success = self.remote_bt.start_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        return bool(found)

    def handle_wid_147(self):
        """Perform LE discovery and verify PTS device found."""
        success = self.remote_bt.start_le_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        return bool(found)

    def handle_wid_157(self):
        """Wait for any advertising packet."""
        success = self.remote_bt.wait_for_any_advertisement(timeout=20)
        return bool(success)

    def handle_wid_160(self):
        """Enable Limited Discoverable Connectable advertising."""
        success = self.remote_bt.start_advertising(
            advertisement_data_key="pts_limited",
            advertisement_param_key="connectable"
        )()
        return bool(success)

    def handle_wid_164(self):
        """Perform discovery and verify PTS device found."""
        success = self.remote_bt.start_discovery()
        if not success:
            return False
        discovered_devices = self.remote_bt.get_discovered_devices()
        found = any(
            device["address"].lower() == constants.pts_address.lower()
            for device in discovered_devices
        )
        self.remote_bt.stop_discovery()
        return bool(found)

    def handle_wid_222(self):
        """Start discovery and initiate pairing."""
        self.remote_bt.start_discovery()
        success = self.remote_bt.pair(constants.pts_address)
        return bool(success)

    def handle_wid_232(self):
        """Advertise using Long Advertising Interval."""
        success = self.remote_bt.start_advertising(
            advertisement_structure_key="adv_interval_long",
            advertisement_param_key="connectable"
        )
        return bool(success)
