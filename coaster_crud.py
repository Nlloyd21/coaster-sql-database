import subprocess
import os
import sqlite3

DB_FILE = "mini_coasters.db"


def init_database():
    """Creates the database and builds the table structure without preloading rows."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS coasters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        park TEXT NOT NULL,
        speed REAL,
        inversions INTEGER
    )
    """)
    conn.commit()
    conn.close()

def create_coaster():
    """C - CREATE: Adds a new coaster to the table."""
    print("\n--- Add a New Roller Coaster ---")
    name = input("Coaster Name: ")
    park = input("Park Name: ")
    try:
        speed = float(input("Top Speed (mph): "))
        inversions = int(input("Number of Inversions: "))
    except ValueError:
        print("Invalid number format. Coaster not added.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO coasters (name, park, speed, inversions) 
        VALUES (?, ?, ?, ?)
    """, (name, park, speed, inversions))
    conn.commit()
    conn.close()
    print(f"Successfully added '{name}'!")

def read_coasters():
    """R - READ: Displays all coasters currently in the database."""
    print("\n=== Roller Coaster List ===")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, park, speed, inversions FROM coasters")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("The database is currently empty.")
        return

    for row in rows:
        print(f"ID: {row[0]} | {row[1]} ({row[2]}) - Speed: {row[3]}mph, Inversions: {row[4]}")
    print("===========================")

def update_coaster():
    """U - UPDATE: Loads a coaster into memory, allows selective editing, and saves on command."""
    read_coasters()
    try:
        coaster_id = int(input("\nEnter the ID of the coaster you want to update: "))
    except ValueError:
        print("Invalid ID selection.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, park, speed, inversions FROM coasters WHERE id = ?", (coaster_id,))
    current_record = cursor.fetchone()
    
    if not current_record:
        print(f"Coaster ID {coaster_id} not found.")
        conn.close()
        return

    
    working_name = current_record[0]
    working_park = current_record[1]
    working_speed = current_record[2]
    working_inversions = current_record[3]

    while True:
        print(f"\n======================================")
        print(f"Editing Coaster ID: {coaster_id}")
        print(f"1. Name:       {working_name}")
        print(f"2. Park:       {working_park}")
        print(f"3. Top Speed:  {working_speed} mph")
        print(f"4. Inversions: {working_inversions}")
        print(f"5. [SAVE CHANGES TO DATABASE]")
        print(f"6. [CANCEL & DISCARD CHANGES]")
        print(f"======================================")
        
        sub_choice = input("Select what you want to change, or Save/Cancel (1-6): ")

        if sub_choice == '1':
            working_name = input("Enter new Coaster Name: ")
        elif sub_choice == '2':
            working_park = input("Enter new Park Name: ")
        elif sub_choice == '3':
            try:
                working_speed = float(input("Enter new Top Speed (mph): "))
            except ValueError:
                print("Invalid format. Speed unchanged.")
        elif sub_choice == '4':
            try:
                working_inversions = int(input("Enter new Number of Inversions: "))
            except ValueError:
                print("Invalid format. Inversions unchanged.")
        elif sub_choice == '5':
            
            cursor.execute("""
                UPDATE coasters 
                SET name = ?, 
                    park = ?, 
                    speed = ?, 
                    inversions = ? 
                WHERE id = ?
            """, (working_name, working_park, working_speed, working_inversions, coaster_id))
            conn.commit()
            print(f"\nChanges saved successfully to the database for ID {coaster_id}!")
            break
        elif sub_choice == '6':
            print("\nUpdates canceled. No changes were saved.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 6.")

    conn.close()

def delete_coaster():
    """D - DELETE: Removes a coaster from the database by its ID."""
    read_coasters()
    try:
        coaster_id = int(input("\nEnter the ID of the coaster to remove: "))
    except ValueError:
        print("Invalid ID selection.")
        return

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM coasters WHERE id = ?", (coaster_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Successfully removed coaster ID {coaster_id} from the database.")
    else:
        print(f"Coaster ID {coaster_id} not found.")
    conn.close()

def main():
    init_database()
    
    while True:
        print("\n*** Mini Coaster Database Menu ***")
        print("1. View All Coasters (Read)")
        print("2. Add a New Coaster (Create)")
        print("3. Update Coaster Speed (Update)")
        print("4. Remove a Coaster (Delete)")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            read_coasters()
        elif choice == '2':
            create_coaster()
        elif choice == '3':
            update_coaster()
        elif choice == '4':
            delete_coaster()
        elif choice == '5':
            print("\nExiting program. Keep clear of the closing gates!")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()