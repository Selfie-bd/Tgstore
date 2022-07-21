import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyromod import listen
from pyrogram import Client
from config import *

def main():
    plugins = dict(root="plugins")
    app = Client("FileStore",
                 bot_token=BOT_TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)

    app.run()

async def get_shortlink(link, x):
    url = f'https://shorte.st/api'
    params = {'api': API_KEY,
              'url': link,
              'alias': x
              }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
            data = await response.json()
            print(data["status"])
            if data["status"] == "success":
                return f"<code>{data['shortenedUrl']}</code>\n\nHere is your Link:\n{data['shortenedUrl']}"
            else:
                return f"Error: {data['message']}"

if __name__ == "__main__":
    main()
