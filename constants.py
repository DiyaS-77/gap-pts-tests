adapter_interface = 'org.bluez.Adapter1'
agent_path = '/test/agent'
agent = "org.bluez.Agent1"
agent_interface = 'org.bluez.AgentManager1'
bluez_service = 'org.bluez'
bluez_path = '/org/bluez'
device_interface = "org.bluez.Device1"
properties_interface = "org.freedesktop.DBus.Properties"
pulseaudio_command = '/usr/local/bluez/pulseaudio-13.0_for_bluez-5.65/bin/pulseaudio -vvv'
media_control_interface = "org.bluez.MediaControl1"
media_player_interface = "org.bluez.MediaPlayer1"
media_transport_interface = "org.bluez.MediaTransport1"
obex_client = "org.bluez.obex.Client1"
obex_path = "/org/bluez/obex"
obex_service = "org.bluez.obex"
obex_object_push = "org.bluez.obex.ObjectPush1"
obex_object_transfer = "org.bluez.obex.Transfer1"
obex_pbap_interface = "org.bluez.obex.PhonebookAccess1"
object_manager_interface = "org.freedesktop.DBus.ObjectManager"
ofono_bus = "org.ofono"
ofono_manager = "org.ofono.Manager"

profile_uuids = {
    "A2DP Sink": "0000110b-0000-1000-8000-00805f9b34fb",
    "A2DP Source": "0000110a-0000-1000-8000-00805f9b34fb",
    "OPP": "00001105-0000-1000-8000-00805f9b34fb",
    "PBAP": "0000112f-0000-1000-8000-00805f9b34fb",
    "HFP AG": "0000111f-0000-1000-8000-00805f9b34fb",
    "HFP HF": "0000111e-0000-1000-8000-00805f9b34fb"

}

device_action_map = {
    "pair": ["pair", "add_paired_device_to_list"],
    "connect": ["handle_connect", "load_device_profile_tabs"],
    "disconnect": ["handle_disconnect", "load_device_profile_tabs"],
    "unpair": ["unpair_device", "remove_device_from_list"]
}

#Maps pairing requests to corresponding request types and handler function names.
#The first element is the pairing request type and the second element is the handler function name.
pairing_request_handlers = {
    "pin": "handle_pin_request",
    "passkey": "handle_passkey_request",
    "confirm": "handle_confirm_request",
    "authorize": "handle_authorize_request",
    "display_pin": "handle_display_pin_request",
    "display_passkey": "handle_display_passkey_request",
    "cancel": "handle_cancel_request",
}

profile_widget_map = {
    'all': 'all_profiles',
    'a2dp': 'a2dp_checkbox',
    'opp': 'opp_checkbox',
    'pbap': 'pbap_checkbox',
    'hfp': 'hfp_checkbox'
}
location = {'internal': 'int', 'sim1': 'sim1', 'sim2': 'sim2'}

phonebook_types = {
    "phonebook": "pb",
    "received_call_logs": "ich",
    "dialed_call_logs": "och",
    "missed_call_logs": "mch",
    "combined_call_logs": "cch",
    "speed_dial": "spd",
    "favorites": "fav"
}

# LE
client_characteristic_config_uuid = '00002902-0000-1000-8000-00805f9b34fb'
gatt_characteristic_interface = 'org.bluez.GattCharacteristic1'
gatt_service_interface = 'org.bluez.GattService1'
gatt_descriptor_interface = 'org.bluez.GattDescriptor1'
le_advertisement_interface = 'org.bluez.LEAdvertisement1'
le_advertising_manager_interface = 'org.bluez.LEAdvertisingManager1'
advertisement_path = '/org/bluez/example/advertisement'
service_path = '/org/test/gatt/service'
gatt_application_path = '/org/test/gatt/application'
gatt_manager_interface = 'org.bluez.GattManager1'


# Battery Service
battery_service_uuid = "0000180f-0000-1000-8000-00805f9b34fb"
battery_level_uuid = "00002a19-0000-1000-8000-00805f9b34fb"
battery_status_level_uuid = "00002a1b-0000-1000-8000-00805f9b34fb"

status_map = {0: 'Unknown', 1: "Good", 2: "Low", 3: "Critical"}

level_map = {0x00: "No Alert", 0x01: "Mild Alert", 0x02: "High Alert"}

# Find me
findme_service_uuid = "00001802-0000-1000-8000-00805f9b34fb"
immediate_alert_uuid = "00002a06-0000-1000-8000-00805f9b34fb"

# Custom Scan Parameter uuids
scan_parameters_service_uuid = "12345678-1234-5678-1234-56789abcdef0"
scan_interval_window_uuid = "12345678-1234-5678-1234-56789abcdef1"
scan_refresh_uuid = "12345678-1234-5678-1234-56789abcdef2"

# Health Thermometer
health_thermometer_service_uuid = "00001809-0000-1000-8000-00805f9b34fb"
temperature_measurement_uuid = "00002a1c-0000-1000-8000-00805f9b34fb"
intermediate_temperature_uuid = "00002a1e-0000-1000-8000-00805f9b34fb"
temperature_type_uuid = "00002a1d-0000-1000-8000-00805f9b34fb"
measurement_interval_uuid = "00002a21-0000-1000-8000-00805f9b34fb"
health_thermometer_descriptor_uuid = '00002901-0000-1000-8000-00805f9b34fb'

temperature_type_map = {
    1: "Armpit",
    2: "Body",
    3: "Ear",
    4: "Finger",
    5: "GI Tract",
    6: "Mouth",
    7: "Rectum",
    8: "Toe",
    9: "Tympanum"
}

# Phone Alert Status
phone_alert_service_uuid = "0000180e-0000-1000-8000-00805f9b34fb"
alert_status_uuid = "00002a3f-0000-1000-8000-00805f9b34fb"
ringer_control_point_uuid = "00002a40-0000-1000-8000-00805f9b34fb"
ringer_setting_uuid = "00002a41-0000-1000-8000-00805f9b34fb"

command_map = {1: "Silent Mode", 2: "Mute Once", 3: "Cancel Silent Mode"}

ringer_setting_map = {
    0: "Normal",
    1: "Silent"
}

alert_status_map = {
    0b000: "None",
    0b001: "Ringer Active",
    0b010: "Vibrate Active",
    0b011: "Ringer + Vibrate",
    0b100: "Display Alert"
}

# Heart Rate
heart_rate_service_uuid = "0000180d-0000-1000-8000-00805f9b34fb"
heart_rate_measurement_uuid = "00002a37-0000-1000-8000-00805f9b34fb"
body_sensor_location_uuid = "00002a38-0000-1000-8000-00805f9b34fb"
heart_rate_control_point_uuid = "00002a39-0000-1000-8000-00805f9b34fb"

location_map = {
    0: "Other",
    1: "Chest",
    2: "Wrist",
    3: "Finger",
    4: "Hand",
    5: "Ear Lobe",
    6: "Foot",
}

# Alert Notification Service
alert_notification_service_uuid = '00001811-0000-1000-8000-00805f9b34fb'
supported_new_alert_category_uuid = '00002A47-0000-1000-8000-00805f9b34fb'
new_alert_uuid = '00002A46-0000-1000-8000-00805f9b34fb'
supported_unread_alert_category_uuid = '00002A48-0000-1000-8000-00805f9b34fb'
unread_alert_status_uuid = '00002A45-0000-1000-8000-00805f9b34fb'

#Blood Pressure
blood_pressure_service_uuid = "00001810-0000-1000-8000-00805f9b34fb"
blood_pressure_measurement_uuid = "00002a35-0000-1000-8000-00805f9b34fb"
blood_pressure_feature_uuid = "00002a49-0000-1000-8000-00805f9b34fb"

# HID Service
hid_service_uuid = "00001812-0000-1000-8000-00805f9b34fb"
hid_information_uuid = "00002a4a-0000-1000-8000-00805f9b34fb"
hid_report_map_uuid = "00002a4b-0000-1000-8000-00805f9b34fb"
hid_control_point_uuid = "00002a4c-0000-1000-8000-00805f9b34fb"
hid_protocol_mode_uuid = "00002a4e-0000-1000-8000-00805f9b34fb"
hid_report_uuid = "00002a4d-0000-1000-8000-00805f9b34fb"

# Glucose Service
glucose_service_uuid = "00001808-0000-1000-8000-00805f9b34fb"
glucose_measurement_uuid = "00002a18-0000-1000-8000-00805f9b34fb"
glucose_feature_uuid = "00002a51-0000-1000-8000-00805f9b34fb"
record_access_control_point_uuid = "00002a52-0000-1000-8000-00805f9b34fb"

racp_commands = {
    1: bytes([0x01, 0x01]),
    2: bytes([0x02, 0x01]),
    3: bytes([0x03, 0x00])
}

opcode_report_stored_records = 1
opcode_delete_stored_records = 2
opcode_abort_operation = 3
opcode_report_num_records = 4
opcode_response_code = 6
operator_all_records = 1
result_success = 1
result_opcode_not_supported = 2
result_invalid_operator = 3
operator_null = 0

# Proximity
link_loss_service_uuid = "00001803-0000-1000-8000-00805f9b34fb"
alert_level_uuid = "00002a06-0000-1000-8000-00805f9b34fb"

# Dictionaries for UI mapping
service_names = {
    battery_service_uuid: "Battery Service",
    scan_parameters_service_uuid: "Scan Parameter Service",
    findme_service_uuid: "Find Me Service",
    health_thermometer_service_uuid: "Health Thermometer Service",
    phone_alert_service_uuid: "Phone Alert Service",
    heart_rate_service_uuid: "Heart Rate Service",
    alert_notification_service_uuid: "Alert Notification Service",
    blood_pressure_service_uuid: "Blood Pressure Service",
    hid_service_uuid: "HID Service",
    glucose_service_uuid: "Glucose Service",
    link_loss_service_uuid: "Link Loss Service"
}


characteristic_names = {
    battery_level_uuid: "Battery Level",
    battery_status_level_uuid: "Battery Status",
    scan_interval_window_uuid: "Scan Interval Window",
    scan_refresh_uuid: "Scan Refresh",
    immediate_alert_uuid: "Immediate Alert",
    temperature_measurement_uuid: "Temperature Measurement",
    intermediate_temperature_uuid: "Intermediate Temperature",
    temperature_type_uuid: "Temperature Type",
    measurement_interval_uuid: "Measurement Interval",
    alert_status_uuid: "Alert Status",
    ringer_control_point_uuid: "Ringer Control Point",
    ringer_setting_uuid: "Ringer Setting",
    heart_rate_measurement_uuid: "Heart Rate Measurement",
    body_sensor_location_uuid: "Body Sensor Location",
    heart_rate_control_point_uuid: "Heart Rate Control Point",
    supported_new_alert_category_uuid: "Supported New Alert Category",
    new_alert_uuid: "New Alert",
    supported_unread_alert_category_uuid: "Supported Unread Alert Category",
    unread_alert_status_uuid: "Unread Alert Status",
    blood_pressure_measurement_uuid: "Blood Pressure Measurement",
    blood_pressure_feature_uuid: "Blood Pressure Feature",
    hid_information_uuid: "HID Information",
    hid_report_map_uuid: "HID Report Map",
    hid_control_point_uuid: "HID Control Point",
    hid_protocol_mode_uuid: "HID Protocol Mode",
    hid_report_uuid: "HID Report",
    glucose_measurement_uuid: "Glucose Measurement",
    glucose_feature_uuid: "Glucose Feature",
    record_access_control_point_uuid: "Record Access Control Point",
    alert_level_uuid: "alert level"
}


report_map = [
    # Keyboard
    0x05, 0x01,
    0x09, 0x06,
    0xA1, 0x01,
    0x05, 0x07,
    0x19, 0xE0,
    0x29, 0xE7,
    0x15, 0x00,
    0x25, 0x01,
    0x75, 0x01,
    0x95, 0x08,
    0x81, 0x02,
    0x75, 0x08,
    0x95, 0x01,
    0x81, 0x01,
    0x05, 0x07,
    0x19, 0x00,
    0x29, 0x65,
    0x15, 0x00,
    0x25, 0x65,
    0x75, 0x08,
    0x95, 0x06,
    0x81, 0x00,
    0xC0,

    # Mouse
    0x05, 0x01,
    0x09, 0x02,
    0xA1, 0x01,
    0x09, 0x01,
    0xA1, 0x00,

    # Buttons
    0x05, 0x09,
    0x29, 0x03,
    0x15, 0x00,
    0x25, 0x01,
    0x75, 0x01,
    0x95, 0x03,
    0x81, 0x02,

    0x75, 0x05,
    0x95, 0x01,
    0x81, 0x01,
    0x05, 0x01,
    0x09, 0x30,
    0x09, 0x31,
    0x09, 0x38,
    0x15, 0x81,
    0x25, 0x7F,
    0x75, 0x08,
    0x95, 0x03,
    0x81, 0x06,

    0xC0,
    0xC0
]


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
