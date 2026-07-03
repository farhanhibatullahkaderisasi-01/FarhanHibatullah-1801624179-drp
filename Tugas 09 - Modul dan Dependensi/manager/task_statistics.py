import sqlite3 

def task_statistics():

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM task")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status = 'Selesai'
    """)
    task_selesai = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status = 'Belum Selesai'
    """)
    task_belum_selesai = cursor.fetchone()[0]

    conn.close()