import pytest
import requests
import app_constants

@pytest.mark.get
@pytest.mark.passing
def test_GET_success():
    expected_response = {
        "price": 23.89,
        "description": "The Nike LunarEpic Low Flyknit Running Shoe is "
                       "lightweight and breathable with targeted cushioning "
                       "for a soft, effortless sensation underfoot.",
        "name": "Nike Shoes",
        "id": int(app_constants.existing_ID)
    }
    get_response = requests.get(
        app_constants.app_url + "/" + app_constants.existing_ID)
    assert get_response.status_code == 200
    assert get_response.json() == expected_response

@pytest.mark.failing
@pytest.mark.get
def test_GET_fail():
    get_response = requests.get(
        app_constants.app_url + "/" + app_constants.nonexistant_ID)
    assert get_response.status_code == 404
