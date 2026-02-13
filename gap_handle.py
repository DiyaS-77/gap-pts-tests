root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# python client.py pts_trigger --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 13:39:39,321 | INFO | ==============================
2026-02-13 13:39:39,321 | INFO | gRPC Client Started
2026-02-13 13:39:39,321 | INFO | ==============================
2026-02-13 13:39:39,325 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:39:39,325 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:39:39,332 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:39:39,332 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:39:58,421 | INFO | Starting project execution: GAP
2026-02-13 13:39:58,422 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:39:58,423 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:39:58,423 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:39:58,424 | INFO | Opening PTS workspace once
2026-02-13 13:39:58,424 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:39:58,425 | INFO | Selecting PTS project once
2026-02-13 13:39:58,425 | INFO | Selecting project: GAP
2026-02-13 13:39:58,425 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:39:58,426 | INFO | Registering PTS logger
2026-02-13 13:39:58,426 | INFO | Registering MMI handler
2026-02-13 13:39:58,427 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:39:58,427 | INFO | MMI RECEIVED
2026-02-13 13:39:58,427 | INFO | Project   : GAP
2026-02-13 13:39:58,428 | INFO | WID       : 25
2026-02-13 13:39:58,428 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:39:58,428 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:39:58,429 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:39:58,429 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:39:58,429 | INFO | Executing GAP handler for WID 25
2026-02-13 13:39:58,430 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:39:58,430 | INFO | WID 25 completed with result: False
2026-02-13 13:39:58,431 | INFO | MMI action not executed for WID 25
2026-02-13 13:39:58,431 | INFO | MMI response: Cancel
2026-02-13 13:39:58,432 | INFO | PTS cannot find any address in advertising reports that matches ixit.
2026-02-13 13:39:58,432 | INFO | Failed to scan advertising packets.
2026-02-13 13:39:58,433 | INFO | Resetting DUT between tests
2026-02-13 13:39:58,433 | INFO | PTS test state stopped
2026-02-13 13:39:58,434 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:39:58,434 | INFO | 
2026-02-13 13:39:58,435 | INFO | ==============================
2026-02-13 13:39:58,435 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:39:58,435 | INFO | ==============================
2026-02-13 13:39:58,436 | INFO | GAP/ADV/BV-03-C : None : Failed to scan advertising packets.
2026-02-13 13:39:58,436 | INFO | ------------------------------
2026-02-13 13:39:58,437 | INFO | Total testcases : 1
2026-02-13 13:39:58,437 | INFO | Passed          : 0
2026-02-13 13:39:58,438 | INFO | Failed          : 0
2026-02-13 13:39:58,438 | INFO | ==============================
2026-02-13 13:39:58,536 | INFO | Project execution finished
2026-02-13 13:39:58,537 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

