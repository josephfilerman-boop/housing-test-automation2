import os
import sqlite3
import db_manager  # Importing your script from Wednesday
import data_seeder # Importing your script from Thursday

DB_NAME = 'housing.db'

def clean_slate():
    """
    Step 1: Destroy the old world.
    Deletes the database file if it exists so we start FRESH.
    """
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"--- 🗑️  Deleted old {DB_NAME} ---")
    else:
        print(f"--- New setup: No existing {DB_NAME} found ---")

def verify_data():
    """
    Step 4: Trust but Verify.
    Queries the DB to ensure setup was successful.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM SERVICE_MEMBERS")
    count = cursor.fetchone()[0]
    conn.close()
    
    print(f"--- ✅ VERIFICATION: Found {count} soldiers in database. ---")
    
    if count == 3:
        print("--- 🚀 READY FOR TESTING ---")
    else:
        print("--- ❌ ERROR: Data mismatch! ---")

def main():
    print("Starting Test Environment Setup...")
    
    # 1. Delete old DB
    clean_slate()
    
    # 2. Create Schema (Wednesday's work)
    print("Building Schema...")
    db_manager.create_schema()
    
    # 3. Seed Data (Thursday's work)
    print("Seeding Data...")
    data_seeder.seed_data()
    
    # 4. Check results
    verify_data()

if __name__ == "__main__":
    main()