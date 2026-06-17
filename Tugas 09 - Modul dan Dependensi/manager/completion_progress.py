import sqlite3 

def create_progress():

    persentase = int(input("Masukan persentase progress: "))
    id_task = int(input("Masukan ID task: "))

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.excute("""
    INSERT INTO progress (persentase, id_task)
    VALUES (?, ?)
    """, (persentase, id_task))

    conn.commit()
    conn.close()

    print("✅ Progress berhasil ditambahkan!")


def read_progress():
    
    conn = sqlite3.connect("taskmate.db")
    cursor = con.cursor()

    cursor.excute("SELECT * FROM progress")
    progress = cursor.fetchall()

    print("\n📊 Daftar Progress:")

    if len(progress) == 0:
        print("Belum ada progress.")

    else:
        for item in progress:
            print(item)

    conn.close()

def update_progress():

    id_progress = input("Masukkan ID progress yang ingin diupdate: ")
    persentase_baru = imput("Masukkan persentase baru: ")

    conn = sqlite3.connet("taskmate.db")
    cursor = conn.cursor()

    cursor.excute("""
    UPDATE progress
    SET persentase = ?
    WHERE id_progress = ?
    """, (persentase_baru, id_progress))

    conn.commit()
    conn.close()

    print("✅ Progress berhasil diperbarui!")    

def delete_progress():

    id_progress = input("Masukkan ID progress yang ingin dihapus: ")

    conn = sqlite3.connet("taskmate.db")
    cursor = conn.cursor()

    cursor.excute("""
    DELETE FROM progress 
    WHERE id_progress = ?
    """, (id_progress,))

    conn.commit()
    conn.close()

    print("🗑️ Progress berhasil dihapus!")
        