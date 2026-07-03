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

    if total > 0:
        persentase = (task_selesai / total) * 100
    else:
        persentase = 0

    print("\n===== TASK STATISTICS =====")
    print(f"Total Task          : {total}")
    print(f"Task Selesai        : {task_selesai}")
    print(f"Task Belum Selesai  : {task_belum_selesai}")
    print(f"Persentase Selesai  : {persentase:.2f}%")

    print("\nKesimpulan:")

    if persentase == 100:
        print("Semua tugas sudah selesai.")
    elif persentase >= 70:
        print("Sebagian besar tugas sudah selesai.")
    elif persentase >=40:
        print("Progres tugas sedang berjalan.")
    else:
        print("Masih banyak tugas yang belum selesai.")

    conn.close()