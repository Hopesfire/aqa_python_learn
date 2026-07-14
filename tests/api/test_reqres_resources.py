import pytest
import requests

from config import REQRES_API_KEY, REQRES_URL
from models.reqres_models import ReqresResourcesResponse


@pytest.mark.api
@pytest.mark.skipif(
    not REQRES_API_KEY,
    reason="REQRES_API_KEY is not provided"
)
def test_reqres_resources():
    response = requests.get(
        f"{REQRES_URL}/api/unknown",
        headers={"x-api-key": REQRES_API_KEY}
    )

    assert response.status_code == 200

    resources = ReqresResourcesResponse.model_validate(response.json())
    assert resources.data

    for resource in resources.data:
        assert resource.name
        assert resource.year >= 2000
