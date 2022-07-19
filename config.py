import os

API_ID = int(os.environ.get("API_ID", 2791256))
API_HASH = os.environ.get("API_HASH", "cd2fb4cdc795334aee3fbbc83da463ce")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5006643023:AAFuiTBrxHQWRNAO6i-XKCe0mQ4zlg6RtDM")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID","-1001797004270")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID","1916694742"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
