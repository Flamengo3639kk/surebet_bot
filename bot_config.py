import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPORTS_GAME_ODDS_API_KEY = os.getenv("SPORTS_GAME_ODDS_API_KEY")
CHAT_ID = os.getenv("CHAT_ID")