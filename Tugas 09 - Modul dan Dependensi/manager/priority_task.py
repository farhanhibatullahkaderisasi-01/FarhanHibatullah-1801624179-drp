import sqlite3

def create_priority ():

    kategori = input ("Masukkan kategori prioritas:")

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO priority (kategori) VALUES (?)""", (kategori,))

    conn.commit()
    conn.close()

    print("✅Kategori prioritas berhasil ditambahkan!")

def read_priority ():  

    conn = sqlite3.connect ("taskmate.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM priority")
    priorities = cursor.fetchall()

    print("\n📋 Daftar Prioritas:")

    if len(priorities) == 0:
        print("Belum ada kategori prioritas yang ditambahkan.")

    else:
        for priority in priorities:
            print (priority)

    conn.close()

def update_priority (): 

    id_priority = input ("Masukkan ID kategori prioritas yang ingin diupdate: ")  
    kategori_baru = input ("Masukkan kategori prioritas baru: ")  

    conn = sqlite3.connect ("taskmate.db") 
    cursor = conn.cursor()  

    cursor.execute("""UPDATE priority SET kategori = ? WHERE id_priority = ?""", (kategori_baru, id_priority))

    conn.commit() 
    conn.close()    

    print("✅Kategori prioritas berhasil diupdate!")

def delete_priority (): 

    id_priority = input ("Masukkan ID kategori prioritas yang ingin dihapus: ") 

    conn = sqlite3.connect ("taskmate.db") 
    cursor = conn.cursor() 

    cursor.execute("""DELETE FROM priority WHERE id_priority = ?""", (id_priority,)) 

    conn.commit()
    conn.close() 

    print("🗑️Kategori prioritas berhasil dihapus!")

   
