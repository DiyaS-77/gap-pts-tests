2026-02-13 13:32:41,652 | INFO | ==============================
2026-02-13 13:32:41,652 | INFO | gRPC Client Started
2026-02-13 13:32:41,652 | INFO | ==============================
2026-02-13 13:32:41,656 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:32:41,656 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:32:41,668 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:32:41,668 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:33:01,476 | INFO | Starting project execution: GAP
2026-02-13 13:33:01,477 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:33:01,477 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:33:01,478 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:33:01,479 | INFO | Opening PTS workspace once
2026-02-13 13:33:01,479 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:33:01,480 | INFO | Selecting PTS project once
2026-02-13 13:33:01,481 | INFO | Selecting project: GAP
2026-02-13 13:33:01,481 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:33:01,481 | INFO | Registering PTS logger
2026-02-13 13:33:01,482 | INFO | Registering MMI handler
2026-02-13 13:33:01,483 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:33:01,483 | INFO | MMI RECEIVED
2026-02-13 13:33:01,483 | INFO | Project   : GAP
2026-02-13 13:33:01,484 | INFO | WID       : 25
2026-02-13 13:33:01,484 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:33:01,484 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:33:01,484 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:33:01,484 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:33:01,485 | INFO | Executing GAP handler for WID 25
2026-02-13 13:33:01,485 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:33:01,486 | INFO | WID 25 completed with result: False
2026-02-13 13:33:01,486 | INFO | MMI action not executed for WID 25
2026-02-13 13:33:01,487 | INFO | MMI response: Cancel
2026-02-13 13:33:01,487 | INFO | PASS
2026-02-13 13:33:01,488 | INFO | PASS
2026-02-13 13:33:01,488 | INFO | PASS
2026-02-13 13:33:01,489 | INFO | PASS
2026-02-13 13:33:01,489 | INFO | PASS
2026-02-13 13:33:01,490 | INFO | PASS
2026-02-13 13:33:01,490 | INFO | PASS
2026-02-13 13:33:01,491 | INFO | PASS
2026-02-13 13:33:01,491 | INFO | PASS
2026-02-13 13:33:01,492 | INFO | PASS
2026-02-13 13:33:01,492 | INFO | PASS
2026-02-13 13:33:01,493 | INFO | PASS
2026-02-13 13:33:01,493 | INFO | INDCSV
2026-02-13 13:33:01,494 | INFO | PTS cannot find any address in advertising reports that matches ixit.
2026-02-13 13:33:01,494 | INFO | Failed to scan advertising packets.
2026-02-13 13:33:01,495 | INFO | INDCSV
2026-02-13 13:33:01,495 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:33:01,496 | INFO | RESULT: INDCSV
2026-02-13 13:33:01,496 | INFO | Resetting DUT between tests
2026-02-13 13:33:01,497 | INFO | PTS test state stopped
2026-02-13 13:33:01,497 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:33:01,497 | INFO | 
2026-02-13 13:33:01,498 | INFO | ==============================
2026-02-13 13:33:01,498 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:33:01,499 | INFO | ==============================
2026-02-13 13:33:01,499 | INFO | GAP/ADV/BV-03-C : INDCSV : Failed to scan advertising packets.
2026-02-13 13:33:01,500 | INFO | ------------------------------
2026-02-13 13:33:01,501 | INFO | Total testcases : 1
2026-02-13 13:33:01,501 | INFO | Passed          : 0
2026-02-13 13:33:01,501 | INFO | Failed          : 0
2026-02-13 13:33:01,502 | INFO | ==============================
2026-02-13 13:33:01,611 | INFO | Project execution finished
2026-02-13 13:33:01,612 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

