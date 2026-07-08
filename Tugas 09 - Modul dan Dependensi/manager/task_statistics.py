import sqlite3 

def task_statistics():

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM task")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE LOWER(TRIM(status)) = 'belum selesai'
    """)
    task_belum_selesai = cursor.fetchone()[0]

    print(f"Task belum selesai: {task_belum_selesai}") 

    print("\n🟤🟤🟤 TASK STATISTICS 🟤🟤🟤")
    print(f"Total Task          : {total}")

    print("\nKesimpulan:")

    if task_belum_selesai == 0:
        print("✅ Semua tugas sudah selesai")
    else:
        print(f"Masih ada {task_belum_selesai} tugas yang belum selesai‼️")

    conn.close()