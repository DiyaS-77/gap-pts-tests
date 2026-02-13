 runtime release.
  warnings.warn(
2026-02-13 13:27:44,641 | INFO | ==============================
2026-02-13 13:27:44,641 | INFO | gRPC Client Started
2026-02-13 13:27:44,641 | INFO | ==============================
2026-02-13 13:27:44,645 | INFO | Triggering PTS PROJECT via gRPC
2026-02-13 13:27:44,645 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:27:44,658 | INFO | Loaded 1 testcases for GAP
2026-02-13 13:27:44,658 | INFO |  ===== [1/1] Running GAP/ADV/BV-03-C =====
2026-02-13 13:28:03,462 | INFO | Starting project execution: GAP
2026-02-13 13:28:03,463 | INFO | Loading testbed configuration from: config.json
2026-02-13 13:28:03,463 | INFO | Waiting for gRPC server startup 10.91.220.35
2026-02-13 13:28:03,464 | INFO | gRPC server is running 10.91.220.35
2026-02-13 13:28:03,464 | INFO | Opening PTS workspace once
2026-02-13 13:28:03,465 | INFO | Opening existing workspace: C:\PTS\Workspaces\GAP_WS\GAP_WS.pqw6
2026-02-13 13:28:03,465 | INFO | Selecting PTS project once
2026-02-13 13:28:03,466 | INFO | Selecting project: GAP
2026-02-13 13:28:03,466 | INFO | Running test case: GAP/ADV/BV-03-C
2026-02-13 13:28:03,467 | INFO | Registering PTS logger
2026-02-13 13:28:03,467 | INFO | Registering MMI handler
2026-02-13 13:28:03,467 | INFO | Running test case: GAP / GAP/ADV/BV-03-C
2026-02-13 13:28:03,468 | INFO | MMI RECEIVED
2026-02-13 13:28:03,468 | INFO | Project   : GAP
2026-02-13 13:28:03,469 | INFO | WID       : 25
2026-02-13 13:28:03,469 | INFO | Testcase  : GAP/ADV/BV-03-C
2026-02-13 13:28:03,469 | INFO | Desc      : Please prepare IUT to send an advertising report with Flags.
2026-02-13 13:28:03,470 | INFO | Style     : MMI_Style_Ok_Cancel2
2026-02-13 13:28:03,470 | INFO | Resolving handler: handle_wid_25
2026-02-13 13:28:03,470 | INFO | Executing GAP handler for WID 25
2026-02-13 13:28:03,471 | INFO | [gRPC] start_advertising failed: Either advertisement_data_key or advertisement_structure_key must be provided
2026-02-13 13:28:03,471 | INFO | WID 25 completed with result: False
2026-02-13 13:28:03,474 | INFO | MMI action not executed for WID 25
2026-02-13 13:28:03,474 | INFO | MMI response: Cancel
2026-02-13 13:28:03,474 | INFO | Server: SUCCESS with response=Cancel
2026-02-13 13:28:03,474 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,474 | INFO | 
2026-02-13 13:28:03,475 | INFO | Build date: Dec 11 2025, 11:52:49
2026-02-13 13:28:03,475 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:28:03,475 | INFO | HCI!HCI_RESET
2026-02-13 13:28:03,475 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,475 | INFO | PASS
2026-02-13 13:28:03,475 | INFO | HCI!HCI_READ_LOCAL_VERSION_INFORMATION
2026-02-13 13:28:03,475 | INFO | HCI?HCI_READ_LOCAL_VERSION_INFORMATION_COMPLETE_EVENT{
                           status=HCI_OK,
                           hciVersion=0x08,
                           hciRevision=0x30E8,
                           lmpVersion=0x08,
                           manufacturerName=0x000A,
                           lmpSubversion=0x30E8
                         }
2026-02-13 13:28:03,475 | INFO | PASS
2026-02-13 13:28:03,476 | INFO | HCI!HCI_LE_SET_EVENT_MASK{
                           leEventMask=0x000000000000001F
                         }
2026-02-13 13:28:03,476 | INFO | HCI?HCI_LE_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,476 | INFO | HCI!HCI_SET_EVENT_MASK{
                           eventMask=0x3FFFFFFFFFFFFFFF
                         }
2026-02-13 13:28:03,477 | INFO | HCI?HCI_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,477 | INFO | PASS
2026-02-13 13:28:03,478 | INFO | HCI!HCI_READ_LOCAL_SUPPORTED_FEATURES
2026-02-13 13:28:03,478 | INFO | HCI?HCI_READ_LOCAL_SUPPORTED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x875B1FD87E8FFFFF
                         }
2026-02-13 13:28:03,478 | INFO | PASS
2026-02-13 13:28:03,479 | INFO | HCI!HCI_READ_LOCAL_EXTENDED_FEATURES{
                           page_number=0x01
                         }
2026-02-13 13:28:03,479 | INFO | HCI?HCI_READ_LOCAL_EXTENDED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x0000000000000000
                         }
2026-02-13 13:28:03,480 | INFO | PASS
2026-02-13 13:28:03,480 | INFO | HCI!HCI_READ_LOCAL_EXTENDED_FEATURES{
                           page_number=0x02
                         }
2026-02-13 13:28:03,480 | INFO | HCI?HCI_READ_LOCAL_EXTENDED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           lmpFeatures=0x000000000000030F
                         }
2026-02-13 13:28:03,481 | INFO | PASS
2026-02-13 13:28:03,481 | INFO | HCI!HCI_READ_LOCAL_SUPPORTED_COMMANDS
2026-02-13 13:28:03,482 | INFO | HCI?HCI_READ_LOCAL_SUPPORTED_COMMANDS_COMPLETE_EVENT{
                           status=HCI_OK,
                           supported_commands=0x00000000000000000000000000000000000000000000000000000000000030FFFFC0007FFFFFF7610004001CFF83F73FFEE80FF3FFFFFFFFFFFFFFFE03FFFFFF
                         }
2026-02-13 13:28:03,482 | INFO | PASS
2026-02-13 13:28:03,482 | INFO | HCI!HCI_READ_BD_ADDR
2026-02-13 13:28:03,483 | INFO | HCI?HCI_READ_BD_ADDR_COMPLETE_EVENT{
                           status=HCI_OK,
                           bdAddress=0x001BDCF21F7B
                         }
2026-02-13 13:28:03,483 | INFO | PASS
2026-02-13 13:28:03,484 | INFO | HCI!HCI_WRITE_LE_HOST_SUPPORTED{
                           leSupportedHost=HCI_LE_SUPPORTED_HOST_ENABLED,
                           simultaneousLeHost=HCI_SIMULTANEOUS_LE_HOST_ENABLED
                         }
2026-02-13 13:28:03,484 | INFO | HCI?HCI_WRITE_LE_HOST_SUPPORTED_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,484 | INFO | HCI!HCI_LE_LOCAL_SUPPORTED_FEATURES
2026-02-13 13:28:03,485 | INFO | HCI?HCI_LE_READ_LOCAL_SUPPORTED_FEATURES_COMPLETE_EVENT{
                           status=HCI_OK,
                           leFeatures=0x000000000000001F
                         }
2026-02-13 13:28:03,485 | INFO | PASS
2026-02-13 13:28:03,485 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000900010003700000DA00010000000000
                         }
2026-02-13 13:28:03,486 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=19,
                           DATA=C201000900010003700000DA00010000000700
                         }
2026-02-13 13:28:03,486 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000900020003700000DB00010000000000
                         }
2026-02-13 13:28:03,486 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=19,
                           DATA=C201000900020003700000DB00010000001000
                         }
2026-02-13 13:28:03,487 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000C00030003700000EF00040000000000000000000000
                         }
2026-02-13 13:28:03,487 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=25,
                           DATA=C201000C00030003700000EF0004000000FFFF8F7ED81F5B87
                         }
2026-02-13 13:28:03,487 | INFO | HCI!VENDOR_SPECIFIC_COMMAND{
                           OCF=0x0000,
                           DATA=0xC200000C000400037000002301040000000000000000000000
                         }
2026-02-13 13:28:03,488 | INFO | HCI?HCI_VENDOR_SPECIFIC_EVENT{
                           LENGTH=25,
                           DATA=C201000C000400037000002301040000000F03000000000000
                         }
2026-02-13 13:28:03,488 | INFO | PASS
2026-02-13 13:28:03,488 | INFO | HCI!HCI_LE_SET_EVENT_MASK{
                           leEventMask=0x000000000000001F
                         }
2026-02-13 13:28:03,489 | INFO | HCI?HCI_LE_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,489 | INFO | HCI!HCI_SET_EVENT_MASK{
                           eventMask=0x3FFFFFFFFFFFFFFF
                         }
2026-02-13 13:28:03,490 | INFO | HCI?HCI_SET_EVENT_MASK_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,490 | INFO | PASS
2026-02-13 13:28:03,490 | INFO | HCI!HCI_LE_SET_SCAN_PARAMETERS{
                           leScanType=HCI_LE_ACTIVE_SCANNING,
                           leScanInterval=0x001E,
                           leScanWindow=0x001E,
                           ownAddressType=HCI_LE_PUBLIC_DEVICE_ADDRESS,
                           scanningFilterPolicy=HCI_LE_ACCEPT_ALL_ADVERTISING_PACKETS
                         }
2026-02-13 13:28:03,491 | INFO | HCI?HCI_LE_SET_SCAN_PARAMETERS_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,491 | INFO | PASS
2026-02-13 13:28:03,491 | INFO | HCI!HCI_LE_SET_SCAN_ENABLE{
                           leScanEnable=HCI_LE_SCAN_ENABLE,
                           filterDuplicates=HCI_LE_DUPLICATE_FILTERING_DISABLE
                         }
2026-02-13 13:28:03,492 | INFO | HCI?HCI_LE_SET_SCAN_ENABLE_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,492 | INFO | User clicked No or Cancel button.
2026-02-13 13:28:03,492 | INFO | INDCSV
2026-02-13 13:28:03,493 | INFO | HCI!HCI_LE_SET_SCAN_ENABLE{
                           leScanEnable=HCI_LE_SCAN_DISABLE,
                           filterDuplicates=HCI_LE_DUPLICATE_FILTERING_DISABLE
                         }
2026-02-13 13:28:03,493 | INFO | HCI?HCI_LE_SET_SCAN_ENABLE_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,493 | INFO | PTS cannot find any address in advertising reports that matches ixit.
2026-02-13 13:28:03,494 | INFO | Failed to scan advertising packets.
2026-02-13 13:28:03,494 | INFO | HCI!HCI_RESET
2026-02-13 13:28:03,494 | INFO | HCI?HCI_RESET_COMPLETE_EVENT{
                           status=HCI_OK
                         }
2026-02-13 13:28:03,495 | INFO | INDCSV
2026-02-13 13:28:03,495 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:28:03,495 | INFO | RESULT: INDCSV
2026-02-13 13:28:03,495 | INFO | A1#ZGIxM2UyODlhZjgyNmY1YWM2ZmZhNTFjYjMxMWVhZWMyYzRhOTkyNDRiNjViMWMwMWI2OTM0ZTU4Zjg3M2U0ZA==#sOxsH/d+7b61VOAaKswhHgfL1LI9hOhmpg4TVsqJVKp2O/RO0qzQTXqe4VDBGR/U
2026-02-13 13:28:03,496 | INFO | ---- PTS FINAL VERDICT ----
2026-02-13 13:28:03,496 | INFO | RESULT: A1#ZGIXM2UYODLHZJGYNMY1YWM2ZMZHNTFJYJMXMWVHZWMYYZRHOTKYNDRINJVIMWMWMWI2OTM0ZTU4ZJG3M2U0ZA==#SOXSH/D+7B61VOAAKSWHHGFL1LI9HOHMPG4TVSQJVKP2O/RO0QZQTXQE4VDBGR/U
2026-02-13 13:28:03,496 | INFO | GAP/ADV/BV-03-C
2026-02-13 13:28:03,496 | INFO | Resetting DUT between tests
2026-02-13 13:28:03,496 | INFO | PTS test state stopped
2026-02-13 13:28:03,497 | INFO | GAP/ADV/BV-03-C DONE
2026-02-13 13:28:03,497 | INFO | 
2026-02-13 13:28:03,497 | INFO | ==============================
2026-02-13 13:28:03,497 | INFO | PTS EXECUTION SUMMARY
2026-02-13 13:28:03,497 | INFO | ==============================
2026-02-13 13:28:03,497 | INFO | GAP/ADV/BV-03-C : A1#ZGIXM2UYODLHZJGYNMY1YWM2ZMZHNTFJYJMXMWVHZWMYYZRHOTKYNDRINJVIMWMWMWI2OTM0ZTU4ZJG3M2U0ZA==#SOXSH/D+7B61VOAAKSWHHGFL1LI9HOHMPG4TVSQJVKP2O/RO0QZQTXQE4VDBGR/U : Failed to scan advertising packets.
2026-02-13 13:28:03,497 | INFO | ------------------------------
2026-02-13 13:28:03,497 | INFO | Total testcases : 1
2026-02-13 13:28:03,497 | INFO | Passed          : 0
2026-02-13 13:28:03,498 | INFO | Failed          : 0
2026-02-13 13:28:03,498 | INFO | ==============================
2026-02-13 13:28:03,574 | INFO | Project execution finished
2026-02-13 13:28:03,575 | INFO | PTS project execution completed
root@automation04:~/Desktop/pts-multiple-testcase/btble-automation-pts-automation-test_automation/test_automation# 

