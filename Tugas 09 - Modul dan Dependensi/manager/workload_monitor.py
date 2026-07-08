import sqlite3

def workload_monitor():

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM task")
    total = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status = 'selesai'
    """)
    selesai = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status = 'Belum selesai'
    """)
    belum = cursor.fetchone()[0]

    if total > 0:
        persentase = (selesai / total) * 100
    else:
        persentase = 0

    print("\n🟤🟤🟤 WORKLOAD MONITOR 🟤🟤🟤")
    print(f"Total Task              : {total}")
    print(f"Task Selesai            : {selesai}")
    print(f"Task Belum Selesai      : {belum}")
    print(f"Progress Penyelesaian   : {persentase:.2f}%")

    print("\nStatus Beban Kerja:")

    if belum == 0:
        print("🎐Semua tugas sudah selesai!")
    elif belum <= 3:
        print("🟩 Beban kerja masih ringan. ")
    elif belum <= 5:
        print("🟨 Beban kerja sedang. ")
    else:
        print("🟥 Beban kerja tinggi, segera selesaikan tugas!")

    conn.close()