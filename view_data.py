import sqlite3

DB_PATH = "data/registrations.db"

def view_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrations")
    rows = cursor.fetchall()
    conn.close()

    if rows:
        print("Registered Users:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
    else:
        print("No registrations found.")

if __name__ == "__main__":
    view_data()
