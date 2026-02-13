r --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 13:23:08,436 | INFO | ==============================
2026-02-13 13:23:08,436 | INFO | gRPC Client Started
2026-02-13 13:23:08,436 | INFO | ==============================
2026-02-13 13:23:08,440 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:23:08,440 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:23:08,455 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:23:08,455 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:23:26,881 | INFO | Starting project execution: GAP
2026-02-13 13:23:26,882 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:23:26,882 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:23:26,883 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:23:26,883 | INFO | Opening PTS workspace once
2026-02-13 13:23:26,884 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:23:26,885 | INFO | Selecting PTS project once
2026-02-13 13:23:26,885 | INFO | Selecting project: GAP
2026-02-13 13:23:26,886 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:23:26,886 | INFO | Registering PTS logger
2026-02-13 13:23:26,886 | INFO | Registering MMI handler
2026-02-13 13:23:26,886 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:23:26,887 | INFO | MMI RECEIVED
2026-02-13 13:23:26,887 | INFO | Project   : GAP
2026-02-13 13:23:26,887 | INFO | WID       : 25
2026-02-13 13:23:26,888 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:23:26,888 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:23:26,888 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:23:26,888 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:23:26,888 | INFO | Executing GAP handler for WID 25
2026-02-13 13:23:26,889 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:23:26,889 | INFO | WID 25 completed with result: False
2026-02-13 13:23:26,889 | INFO | MMI action not executed for WID 25
2026-02-13 13:23:26,889 | INFO | MMI response: Cancel
2026-02-13 13:23:26,889 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 13:23:26,890 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:23:26,890 | INFO | INDCSV
2026-02-13 13:23:26,890 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:23:26,890 | INFO | RESULT: INDCSV
2026-02-13 13:23:26,890 | INFO | Resetting DUT between tests
2026-02-13 13:23:26,890 | INFO | PTS test state stopped
2026-02-13 13:23:26,890 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:23:26,890 | INFO | 
2026-02-13 13:23:26,891 | INFO | ==============================
2026-02-13 13:23:26,891 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:23:26,891 | INFO | ==============================
2026-02-13 13:23:26,891 | INFO | GAP/ADV/BV-03-C : INDCSV : Failure reason not provided by PTS
2026-02-13 13:23:26,891 | INFO | ------------------------------
2026-02-13 13:23:26,891 | INFO | Total testcases : 1
2026-02-13 13:23:26,891 | INFO | Passed          : 0
2026-02-13 13:23:26,891 | INFO | Failed          : 0
2026-02-13 13:23:26,892 | INFO | ==============================
2026-02-13 13:23:26,959 | INFO | Project execution finished
2026-02-13 13:23:26,960 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 
