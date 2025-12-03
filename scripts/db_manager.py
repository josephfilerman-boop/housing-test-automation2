import sqlite3

# BEST PRACTICE: Use a function to handle DB operations
def create_schema():
    """
    Initializes the local SQLite database with the Service Member table.
    This mimics the Navy's Oracle 'MILITARY_HOUSING' schema.
    """
    try:
        # 1. Connect to database (creates file if not exists)
        # In a real job, this would be an Oracle connection string.
        conn = sqlite3.connect('housing.db')
        cursor = conn.cursor()

        # 2. Write the SQL (Structured Query Language)
        # BEST PRACTICE: Use 'IF NOT EXISTS' so the script doesn't crash if run twice.
        create_table_query = """
        CREATE TABLE IF NOT EXISTS SERVICE_MEMBERS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            rank TEXT NOT NULL,
            pay_grade TEXT,
            duty_station TEXT,
            housing_allowance REAL,
            has_dependents BOOLEAN
        );
        """

        # 3. Execute the SQL
        cursor.execute(create_table_query)
        print("SUCCESS: Table 'SERVICE_MEMBERS' created successfully.")

        # 4. Commit (Save) changes and close
        conn.commit()
        conn.close()

    except sqlite3.Error as e:
        print(f"ERROR: Database failure: {e}")

if __name__ == "__main__":
    create_schema()
    