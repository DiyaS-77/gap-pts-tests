root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# python client.py pts_trigger --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 13:18:50,093 | INFO | ==============================
2026-02-13 13:18:50,093 | INFO | gRPC Client Started
2026-02-13 13:18:50,093 | INFO | ==============================
2026-02-13 13:18:50,097 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:18:50,097 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:18:50,109 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:18:50,109 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:19:09,342 | INFO | Starting project execution: GAP
2026-02-13 13:19:09,343 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:19:09,343 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:19:09,344 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:19:09,345 | INFO | Opening PTS workspace once
2026-02-13 13:19:09,345 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:19:09,346 | INFO | Selecting PTS project once
2026-02-13 13:19:09,346 | INFO | Selecting project: GAP
2026-02-13 13:19:09,347 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:19:09,347 | INFO | Registering PTS logger
2026-02-13 13:19:09,348 | INFO | Registering MMI handler
2026-02-13 13:19:09,348 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:19:09,349 | INFO | MMI RECEIVED
2026-02-13 13:19:09,350 | INFO | Project   : GAP
2026-02-13 13:19:09,350 | INFO | WID       : 25
2026-02-13 13:19:09,350 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:19:09,350 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:19:09,351 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:19:09,351 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:19:09,351 | INFO | Executing GAP handler for WID 25
2026-02-13 13:19:09,351 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:19:09,352 | INFO | WID 25 completed with result: False
2026-02-13 13:19:09,353 | INFO | MMI action not executed for WID 25
2026-02-13 13:19:09,353 | INFO | MMI response: Cancel
2026-02-13 13:19:09,354 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 13:19:09,354 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:19:09,355 | INFO | INDCSV
2026-02-13 13:19:09,355 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:19:09,356 | INFO | RESULT: INDCSV
2026-02-13 13:19:09,356 | INFO | Resetting DUT between tests
2026-02-13 13:19:09,357 | INFO | PTS test state stopped
2026-02-13 13:19:09,357 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:19:09,357 | INFO | 
2026-02-13 13:19:09,358 | INFO | ==============================
2026-02-13 13:19:09,358 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:19:09,359 | INFO | ==============================
2026-02-13 13:19:09,359 | INFO | GAP/ADV/BV-03-C : INDCSV : INDCSV
2026-02-13 13:19:09,360 | INFO | ------------------------------
2026-02-13 13:19:09,360 | INFO | Total testcases : 1
2026-02-13 13:19:09,361 | INFO | Passed          : 0
2026-02-13 13:19:09,361 | INFO | Failed          : 0
2026-02-13 13:19:09,362 | INFO | ==============================
2026-02-13 13:19:09,448 | INFO | Project execution finished
2026-02-13 13:19:09,449 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

