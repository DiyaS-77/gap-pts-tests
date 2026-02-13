root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# python client.py pts_trigger --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 12:28:51,001 | INFO | ==============================
2026-02-13 12:28:51,001 | INFO | gRPC Client Started
2026-02-13 12:28:51,001 | INFO | ==============================
2026-02-13 12:28:51,005 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 12:28:51,005 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:28:51,017 | INFO | Loaded 4 testcases for GAP
2026-02-13 12:28:51,018 | INFO |  ===== [1/4] Running GAP/BROB/OBSV/BV-01-C =====
2026-02-13 12:29:10,338 | INFO | Starting project execution: GAP
2026-02-13 12:29:10,339 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:29:10,340 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 12:29:10,340 | INFO | gRPC server is running 10.91.220.35
2026-02-13 12:29:10,341 | INFO | Opening PTS workspace once
2026-02-13 12:29:10,341 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 12:29:10,342 | INFO | Selecting PTS project once
2026-02-13 12:29:10,342 | INFO | Selecting project: GAP
2026-02-13 12:29:10,343 | INFO | Running test case: GAP/BROB/OBSV/BV-01-C
2026-02-13 12:29:10,343 | INFO | Registering PTS logger
2026-02-13 12:29:10,344 | INFO | Registering MMI handler
2026-02-13 12:29:10,344 | INFO | Running test case: GAP / GAP/BROB/OBSV/BV-01-C
2026-02-13 12:29:10,345 | INFO | MMI RECEIVED
2026-02-13 12:29:10,345 | INFO | Project   : GAP
2026-02-13 12:29:10,346 | INFO | WID       : 12
2026-02-13 12:29:10,346 | INFO | Testcase  : GAP/BROB/OBSV/BV-01-C
2026-02-13 12:29:10,347 | INFO | Desc      : Please start passive scanning. Press OK to continue.
2026-02-13 12:29:10,347 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:29:10,348 | INFO | Resolving handler: handle_wid_12
2026-02-13 12:29:10,348 | INFO | Executing GAP handler for WID 12
2026-02-13 12:29:10,348 | INFO | WID 12 completed with result: True
2026-02-13 12:29:10,349 | INFO | MMI response: OK
2026-02-13 12:29:10,349 | INFO | Server: SUCCESS with response=OK
2026-02-13 12:29:10,349 | INFO | MMI RECEIVED
2026-02-13 12:29:10,350 | INFO | Project   : GAP
2026-02-13 12:29:10,351 | INFO | WID       : 4
2026-02-13 12:29:10,351 | INFO | Testcase  : GAP/BROB/OBSV/BV-01-C
2026-02-13 12:29:10,352 | INFO | Desc      : Please confirm that IUT has received an Advertising Event then click OK.
2026-02-13 12:29:10,352 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:29:10,353 | INFO | MMI response: OK
2026-02-13 12:29:10,353 | INFO | GAP/BROB/OBSV/BV-01-C
2026-02-13 12:29:10,354 | INFO | PASS
2026-02-13 12:29:10,354 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:29:10,355 | INFO | RESULT: PASS
2026-02-13 12:29:10,355 | INFO | Resetting DUT between tests
2026-02-13 12:29:10,356 | INFO | PTS test state stopped
2026-02-13 12:29:10,356 | INFO | GAP/BROB/OBSV/BV-01-C DONE
2026-02-13 12:29:10,357 | INFO |  ===== [2/4] Running GAP/BROB/OBSV/BV-02-C =====
2026-02-13 12:29:18,229 | INFO | Running test case: GAP/BROB/OBSV/BV-02-C
2026-02-13 12:29:18,229 | INFO | Running test case: GAP / GAP/BROB/OBSV/BV-02-C
2026-02-13 12:29:18,230 | INFO | MMI RECEIVED
2026-02-13 12:29:18,230 | INFO | Project   : GAP
2026-02-13 12:29:18,231 | INFO | WID       : 169
2026-02-13 12:29:18,231 | INFO | Testcase  : GAP/BROB/OBSV/BV-02-C
2026-02-13 12:29:18,231 | INFO | Desc      : Please start observation procedure. Press OK to continue.
2026-02-13 12:29:18,232 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:29:18,232 | INFO | MMI response: OK
2026-02-13 12:29:18,232 | INFO | Server: SUCCESS with response=OK
2026-02-13 12:29:18,233 | INFO | MMI RECEIVED
2026-02-13 12:29:18,233 | INFO | Project   : GAP
2026-02-13 12:29:18,233 | INFO | WID       : 4
2026-02-13 12:29:18,234 | INFO | Testcase  : GAP/BROB/OBSV/BV-02-C
2026-02-13 12:29:18,234 | INFO | Desc      : Please confirm that IUT has received an Advertising Event then click OK.
2026-02-13 12:29:18,234 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:29:18,234 | INFO | MMI response: OK
2026-02-13 12:29:18,235 | INFO | GAP/BROB/OBSV/BV-02-C
2026-02-13 12:29:18,235 | INFO | PASS
2026-02-13 12:29:18,235 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:29:18,235 | INFO | RESULT: PASS
2026-02-13 12:29:18,236 | INFO | Resetting DUT between tests
2026-02-13 12:29:18,236 | INFO | PTS test state stopped
2026-02-13 12:29:18,236 | INFO | GAP/BROB/OBSV/BV-02-C DONE
2026-02-13 12:29:18,236 | INFO |  ===== [3/4] Running GAP/BROB/OBSV/BV-05-C =====
2026-02-13 12:29:25,268 | INFO | Running test case: GAP/BROB/OBSV/BV-05-C
2026-02-13 12:29:25,268 | INFO | Running test case: GAP / GAP/BROB/OBSV/BV-05-C
2026-02-13 12:29:25,269 | INFO | MMI RECEIVED
2026-02-13 12:29:25,269 | INFO | Project   : GAP
2026-02-13 12:29:25,270 | INFO | WID       : 157
2026-02-13 12:29:25,270 | INFO | Testcase  : GAP/BROB/OBSV/BV-05-C
2026-02-13 12:29:25,271 | INFO | Desc      : Please confirm that IUT has received an Advertising data of "0201040503001801180D095054532D4741502D303642380319000000000000" And scan response data of "1324162F2F626C7565746F6F74682E636F6D0D0A0000000000000000000000" Click Yes if IUT receive advertising data and scan response data accordingly, otherwise click No.
2026-02-13 12:29:25,271 | INFO | Style     : MMI_Style_Yes_No1
2026-02-13 12:29:25,271 | INFO | MMI response: Yes
2026-02-13 12:29:25,272 | INFO | Server: SUCCESS with response=Yes
2026-02-13 12:29:25,272 | INFO | GAP/BROB/OBSV/BV-05-C
2026-02-13 12:29:25,273 | INFO | PASS
2026-02-13 12:29:25,274 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:29:25,274 | INFO | RESULT: PASS
2026-02-13 12:29:25,275 | INFO | Resetting DUT between tests
2026-02-13 12:29:25,275 | INFO | PTS test state stopped
2026-02-13 12:29:25,276 | INFO | GAP/BROB/OBSV/BV-05-C DONE
2026-02-13 12:29:25,276 | INFO |  ===== [4/4] Running GAP/BROB/OBSV/BV-06-C =====
2026-02-13 12:30:10,419 | INFO | Running test case: GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,420 | INFO | Running test case: GAP / GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,421 | INFO | MMI RECEIVED
2026-02-13 12:30:10,421 | INFO | Project   : GAP
2026-02-13 12:30:10,422 | INFO | WID       : 78
2026-02-13 12:30:10,422 | INFO | Testcase  : GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,423 | INFO | Desc      : Please send an LE connect request to establish a connection.
2026-02-13 12:30:10,424 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 12:30:10,424 | INFO | Resolving handler: handle_wid_78
2026-02-13 12:30:10,425 | INFO | Executing GAP handler for WID 78
2026-02-13 12:30:10,425 | INFO | Initiating LE connection
2026-02-13 12:30:10,426 | INFO | WID 78 completed with result: True
2026-02-13 12:30:10,426 | INFO | MMI response: OK
2026-02-13 12:30:10,427 | INFO | MMI RECEIVED
2026-02-13 12:30:10,427 | INFO | Project   : GAP
2026-02-13 12:30:10,427 | INFO | WID       : 208
2026-02-13 12:30:10,428 | INFO | Testcase  : GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,428 | INFO | Desc      : Please configure the IUT into LE Security Mode 1 Level 4 and start pairing process.
2026-02-13 12:30:10,428 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 12:30:10,429 | INFO | Resolving handler: handle_wid_208
2026-02-13 12:30:10,429 | INFO | Executing GAP handler for WID 208
2026-02-13 12:30:10,430 | INFO | WID 208 completed with result: True
2026-02-13 12:30:10,430 | INFO | MMI response: OK
2026-02-13 12:30:10,430 | INFO | MMI RECEIVED
2026-02-13 12:30:10,431 | INFO | Project   : GAP
2026-02-13 12:30:10,431 | INFO | WID       : 1003
2026-02-13 12:30:10,432 | INFO | Testcase  : GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,432 | INFO | Desc      : Please confirm the following number matches IUT: 202552.
2026-02-13 12:30:10,433 | INFO | Style     : MMI_Style_Yes_No1
2026-02-13 12:30:10,433 | INFO | Resolving handler: handle_wid_1003
2026-02-13 12:30:10,434 | INFO | Executing GAP handler for WID 1003
2026-02-13 12:30:10,434 | INFO | Confirming numeric comparison
2026-02-13 12:30:10,435 | INFO | WID 1003 completed with result: True
2026-02-13 12:30:10,435 | INFO | MMI response: Yes
2026-02-13 12:30:10,436 | INFO | Server: SUCCESS with response=OK
2026-02-13 12:30:10,436 | INFO | Server: SUCCESS with response=Yes
2026-02-13 12:30:10,437 | INFO | GAP/BROB/OBSV/BV-06-C
2026-02-13 12:30:10,437 | INFO | INDCSV
2026-02-13 12:30:10,438 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:30:10,438 | INFO | RESULT: INDCSV
2026-02-13 12:30:10,439 | INFO | Resetting DUT between tests
2026-02-13 12:30:10,439 | INFO | PTS test state stopped
2026-02-13 12:30:10,440 | INFO | GAP/BROB/OBSV/BV-06-C DONE
2026-02-13 12:30:10,440 | INFO | 
2026-02-13 12:30:10,441 | INFO | ==============================
2026-02-13 12:30:10,441 | INFO | PTS EXECUTION SUMMARY
2026-02-13 12:30:10,442 | INFO | ==============================
2026-02-13 12:30:10,442 | INFO | GAP/BROB/OBSV/BV-01-C : PASS
2026-02-13 12:30:10,442 | INFO | GAP/BROB/OBSV/BV-02-C : PASS
2026-02-13 12:30:10,443 | INFO | GAP/BROB/OBSV/BV-05-C : PASS
2026-02-13 12:30:10,443 | INFO | GAP/BROB/OBSV/BV-06-C : INDCSV : INDCSV
2026-02-13 12:30:10,444 | INFO | ------------------------------
2026-02-13 12:30:10,444 | INFO | Total testcases : 4
2026-02-13 12:30:10,445 | INFO | Passed          : 3
2026-02-13 12:30:10,445 | INFO | Failed          : 0
2026-02-13 12:30:10,446 | INFO | ==============================
2026-02-13 12:30:10,609 | INFO | Project execution finished
2026-02-13 12:30:10,610 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

