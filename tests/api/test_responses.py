import pytest
import responses

from config import CURRENCY_API_URL
from exercises.currency_rates import get_usd_rate


@pytest.mark.api
@responses.activate
def test_get_rate_with_responses():
    responses.add(
        responses.GET, CURRENCY_API_URL, json={"rates": {"EUR": 10.83}}, status=200
    )

    rate = get_usd_rate("EUR")

    assert rate == 10.83
