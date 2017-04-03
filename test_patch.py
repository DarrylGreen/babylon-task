import pytest
import requests
import app_constants

@pytest.mark.patch
@pytest.mark.failing
def test_PATCH_success():
    patch_data = {
        "price": 25.00,
        "name": "Different Nike Shoes",
        "description": "A great pair of trainers!"
    }
    expected_patch_response_data = patch_data.copy()
    expected_patch_response_data["id"] = int(app_constants.existing_ID)
    patch_response = requests.patch(
        app_constants.app_url + "/" + app_constants.existing_ID,
        data=patch_data
    )
    assert patch_response.status_code == 200
    assert patch_response.json() == expected_patch_response_data

@pytest.mark.patch
@pytest.mark.failing
def test_PATCH_incorrect_ID_fail():
    patch_data = {
        "price": 25.00,
        "name": "Different Nike Shoes",
        "description": "A great pair of trainers!",
        "id": int(app_constants.nonexistant_ID)
    }
    patch_response = requests.patch(
        app_constants.app_url + "/" + app_constants.existing_ID,
        data=patch_data
    )
    assert patch_response.status_code == 404

@pytest.mark.patch
@pytest.mark.passing
def test_PATCH_nonexistant_ID_fail():
    patch_data = {
        "price": 25.00,
        "name": "Different Nike Shoes",
        "description": "A great pair of trainers!"
    }
    patch_response = requests.patch(
        app_constants.app_url + "/" + app_constants.nonexistant_ID,
        data=patch_data
    )
    assert patch_response.status_code == 404

@pytest.mark.patch
@pytest.mark.passing
def test_PATCH_negative_price_fail():
    patch_data = {
        "price": float("-23.89"),
        "name": "Nike Shoes",
        "description": "A great pair of trainers!"
    }
    patch_response = requests.patch(
        app_constants.app_url + "/" + app_constants.existing_ID,
        data=patch_data
    )
    assert patch_response.status_code == 400
