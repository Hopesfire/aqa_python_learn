import pytest
import requests

from config import REQRES_API_KEY, REQRES_EMAIL, REQRES_PASSWORD, REQRES_URL


@pytest.mark.api
@pytest.mark.skipif(
    not all([REQRES_API_KEY, REQRES_EMAIL, REQRES_PASSWORD]),
    reason="Reqres credentials are not provided"
)
def test_reqres_login():
    response = requests.post(
        f"{REQRES_URL}/api/login",
        headers={"x-api-key": REQRES_API_KEY},
        json={"email": REQRES_EMAIL, "password": REQRES_PASSWORD},
    )

    assert response.status_code == 200

    login_response_json = response.json()
    assert login_response_json["token"]
