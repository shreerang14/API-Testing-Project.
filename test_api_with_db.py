import requests
import sqlite3

def test_store_users_in_db():
    # Step 1: Call API
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200
    users = response.json()

    # Step 2: Connect to SQLite database (creates file if not exists)
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Step 3: Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT,
            email TEXT
        )
    """)

    # Step 4: Insert API data into table
    for user in users:
        cursor.execute("""
            INSERT OR REPLACE INTO users (id, name, username, email)
            VALUES (?, ?, ?, ?)
        """, (user["id"], user["name"], user["username"], user["email"]))

    conn.commit()

    # Step 5: Validate with SQL query
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    assert count > 0  # ✅ make sure data saved

    conn.close()
