import sqlite3

def seed_data():
    """
    Inserts dummy soldiers into the database for testing purposes.
    """
    # 1. The Data (List of Dictionaries)
    # In the real job, this might come from a CSV or Excel file.
    soldiers = [
        {"last": "Miller", "rank": "E-5", "pay": "E05", "station": "Norfolk", "allowance": 1800.50, "deps": True},
        {"last": "Johnson", "rank": "O-3", "pay": "O03", "station": "San Diego", "allowance": 2400.00, "deps": False},
        {"last": "Smith", "rank": "E-3", "pay": "E03", "station": "Okinawa", "allowance": 1200.75, "deps": False},
    ]

    try:
        # 2. Connect
        conn = sqlite3.connect('housing.db')
        cursor = conn.cursor()

        # 3. The Query (Parameterized)
        # CRITICAL: We use '?' placeholders. NEVER format strings directly (prevents SQL Injection).
        insert_query = """
        INSERT INTO SERVICE_MEMBERS 
        (last_name, rank, pay_grade, duty_station, housing_allowance, has_dependents)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # 4. The Loop (Transforming Data)
        # We assume the user needs to know how to iterate through data.
        count = 0
        for soldier in soldiers:
            # We convert the dictionary values into a tuple for SQLite
            data_tuple = (
                soldier["last"],
                soldier["rank"],
                soldier["pay"],
                soldier["station"],
                soldier["allowance"],
                soldier["deps"]
            )
            cursor.execute(insert_query, data_tuple)
            count += 1

        conn.commit()
        print(f"SUCCESS: Inserted {count} soldiers into the database.")
        conn.close()

    except sqlite3.Error as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    seed_data()