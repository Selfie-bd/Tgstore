import os

API_ID = int(os.environ.get("API_ID", ))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID","")
IS_PRIVATE = os.environ.get("IS_PRIVATE", True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID","1940030638"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
