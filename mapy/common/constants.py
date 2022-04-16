HOST_IP = "127.0.0.1"
SERVER_ADDRESS = bytes([127, 0, 0, 1])
CENTER_PORT = 8383
LOGIN_PORT = 8484
GAME_PORT = 8585
# if there are 20 worlds with 20 channels they will collide with 8787, future thought
SHOP_PORT = 8787

USE_DATABASE = False
# DB_HOST = ""
# DB_PASS = ""
# DSN = "postgres://user:password@host:port/database"

USE_HTTP_API = False
HTTP_API_ROUTE = "http://127.0.0.1:54545"

WORLD_COUNT = 1
CHANNEL_COUNT = 4

VERSION = 112
SUB_VERSION = "4"
LOCALE = 7

# VERSION = 95
# SUB_VERSION = "1"
# LOCALE = 8

EXP_RATE = 1
QUEST_EXP = 1
PARTY_QUEST_EXP = 1
MESO_RATE = 1
DROP_RATE = 1

LOG_PACKETS = True

AUTO_LOGIN = False
AUTO_REGISTER = True
REQUEST_PIN = False
REQUEST_PIC = False
REQUIRE_STAFF_IP = False
MAX_CHARACTERS = 3

DEFAULT_EVENT_MESSAGE = "Wow amazing world choose this one"
DEFAULT_TICKER = "Welcome"
ALLOW_MULTI_LEVELING = False
DEFAULT_CREATION_SLOTS = 3
DISABLE_CHARACTER_CREATION = True

PERMANENT = 150841440000000000

ANTIREPEAT_BUFFS = [
    11101004,
    5221000,
    11001001,
    5211007,
    5121000,
    5121007,
    5111007,
    4341000,
    5111007,
    4121000,
    4201003,
    2121000,
    1221000,
    1201006,
    1211008,
    1211009,
    1211010,
    1121000,
    1001003,
    1101006,
    1111007,
    2101001,
    2101003,
    1321000,
    1311007,
    1311006,
]

EVENT_VEHICLE_SKILLS = [
    1025,
    1027,
    1028,
    1029,
    1030,
    1031,
    1033,
    1034,
    1035,
    1036,
    1037,
    1038,
    1039,
    1040,
    1042,
    1044,
    1049,
    1050,
    1051,
    1052,
    1053,
    1054,
    1063,
    1064,
    1065,
    1069,
    1070,
    1071,
]


def is_event_vehicle_skill(skill_id):
    return skill_id % 10000 in EVENT_VEHICLE_SKILLS


def get_job_from_creation(job_id):
    return {0: 3000, 1: 0, 2: 1000, 3: 2000, 4: 2001}.get(job_id, 0)


def is_extend_sp_job(job_id):
    return job_id / 1000 == 3 or job_id / 100 == 22 or job_id == 2001
