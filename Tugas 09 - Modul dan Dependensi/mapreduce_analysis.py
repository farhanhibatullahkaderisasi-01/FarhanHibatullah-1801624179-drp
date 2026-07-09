import sqlite3   
from functools import reduce

def mapreduce_analysis():

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
             task.nama_task,
             priority.kategori,
             task.status
        FROM task
        JOIN priority
            ON task.id_task = priority.id_task
    """)

    rows = cursor.fetchall()
    conn.close()

    data = []

    for row in rows:
        data.append({
            "nama_task": row[0],
            "prioritas": row[1],
            "status": row[2]
        })

    print(f"Total data : {len(data)}")

    # MAP
    
    def ubah_prioritas(task):

        skor = {
            "Rendah": 1,
            "Sedang": 2,
            "Tinggi": 3
        }

        return {
            "nama_task": task["nama_task"],
            "prioritas": task["prioritas"],
            "status": task["status"],
            "skor_prioritas": skor[task["prioritas"]]
        }

    mapped_data = list(map(ubah_prioritas, data))

    print("\n🟤🟤🟤 MAP 🟤🟤🟤")
    for task in mapped_data[:5]:
        print(task)

    # FILTER

    filtered_data = list(
        filter(lambda task: task["skor_prioritas"] == 3, mapped_data)
    )

    print("\n🟤🟤🟤 FILTER 🟤🟤🟤")
    for task in filtered_data[:5]:
        print(task)

    print(f"Jumlah task prioritas tinggi: {len(filtered_data)}") 

    # SORT

    sorted_data = sorted(
        mapped_data,
        key=lambda task: task["nama_task"]
    )

    print("\n🟤🟤🟤 SORT 🟤🟤🟤")
    for task in sorted_data[:5]:
        print(task)

    # REDUCE

    total_task = reduce(
        lambda x, y: x + y,
        map(lambda task: 1, mapped_data),
        0
    )
    
    total_belum_selesai = reduce(
        lambda x, y: x + y, 
        map(
            lambda task: 1 if task["status"].strip().lower() == "belum selesai" else 0, 
            mapped_data
        ),
        0
    )

    print("\n🟤🟤🟤 REDUCE 🟤🟤🟤")
    print(f"Total Task         : {total_task}")
    print(f"Task belum selesai : {total_belum_selesai}")

    print("\nKesimpulan:")

    if total_belum_selesai == 0:
        print("✅ Semua tugas sudah selesai")
    else:
        print(f"Masih ada {total_belum_selesai} tugas yang belum selesai‼️")

if __name__ == "__main__":
    print("Program dimulai")
    mapreduce_analysis()