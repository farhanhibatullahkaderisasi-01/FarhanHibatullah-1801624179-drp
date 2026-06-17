import sqlite3

def create_task (): 

    nama_task = input("Masukkan nama task: ")
    deadline = input ("Masukkan deadline task:")
    status = input ("Masukkan status task (Belum selesai/selesai):")

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO task (nama_task, deadline, status) VALUES (?, ?, ?)""", (nama_task, deadline, status))
    
    conn.commit()
    conn.close()

    print("✅Task berhasil ditambahkan!")


def read_task ():

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()

    print("\n📋 Daftar Task:")

    if len(tasks) == 0:
        print("Belum ada task yang ditambahkan.")

    else:
        for task in tasks:
            print (task)

    conn.close()

def update_task ():

    id_task = input ("Masukkan ID task yang ingin diupdate: ")
    status_baru = input ("Masukkan status baru (Belum selesai/selesai): ")

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""UPDATE task SET status = ? WHERE id_task = ?""", (status_baru, id_task))

    conn.commit()
    conn.close()

    print("✅Status task berhasil diupdate!")

def delete_task ():

    id_task = input ("Masukkan ID task yang ingin dihapus: ")

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""DELETE FROM task WHERE id_task = ?""", (id_task,))

    conn.commit()
    conn.close()

    print("🗑️Task berhasil dihapus!")