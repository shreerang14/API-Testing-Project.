import requests
import pytest
import json

# Load test data from JSON file
def load_test_data():
    with open("api_test_data.json", "r") as f:
        return json.load(f)

# Parameterize tests using data from JSON
@pytest.mark.parametrize("test_case", load_test_data())
def test_api_endpoints(test_case):
    url = test_case["url"]
    expected_status = test_case["expected_status"]

    response = requests.get(url)

    # Validate status code
    assert response.status_code == expected_status
