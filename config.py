import os

from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()

USERNAME = os.getenv("GH_USER")
PASSWORD = os.getenv("GH_PASS")
REQRES_URL = "https://reqres.in"
REQRES_API_KEY = os.getenv("REQRES_API_KEY")
REQRES_EMAIL = os.getenv("REQRES_EMAIL")
REQRES_PASSWORD = os.getenv("REQRES_PASSWORD")
