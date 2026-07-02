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
    cursor = conn.cursor()

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
    persentase_baru = input("Masukkan persentase baru: ")

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
        
import json

def export_json():
    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM progress")
    progress = cursor.fetchall()

    with open("progress_backup.json", "w") as file:
        json.dump(progress, file, indent=4)

    conn.close()
    print("Export progress berhasil!")

def import_json():
    with open("progress_backup.json", "r") as file:
        progress = json.load(file)

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM progress")

    for item in progress:
        cursor.execute("""
        INSERT INTO progress (id_progress, persentase, id_task)
        VALUES (?, ?, ?)
        """, item)

    conn.commit()
    conn.close()

    print("Import progress berhasil!")

if __name__ == "__main__":
    pilihan = input(
        "1. Tambah Progress\n"
        "2. Lihat Progress\n"
        "3. Update Progress\n"
        "4. Hapus Progress\n"
        "5. Export Progress\n"
        "6. Import Progress\n"
        "Pilih: "   
    )

if pilihan == "1":
    create_progress()
elif pilihan == "2":
    read_progress()
elif pilihan == "3":
    update_progress()
elif pilihan == "4":
    delete_progress()
elif pilihan == "5":
    export_json()
elif pilihan == "6":
    import_json()
