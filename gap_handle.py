root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# python client.py pts_trigger --config config.json --testbed TESTBED_1 --workspace GAP_WS --project GAP
/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 12:06:25,963 | INFO | ==============================
2026-02-13 12:06:25,963 | INFO | gRPC Client Started
2026-02-13 12:06:25,963 | INFO | ==============================
2026-02-13 12:06:25,967 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 12:06:25,967 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:06:25,974 | INFO | Loaded 79 testcases for GAP
2026-02-13 12:06:25,974 | INFO |  ===== [1/79] Running GAP/BROB/OBSV/BV-01-C =====
2026-02-13 12:06:45,043 | INFO | Starting project execution: GAP
2026-02-13 12:06:45,044 | INFO | Loading testbed configuration from: config.json
2026-02-13 12:06:45,044 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 12:06:45,045 | INFO | gRPC server is running 10.91.220.35
2026-02-13 12:06:45,045 | INFO | Opening PTS workspace once
2026-02-13 12:06:45,046 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 12:06:45,046 | INFO | Selecting PTS project once
2026-02-13 12:06:45,047 | INFO | Selecting project: GAP
2026-02-13 12:06:45,047 | INFO | Running test case: GAP/BROB/OBSV/BV-01-C
2026-02-13 12:06:45,047 | INFO | Registering PTS logger
2026-02-13 12:06:45,048 | INFO | Registering MMI handler
2026-02-13 12:06:45,049 | INFO | Running test case: GAP / GAP/BROB/OBSV/BV-01-C
2026-02-13 12:06:45,049 | INFO | MMI RECEIVED
2026-02-13 12:06:45,049 | INFO | Project   : GAP
2026-02-13 12:06:45,050 | INFO | WID       : 12
2026-02-13 12:06:45,050 | INFO | Testcase  : GAP/BROB/OBSV/BV-01-C
2026-02-13 12:06:45,051 | INFO | Desc      : Please start passive scanning. Press OK to continue.
2026-02-13 12:06:45,051 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:06:45,052 | INFO | Resolving handler: handle_wid_12
2026-02-13 12:06:45,052 | INFO | Executing GAP handler for WID 12
2026-02-13 12:06:45,053 | INFO | WID 12 completed with result: True
2026-02-13 12:06:45,053 | INFO | MMI response: OK
2026-02-13 12:06:45,054 | INFO | Server: SUCCESS with response=OK
2026-02-13 12:06:45,054 | INFO | MMI RECEIVED
2026-02-13 12:06:45,055 | INFO | Project   : GAP
2026-02-13 12:06:45,055 | INFO | WID       : 4
2026-02-13 12:06:45,056 | INFO | Testcase  : GAP/BROB/OBSV/BV-01-C
2026-02-13 12:06:45,056 | INFO | Desc      : Please confirm that IUT has received an Advertising Event then click OK.
2026-02-13 12:06:45,057 | INFO | Style     : MMI_Style_Ok_Cancel1
2026-02-13 12:06:45,057 | INFO | MMI response: OK
2026-02-13 12:06:45,058 | INFO | GAP/BROB/OBSV/BV-01-C
2026-02-13 12:06:45,058 | INFO | PASS
2026-02-13 12:06:45,059 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 12:06:45,059 | INFO | RESULT: PASS
2026-02-13 12:06:45,060 | INFO | Resetting DUT between tests
2026-02-13 12:06:45,060 | INFO | PTS test state stopped
2026-02-13 12:06:45,061 | INFO | Project failed: 'tuple' object has no attribute 'get_last_verdict'
2026-02-13 12:06:45,061 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

