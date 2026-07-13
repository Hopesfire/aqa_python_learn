import os

from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("GH_USER")
PASSWORD = os.getenv("GH_PASS")
REQRES_URL = "https://reqres.in"
REQRES_API_KEY = os.getenv("REQRES_API_KEY")