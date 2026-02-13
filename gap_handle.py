root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# python client.py pts_trigger --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 12:57:12,941 | INFO | ==============================
2026-02-13 12:57:12,941 | INFO | gRPC Client Started
2026-02-13 12:57:12,942 | INFO | ==============================
2026-02-13 12:57:12,945 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 12:57:12,945 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:57:12,952 | INFO | Loaded 1 testcases for GAP
2026-02-13 12:57:12,953 | INFO |  ===== [1/1] Running GAP/MOD/SYN/BV-01-C =====
2026-02-13 12:57:31,491 | INFO | Starting project execution: GAP
2026-02-13 12:57:31,491 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:57:31,492 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 12:57:31,493 | INFO | gRPC server is running 10.91.220.35
2026-02-13 12:57:31,493 | INFO | Opening PTS workspace once
2026-02-13 12:57:31,494 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 12:57:31,494 | INFO | Selecting PTS project once
2026-02-13 12:57:31,495 | INFO | Selecting project: GAP
2026-02-13 12:57:31,495 | INFO | Running test case: GAP/MOD/SYN/BV-01-C
2026-02-13 12:57:31,496 | INFO | Registering PTS logger
2026-02-13 12:57:31,496 | INFO | Registering MMI handler
2026-02-13 12:57:31,497 | INFO | Running test case: GAP / GAP/MOD/SYN/BV-01-C
2026-02-13 12:57:31,497 | INFO | MMI RECEIVED
2026-02-13 12:57:31,497 | INFO | Project   : GAP
2026-02-13 12:57:31,497 | INFO | WID       : 1302
2026-02-13 12:57:31,498 | INFO | Testcase  : GAP/MOD/SYN/BV-01-C
2026-02-13 12:57:31,498 | INFO | Desc      : Please make a sure that IUT configure, start connection broadcast and start synchronization train. Click OK after IUT started the synchronization train.
2026-02-13 12:57:31,498 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:57:31,498 | INFO | Resolving handler: handle_wid_1302
2026-02-13 12:57:31,498 | INFO | No GAP handler implemented for WID 1302
2026-02-13 12:57:31,498 | INFO | No automation implemented for project=GAP, WID=1302
2026-02-13 12:57:31,498 | INFO | MMI action not executed for WID 1302
2026-02-13 12:57:31,499 | INFO | MMI response: Cancel
2026-02-13 12:57:31,499 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 12:57:31,499 | INFO | GAP/MOD/SYN/BV-01-C
2026-02-13 12:57:31,499 | INFO | INDCSV
2026-02-13 12:57:31,499 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:57:31,499 | INFO | RESULT: INDCSV
2026-02-13 12:57:31,499 | INFO | Resetting DUT between tests
2026-02-13 12:57:31,499 | INFO | PTS test state stopped
2026-02-13 12:57:31,500 | INFO | GAP/MOD/SYN/BV-01-C DONE
2026-02-13 12:57:31,500 | INFO | 
2026-02-13 12:57:31,500 | INFO | ==============================
2026-02-13 12:57:31,500 | INFO | PTS EXECUTION SUMMARY
2026-02-13 12:57:31,500 | INFO | ==============================
2026-02-13 12:57:31,500 | INFO | GAP/MOD/SYN/BV-01-C : INDCSV : Server: SUCCESS with response=Cancel
2026-02-13 12:57:31,500 | INFO | ------------------------------
2026-02-13 12:57:31,500 | INFO | Total testcases : 1
2026-02-13 12:57:31,501 | INFO | Passed          : 0
2026-02-13 12:57:31,501 | INFO | Failed          : 0
2026-02-13 12:57:31,501 | INFO | ==============================
2026-02-13 12:57:31,572 | INFO | Project execution finished
2026-02-13 12:57:31,573 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

