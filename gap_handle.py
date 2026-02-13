/usr/local/lib/python3.11/dist-packages/google/protobuf/runtime_version.py:98: UserWarning: Protobuf gencode version 5.29.0 is exactly one major version older than the runtime version 6.31.1 at pts_trigger.proto. Please update the gencode to avoid compatibility violations in the next runtime release.
  warnings.warn(
2026-02-13 13:30:02,290 | INFO | ==============================
2026-02-13 13:30:02,290 | INFO | gRPC Client Started
2026-02-13 13:30:02,290 | INFO | ==============================
2026-02-13 13:30:02,294 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:30:02,294 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:30:02,306 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:30:02,306 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:30:22,311 | INFO | Starting project execution: GAP
2026-02-13 13:30:22,312 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:30:22,313 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:30:22,313 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:30:22,314 | INFO | Opening PTS workspace once
2026-02-13 13:30:22,314 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:30:22,314 | INFO | Selecting PTS project once
2026-02-13 13:30:22,315 | INFO | Selecting project: GAP
2026-02-13 13:30:22,315 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:30:22,315 | INFO | Registering PTS logger
2026-02-13 13:30:22,316 | INFO | Registering MMI handler
2026-02-13 13:30:22,316 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:30:22,317 | INFO | MMI RECEIVED
2026-02-13 13:30:22,317 | INFO | Project   : GAP
2026-02-13 13:30:22,318 | INFO | WID       : 25
2026-02-13 13:30:22,318 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:30:22,319 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:30:22,319 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:30:22,320 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:30:22,320 | INFO | Executing GAP handler for WID 25
2026-02-13 13:30:22,321 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:30:22,321 | INFO | WID 25 completed with result: False
2026-02-13 13:30:22,322 | INFO | MMI action not executed for WID 25
2026-02-13 13:30:22,322 | INFO | MMI response: Cancel
2026-02-13 13:30:22,323 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 13:30:22,323 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,324 | INFO | 
2026-02-13 13:30:22,324 | INFO | Build date: Dec 11 2025, 11:52:49
2026-02-13 13:30:22,325 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:30:22,325 | INFO | HCI!HCI_RESET
2026-02-13 13:30:22,326 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,326 | INFO | PASS
2026-02-13 13:30:22,327 | INFO | HCI!HCI_READ_LOCAL_VERSION_INFORMATION
2026-02-13 13:30:22,327 | INFO | HCI?HCI_READ_LOCAL_VERSION_INFORMATION_COMPLETE_EVENT{
                           status=HCI_OK,
                           hciVersion=0x08,
                           hciRevision=0x30E8,
                           lmpVersion=0x08,
                           manufacturerName=0x000A,
                           lmpSubversion=0x30E8
                         }
2026-02-13 13:30:22,328 | INFO | PASS
2026-02-13 13:30:22,328 | INFO | HCI!HCI_LE_SET_EVENT_MASK{
                           leEventMask=0x000000000000001F
                         }
2026-02-13 13:30:22,329 | INFO | HCI?HCI_LE_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,329 | INFO | HCI!HCI_SET_EVENT_MASK{
                           eventMask=0x3FFFFFFFFFFFFFFF
                         }
2026-02-13 13:30:22,329 | INFO | HCI?HCI_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,330 | INFO | PASS
2026-02-13 13:30:22,330 | INFO | HCI!HCI_READ_LOCAL_SUPPORTED_FEATURES
2026-02-13 13:30:22,331 | INFO | HCI?HCI_READ_LOCAL_SUPPORTED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x875B1FD87E8FFFFF
                         }
2026-02-13 13:30:22,331 | INFO | PASS
2026-02-13 13:30:22,331 | INFO | HCI!HCI_READ_LOCAL_EXTENDED_FEATURES{
                           page_number=0x01
                         }
2026-02-13 13:30:22,332 | INFO | HCI?HCI_READ_LOCAL_EXTENDED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x0000000000000000
                         }
2026-02-13 13:30:22,332 | INFO | PASS
2026-02-13 13:30:22,333 | INFO | HCI!HCI_READ_LOCAL_EXTENDED_FEATURES{
                           page_number=0x02
                         }
2026-02-13 13:30:22,333 | INFO | HCI?HCI_READ_LOCAL_EXTENDED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x000000000000030F
                         }
2026-02-13 13:30:22,334 | INFO | PASS
2026-02-13 13:30:22,334 | INFO | HCI!HCI_READ_LOCAL_SUPPORTED_COMMANDS
2026-02-13 13:30:22,335 | INFO | HCI?HCI_READ_LOCAL_SUPPORTED_COMMANDS_COMPLETE_EVENT{
                           status=HCI_OK,
                           supported_commands=0x00000000000000000000000000000000000000000000000000000000000030FFFFC0007FFFFFF7610004001CFF83F73FFEE80FF3FFFFFFFFFFFFFFFE03FFFFFF
                         }
2026-02-13 13:30:22,335 | INFO | PASS
2026-02-13 13:30:22,336 | INFO | HCI!HCI_READ_BD_ADDR
2026-02-13 13:30:22,336 | INFO | HCI?HCI_READ_BD_ADDR_COMPLETE_EVENT{
                           status=HCI_OK,
                           bdAddress=0x001BDCF21F7B
                         }
2026-02-13 13:30:22,336 | INFO | PASS
2026-02-13 13:30:22,337 | INFO | HCI!HCI_WRITE_LE_HOST_SUPPORTED{
                           leSupportedHost=HCI_LE_SUPPORTED_HOST_ENABLED,
                           simultaneousLeHost=HCI_SIMULTANEOUS_LE_HOST_ENABLED
                         }
2026-02-13 13:30:22,337 | INFO | HCI?HCI_WRITE_LE_HOST_SUPPORTED_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,337 | INFO | HCI!HCI_LE_LOCAL_SUPPORTED_FEATURES
2026-02-13 13:30:22,338 | INFO | HCI?HCI_LE_READ_LOCAL_SUPPORTED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           leFeatures=0x000000000000001F
                         }
2026-02-13 13:30:22,338 | INFO | PASS
2026-02-13 13:30:22,339 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000900010003700000DA00010000000000
                         }
2026-02-13 13:30:22,339 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=19,
                           DATA=C201000900010003700000DA00010000000700
                         }
2026-02-13 13:30:22,339 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000900020003700000DB00010000000000
                         }
2026-02-13 13:30:22,340 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=19,
                           DATA=C201000900020003700000DB00010000001000
                         }
2026-02-13 13:30:22,340 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000C00030003700000EF00040000000000000000000000
                         }
2026-02-13 13:30:22,340 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=25,
                           DATA=C201000C00030003700000EF0004000000FFFF8F7ED81F5B87
                         }
2026-02-13 13:30:22,341 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000C000400037000002301040000000000000000000000
                         }
2026-02-13 13:30:22,341 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=25,
                           DATA=C201000C000400037000002301040000000F03000000000000
                         }
2026-02-13 13:30:22,341 | INFO | PASS
2026-02-13 13:30:22,342 | INFO | HCI!HCI_LE_SET_EVENT_MASK{
                           leEventMask=0x000000000000001F
                         }
2026-02-13 13:30:22,342 | INFO | HCI?HCI_LE_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,342 | INFO | HCI!HCI_SET_EVENT_MASK{
                           eventMask=0x3FFFFFFFFFFFFFFF
                         }
2026-02-13 13:30:22,343 | INFO | HCI?HCI_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,343 | INFO | PASS
2026-02-13 13:30:22,343 | INFO | HCI!HCI_LE_SET_SCAN_PARAMETERS{
                           leScanType=HCI_LE_ACTIVE_SCANNING,
                           leScanInterval=0x001E,
                           leScanWindow=0x001E,
                           ownAddressType=HCI_LE_PUBLIC_DEVICE_ADDRESS,
                           scanningFilterPolicy=HCI_LE_ACCEPT_ALL_ADVERTISING_PACKETS
                         }
2026-02-13 13:30:22,343 | INFO | HCI?HCI_LE_SET_SCAN_PARAMETERS_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,344 | INFO | PASS
2026-02-13 13:30:22,344 | INFO | HCI!HCI_LE_SET_SCAN_ENABLE{
                           leScanEnable=HCI_LE_SCAN_ENABLE,
                           filterDuplicates=HCI_LE_DUPLICATE_FILTERING_DISABLE
                         }
2026-02-13 13:30:22,344 | INFO | HCI?HCI_LE_SET_SCAN_ENABLE_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,344 | INFO | User clicked No or Cancel button.
2026-02-13 13:30:22,345 | INFO | INDCSV
2026-02-13 13:30:22,345 | INFO | HCI!HCI_LE_SET_SCAN_ENABLE{
                           leScanEnable=HCI_LE_SCAN_DISABLE,
                           filterDuplicates=HCI_LE_DUPLICATE_FILTERING_DISABLE
                         }
2026-02-13 13:30:22,345 | INFO | HCI?HCI_LE_SET_SCAN_ENABLE_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,345 | INFO | PTS cannot find any address in advertising reports that matches ixit.
2026-02-13 13:30:22,346 | INFO | Failed to scan advertising packets.
2026-02-13 13:30:22,346 | INFO | HCI!HCI_RESET
2026-02-13 13:30:22,346 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:30:22,346 | INFO | INDCSV
2026-02-13 13:30:22,346 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:30:22,347 | INFO | RESULT: INDCSV
2026-02-13 13:30:22,347 | INFO | A1#NWNlNGFjNTNjNzI2ZGI0MTIwNDcyZmM0MzViNGUxZDcyMzI4Y2VjZmJjMDhjYzQ1NTY3ZGJiOTIzN2U1MjIwYw==#1Qo4bqef1tJgKLSwoJwVNcZ43vtrnCPjcQrQGTmPpuhXwgoiw8O8MUUPeScdvVHa
2026-02-13 13:30:22,347 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:30:22,347 | INFO | RESULT: A1#NWNLNGFJNTNJNZI2ZGI0MTIWNDCYZMM0MZVINGUXZDCYMZI4Y2VJZMJJMDHJYZQ1NTY3ZGJIOTIZN2U1MJIWYW==#1QO4BQEF1TJGKLSWOJWVNCZ43VTRNCPJCQRQGTMPPUHXWGOIW8O8MUUPESCDVVHA
2026-02-13 13:30:22,347 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:30:22,347 | INFO | Resetting DUT between tests
2026-02-13 13:30:22,348 | INFO | PTS test state stopped
2026-02-13 13:30:22,348 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:30:22,348 | INFO | 
2026-02-13 13:30:22,348 | INFO | ==============================
2026-02-13 13:30:22,348 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:30:22,349 | INFO | ==============================
2026-02-13 13:30:22,349 | INFO | GAP/ADV/BV-03-C : A1#NWNLNGFJNTNJNZI2ZGI0MTIWNDCYZMM0MZVINGUXZDCYMZI4Y2VJZMJJMDHJYZQ1NTY3ZGJIOTIZN2U1MJIWYW==#1QO4BQEF1TJGKLSWOJWVNCZ43VTRNCPJCQRQGTMPPUHXWGOIW8O8MUUPESCDVVHA : Failed to scan advertising packets.
2026-02-13 13:30:22,349 | INFO | ------------------------------
2026-02-13 13:30:22,349 | INFO | Total testcases : 1
2026-02-13 13:30:22,349 | INFO | Passed          : 0
2026-02-13 13:30:22,349 | INFO | Failed          : 0
2026-02-13 13:30:22,350 | INFO | ==============================
2026-02-13 13:30:22,422 | INFO | Project execution finished
2026-02-13 13:30:22,422 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

