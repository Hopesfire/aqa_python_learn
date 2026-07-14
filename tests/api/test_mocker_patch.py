import pytest

from exercises.currency_rates import get_usd_rate


@pytest.mark.api
def test_get_rate_with_mock(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"rates": {"RUB": 125.66}}
    mock_response.raise_for_status.return_value = None

    mocker.patch("exercises.currency_rates.requests.get", return_value=mock_response)

    rate = get_usd_rate("RUB")

    assert rate == 125.66
