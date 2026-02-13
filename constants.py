#PTS CONSTANTS
pts_address ="00:1B:DC:F2:1F:7B"
pts_file = r"C:\PTS\ICS_20260121-0538205487 - Copy.pts"
workspace_path = r"C:\PTS\Workspaces"
ok_cancel_wids = {
    118: "OK", 169: "OK", 12: "OK",  4: "OK", 135: "OK", 104:"OK", 35:"OK", 14:"OK", 34:"OK", 83:"OK",
}
yes_no_wids = {120: "YES", 157: "Yes",1304: "Yes",1301: "Yes", 1305: "Yes", 121: "YES", 33:"YES", 13:"YES", 165:"YES", 83:"YES", 2004:"YES", 504:"YES"}
action_wids = {51,23,25,222,33,26,30,160,32, 27,29,56,1302,57,149,152,153, 154, 173, 232,243, 59,60,75,76,90, 20115,2004,78, 49,50,164,102, 146, 147, 10,11,13,74, 14, 164,  74,1016,102, 72, 86,36,105,34, 5,20000, 35, 33, 23, 21,  52, 31, 24, 53, 54, 78, 91, 100, 104, 108, 20,  118, 47, 79, 12, 208, 1003, 77, 135, 121, 55}
remote_base_directory = "~/pts-grpc"
remote_log_file = "~/pts-grpc/logfiles/grpc_server.log"
ssh_user = "root"
ssh_options = [
    "-o", "StrictHostKeyChecking=no",
    "-o", "UserKnownHostsFile=/dev/null",
]
MMI_Style_Ok_Cancel1 = 0x11041
MMI_Style_Ok_Cancel2 = 0x11141
MMI_Style_Ok = 0x11040
MMI_Style_Yes_No1 = 0x11044
MMI_Style_Yes_No_Cancel1 = 0x11043
MMI_Style_Abort_Retry1 = 0x11042
MMI_Style_Edit1 = 0x12040
MMI_Style_Edit2 = 0x12140
MMI_STYLE_STRING = {
    MMI_Style_Ok_Cancel1: "MMI_Style_Ok_Cancel1",
    MMI_Style_Ok_Cancel2: "MMI_Style_Ok_Cancel2",
    MMI_Style_Ok: "MMI_Style_Ok",
    MMI_Style_Yes_No1: "MMI_Style_Yes_No1",
    MMI_Style_Yes_No_Cancel1: "MMI_Style_Yes_No_Cancel1",
    MMI_Style_Abort_Retry1: "MMI_Style_Abort_Retry1",
    MMI_Style_Edit1: "MMI_Style_Edit1",
    MMI_Style_Edit2: "MMI_Style_Edit2"
}
PTS_LOGTYPE_START_TEST      = 1
PTS_LOGTYPE_IMPLICIT_SEND   = 3
PTS_LOGTYPE_ERROR          = 5
PTS_LOGTYPE_FINAL_VERDICT  = 8
logtype_whitelist = [
    PTS_LOGTYPE_START_TEST,
    PTS_LOGTYPE_IMPLICIT_SEND,
    PTS_LOGTYPE_ERROR,
    PTS_LOGTYPE_FINAL_VERDICT,
]
REPLACEMENT_STRING = [
    (r"\+.*?ms", ""),
    (r"\|.*?\|", ""),
    (r"C:.*?pts", ""),
    (r"Receive Event", ""),
    (r"Send Event", ""),
]
# hci command ogf/ocf
cmd = {
    "le_set_advertisement_enable": "0x08 0x000a",
    "le_set_advertisement_data": "0x08 0x0008",
    "le_set_advertisement_params": "0x08 0x0006",
    "le_set_random_addr": "0x08 0x0005"
}

# advertising modes
adv_modes = {
    "enable": "01",
    "disable": "00",

    "conn_undirected": "00",
    "nonconn_undirected": "03"
}

# advertising parameters
advertisement_params = {
    "connectable": "a0 00 a0 00 00 00 00 00 00 00 00 07 00"
,
    "connectable_directed": "a0 00 a0 00 01 00 00 7b 1f f2 dc 1b 00 07 00",
    "non_connectable": "a0 00 a0 00 03 00 00 00 00 00 00 00 00 07 00",
    "broadcast": "a0 00 a0 00 03 01 00 00 00 00 00 00 07 00"
}

# advertising payloads
advertisement_data = {
    "pts_general": "02 01 02",
    "pts_limited": "1f 02 01 05 05 03 00 18 01 18 0d 09 50 54 53 2d 47 41 50 2d 30 36 42 38 03 19 00 00",
    "pts_broadcast": "1f 02 01 04 05 03 00 18 01 18 0d 09 50 54 53 2d 47 41 50 2d 30 36 42 38 03 19 00 00",

    "pts_non_discoverable": "02 01 00",

    "service_uuid": "06 02 01 06 03 03 0d 18",
    "local_name": "0f 02 01 06 0b 09 42 6c 75 65 7a 20 35 2e 36 35",
    "flags": "02 01 06"
}


random_address = {
    "nrpa": "3a 91 22 7c 10 45"
}
iut_address="5C:F3:70:60:1D:A1"
advertisement_structures = {

    # Flags
        "flags": [
        "02", "01", "06"
    ],

    # Manufacturer Specific Data (Apple example)
    "manufacturer": [
        "02", "01", "06",  # Flags
        # Length = 1(type) + 2(company) + 2(data) = 5
        "05", "FF",
        "4C", "00",  # Company ID (Apple)
        "AA", "BB"  # Manufacturer payload
    ]
    ,
    # TX Power Level (0 dBm)
    "tx_power": ["02", "0A", "00"],

    # Peripheral Preferred Connection Interval Range
    # 0x0006 – 0x0C80 (7.5ms – 4s)
    "ppci": ["05", "12", "06", "00", "80", "0C"],

    # Service Solicitation (Heart Rate 0x180D)
    "service_solicit": ["03", "14", "0D", "18"],

    # Service Data (Battery Service 0x180F + level 0x01)
    "service_data": ["04", "16", "0F", "18", "01"],

    # Appearance (Generic Computer 0x0080)
    "appearance": ["03", "19", "80", "00"],

    # Public Target Address (PTS address 00:1B:DC:F2:1F:7B)
    # AD type = 0x17
    "public_target": [
        "07", "17",
        "7B", "1F", "F2", "DC", "1B", "00"
    ],

    # Random Target Address
    # AD type = 0x18
    "random_target": [
        "07", "18",
        "45", "10", "7C", "22", "91", "3A"
    ],

    # Advertising Interval
    # AD type = 0x1A
    "adv_interval": [
        "03", "1A",
        "A0", "00"   # 100ms
    ],

    #  Advertising Interval Long
    "adv_interval_long": [
        "05", "2F",
        "A0", "00", "A0", "00"
    ],

    # URI (https://bluetooth.com)
    "uri": [
        "1C", "24",
        "00", "01",
        "68", "74", "74", "70", "73", "3A", "2F", "2F",
        "77", "77", "77", "2E",
        "62", "6C", "75", "65",
        "74", "6F", "6F", "74",
        "68", "2E",
        "63", "6F", "6D"
    ],

    "le_features": [
        "02", "01", "06",  # Flags
        "09", "27",  # Length + AD Type (0x27)
        "01", "00", "00", "00",
        "00", "00", "00", "01"  # Last octet MUST NOT be zero
    ]

}
