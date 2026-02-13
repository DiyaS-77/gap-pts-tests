adv_structures = {

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
