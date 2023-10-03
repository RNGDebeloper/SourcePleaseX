from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = getenv(" ")
API_HASH = getenv(" ")
BOT_TOKEN = getenv(" ")

MONGO_DB_URI = getenv(" ")

INDEX_ID = int(getenv(" "))
UPLOADS_ID = int(getenv(" "))

STATUS_ID = int(getenv(" "))
SCHEDULE_ID = int(getenv(" "))

CHANNEL_TITLE = getenv(" ")
INDEX_USERNAME = getenv(" ")
UPLOADS_USERNAME = getenv(" ")
