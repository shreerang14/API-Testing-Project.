import requests
import pytest

# Test data: list of (endpoint, expected_status)
api_test_data = [
    ("https://jsonplaceholder.typicode.com/users", 200),
    ("https://jsonplaceholder.typicode.com/posts", 200),
    ("https://jsonplaceholder.typicode.com/comments", 200),
    ("https://jsonplaceholder.typicode.com/invalidendpoint", 404)  # negative test
]

@pytest.mark.parametrize("url, expected_status", api_test_data)
def test_api_endpoints(url, expected_status):
    response = requests.get(url)
    assert response.status_code == expected_status
