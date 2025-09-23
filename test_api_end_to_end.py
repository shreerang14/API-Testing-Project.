import requests
import sqlite3

def test_end_to_end_users_api():
    # Step 1: Call API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    # Step 2: Validate payload structure for first user
    user = users[0]
    expected_fields = ["id", "name", "username", "email"]
    for field in expected_fields:
        assert field in user, f"Missing field: {field}"

    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["username"], str)
    assert "@" in user["email"]

    # Step 3: Save data into SQLite DB
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT
        )
    """)

    for u in users:
        cursor.execute("""
            INSERT OR REPLACE INTO users (id, name, username, email)
            VALUES (?, ?, ?, ?)
        """, (u["id"], u["name"], u["username"], u["email"]))

    conn.commit()

    # Step 4: SQL Validation
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    assert count == len(users), "Database row count does not match API data count"

    cursor.execute("SELECT email FROM users WHERE id=1")
    email = cursor.fetchone()[0]
    assert "@" in email, "Email in DB not valid"

    conn.close()
