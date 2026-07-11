import pytest
import requests

from config import REQRES_API_KEY, REQRES_URL, REQRES_LOGIN, REQRES_PASSWORD


@pytest.mark.api
def test_reqres_users():
    response = requests.post(
        f"{REQRES_URL}/api/login",
        headers={"x-api-key": REQRES_API_KEY},
        json={"email": REQRES_LOGIN, "password": REQRES_PASSWORD},
    )

    assert response.status_code == 200

    login_response_json = response.json()
    assert login_response_json["token"]
