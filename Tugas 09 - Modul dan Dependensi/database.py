import sqlite3

def create_database():
    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    # USER
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
        nama_user TEXT
    )
    """)
    
    # PRIORITY
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS priority(
        id_priority INTEGER PRIMARY KEY AUTOINCREMENT,
        kategori TEXT
    )
    """)

    # TASK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task(
        id_task INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_task TEXT,
        deadline TEXT,
        status TEXT,
        id_user INTEGER,
        id_priority INTEGER
    )
    """)

    # PROGRESS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress(
        id_progress INTEGER PRIMARY KEY AUTOINCREMENT,
        presentase INTEGER
    )
    """)

    # REMINDER
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminder(
        id_reminder INTEGER PRIMARY KEY AUTOINCREMENT,
        pesan TEXT,
        id_task INTEGER
    )
    """)

    conn.commit()
    conn.close()

create_database()

print("Database berhasil dibuat!")
