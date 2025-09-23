import requests

def test_users_payload_structure():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # ✅ Check response status
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    # ✅ Check fields for first user
    user = data[0]
    expected_fields = ["id", "name", "username", "email"]

    for field in expected_fields:
        assert field in user, f"Missing field: {field}"

    # ✅ Check field types
    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["username"], str)
    assert "@" in user["email"]  # simple email check
