import pytest
import requests
import app_constants

@pytest.mark.post
@pytest.mark.failing
def test_POST_success():
    post_data = {
        "price": 23.89,
        "name": "Nike Shoes",
        "description": "A great pair of trainers!"
    }
    expected_post_response_data = post_data.copy()
    expected_post_response_data["id"] = int(app_constants.nonexistant_ID)
    post_response = requests.post(app_constants.app_url, data=post_data)
    assert post_response.status_code == 200
    assert post_response.json() == expected_post_response_data

@pytest.mark.post
@pytest.mark.failing
def test_POST_negative_price_fail():
    post_data = {
        "price": float("-23.89"),
        "name": "Nike Shoes",
        "description": "A great pair of trainers!"
    }
    post_response = requests.post(app_constants.app_url, data=post_data)
    assert post_response.status_code == 400
