import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Check API returns success
    assert response.status_code == 200

    # Check response is a list
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
