from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("23267035"))
API_HASH = getenv("a516af48bca80b9f339980650126149c")
BOT_TOKEN = getenv("6541399786:AAFa17jHfX4IYECp5cTFsR945skTs8bZ_9Y")

MONGO_DB_URI = getenv("mongodb+srv://animebot:animesdkbot@cluster0.cybneuo.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001897930752"))
UPLOADS_ID = int(getenv("-1001835485195"))

STATUS_ID = int(getenv("-1001605018135"))
SCHEDULE_ID = int(getenv("-1001519241462"))

CHANNEL_TITLE = getenv("Anime Hindi Dubbed")
INDEX_USERNAME = getenv("anime_hindi_dubbed_by_moviesme")
UPLOADS_USERNAME = getenv("anime_hubxs")
