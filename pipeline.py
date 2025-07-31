import requests
import pandas as pd
import mysql.connector
from datetime import datetime

# 1. Fetch data from API (
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# 2. Transform data (Do yourtransformations here)
def transform_data(raw_data):
    df = pd.DataFrame(raw_data)
    df["pulled_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df["short_title"] = df["title"].str.slice(0, 20)
    return df[["id", "userId", "short_title", "pulled_at"]]

# 3. Load into MySQL
def load_to_mysql(df, db_config):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INT PRIMARY KEY,
            userId INT,
            short_title VARCHAR(255),
            pulled_at DATETIME
        );
    """)

    # Clear table (optional for demo)
    cursor.execute("DELETE FROM posts")

    # Insert rows
    insert_query = """
        INSERT INTO posts (id, userId, short_title, pulled_at)
        VALUES (%s, %s, %s, %s)
    """
    data = df.to_records(index=False)
    cursor.executemany(insert_query, data)

    conn.commit()
    cursor.close()
    conn.close()

def main():
    raw = fetch_data()
    transformed = transform_data(raw)

    # Update this config with your actual DB credentials
    db_config = {
        'host': 'localhost',
        'user': 'your_user',
        'password': 'your_password',
        'database': 'your_database'
    }

    load_to_mysql(transformed, db_config)

if __name__ == "__main__":
    main()
