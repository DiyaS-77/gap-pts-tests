or version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 12:52:13,250 | INFO | ==============================
2026-02-13 12:52:13,250 | INFO | gRPC Client Started
2026-02-13 12:52:13,251 | INFO | ==============================
2026-02-13 12:52:13,254 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 12:52:13,254 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:52:13,264 | INFO | Loaded 1 testcases for GAP
2026-02-13 12:52:13,264 | INFO |  ===== [1/1] Running GAP/MOD/SYN/BV-01-C =====
2026-02-13 12:52:31,866 | INFO | Starting project execution: GAP
2026-02-13 12:52:31,867 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:52:31,867 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 12:52:31,868 | INFO | gRPC server is running 10.91.220.35
2026-02-13 12:52:31,868 | INFO | Opening PTS workspace once
2026-02-13 12:52:31,869 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 12:52:31,869 | INFO | Selecting PTS project once
2026-02-13 12:52:31,870 | INFO | Selecting project: GAP
2026-02-13 12:52:31,870 | INFO | Running test case: GAP/MOD/SYN/BV-01-C
2026-02-13 12:52:31,871 | INFO | Registering PTS logger
2026-02-13 12:52:31,871 | INFO | Registering MMI handler
2026-02-13 12:52:31,871 | INFO | Running test case: GAP / GAP/MOD/SYN/BV-01-C
2026-02-13 12:52:31,872 | INFO | MMI RECEIVED
2026-02-13 12:52:31,872 | INFO | Project   : GAP
2026-02-13 12:52:31,873 | INFO | WID       : 1302
2026-02-13 12:52:31,874 | INFO | Testcase  : GAP/MOD/SYN/BV-01-C
2026-02-13 12:52:31,874 | INFO | Desc      : Please make a sure that IUT configure, start connection broadcast and start synchronization train. Click OK after IUT started the synchronization train.
2026-02-13 12:52:31,874 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:52:31,875 | INFO | Resolving handler: handle_wid_1302
2026-02-13 12:52:31,875 | INFO | No GAP handler implemented for WID 1302
2026-02-13 12:52:31,876 | INFO | No automation implemented for project=GAP, WID=1302
2026-02-13 12:52:31,876 | INFO | MMI action not executed for WID 1302
2026-02-13 12:52:31,877 | INFO | MMI response: Cancel
2026-02-13 12:52:31,877 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 12:52:31,878 | INFO | GAP/MOD/SYN/BV-01-C
2026-02-13 12:52:31,878 | INFO | INDCSV
2026-02-13 12:52:31,879 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:52:31,879 | INFO | RESULT: INDCSV
2026-02-13 12:52:31,880 | INFO | Resetting DUT between tests
2026-02-13 12:52:31,880 | INFO | PTS test state stopped
2026-02-13 12:52:31,880 | INFO | GAP/MOD/SYN/BV-01-C DONE
2026-02-13 12:52:31,881 | INFO | 
2026-02-13 12:52:31,881 | INFO | ==============================
2026-02-13 12:52:31,882 | INFO | PTS EXECUTION SUMMARY
2026-02-13 12:52:31,882 | INFO | ==============================
2026-02-13 12:52:31,883 | INFO | GAP/MOD/SYN/BV-01-C : INDCSV : INDCSV
2026-02-13 12:52:31,883 | INFO | ------------------------------
2026-02-13 12:52:31,884 | INFO | Total testcases : 1
2026-02-13 12:52:31,884 | INFO | Passed          : 0
2026-02-13 12:52:31,885 | INFO | Failed          : 0
2026-02-13 12:52:31,885 | INFO | ==============================
2026-02-13 12:52:31,976 | INFO | Project execution finished
2026-02-13 12:52:31,977 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

