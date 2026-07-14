import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("GH_USER")
PASSWORD = os.getenv("GH_PASS")
CURRENCY_API_URL = "https://api.fxratesapi.com/latest"