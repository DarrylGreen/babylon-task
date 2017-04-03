import pytest
import requests
import app_constants

@pytest.mark.delete
@pytest.mark.failing
def test_DELETE_fail():
    delete_response = requests.delete(
        app_constants.app_url + "/" + app_constants.existing_ID)
    assert delete_response.status_code == 404

@pytest.mark.delete
@pytest.mark.failing
def test_DELETE_nonexistant_ID_fail():
    delete_response = requests.delete(
        app_constants.app_url + "/" + app_constants.nonexistant_ID)
    assert delete_response.status_code == 404
