import sqlite3 

def create_progress():

    persentase = int(input("Masukkan persentase progress: "))
    id_task = int(input("Masukkan ID task: "))

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO progress (persentase, id_task)
    VALUES (?, ?)
    """, (persentase, id_task))

    conn.commit()
    conn.close()

    print("✅ Progress berhasil ditambahkan!")


def read_progress():
    
    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM progress")
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
    persentase_baru = input("Masukkan persentase baru: ")

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE progress
    SET persentase = ?
    WHERE id_progress = ?
    """, (persentase_baru, id_progress))

    conn.commit()
    conn.close()

    print("✅ Progress berhasil diperbarui!")    

def delete_progress():

    id_progress = input("Masukkan ID progress yang ingin dihapus: ")

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM progress 
    WHERE id_progress = ?
    """, (id_progress,))

    conn.commit()
    conn.close()

    print("🗑️ Progress berhasil dihapus!")
        
def completion_progress():

    while True:
        print("\n=== COMPLETION PROGRESS ===")
        print("1. Tambah Progress")
        print("2. Lihat Progress")
        print("3. Update Progress")
        print("4. Hapus Progress")
        print("5. Kembali")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            create_progress()
        elif pilihan == "2":
            read_progress()
        elif pilihan == "3":
            update_progress()
        elif pilihan == "4":
            delete_progress()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid")

            
