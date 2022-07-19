import os

API_ID = int(os.environ.get("API_ID", 2791256))
API_HASH = os.environ.get("API_HASH", "cd2fb4cdc795334aee3fbbc83da463ce")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID","-1001720660922")
IS_PRIVATE = os.environ.get("IS_PRIVATE", True) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID","1916694742"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001576695301')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "1940030638").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
