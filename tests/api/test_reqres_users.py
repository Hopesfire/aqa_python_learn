import pytest
import requests

from config import REQRES_API_KEY, REQRES_URL
from models.reqres_models import ReqresUsersResponse


@pytest.mark.api
@pytest.mark.skipif(not REQRES_API_KEY, reason="REQRES_API_KEY is not provided")
def test_reqres_users():
    response = requests.get(
        f"{REQRES_URL}/api/users?page=2", headers={"x-api-key": REQRES_API_KEY}
    )

    assert response.status_code == 200

    users_response = ReqresUsersResponse.model_validate(response.json())
    assert users_response.data

    assert len(users_response.data) == 6
