import sqlite3 

def create_reminder():
    
   pesan = input("Masukan pesan reminder: ")
   id_task = int(input("Masukkan ID task: "))

   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.execute("""
   INSERT INTO reminder (pesan, id_task)
   VALUES (?, ?)
   """, (pesan, id_task))
    
   conn.commit()
   conn.close()

   print("✅ Reminder berhasil ditambahkan!")


def read_reminder():
    
   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.excute("SELECT * FROM reminder")
   reminders = cursor.fetchall()

   print("\n🔔 Daftar Reminder")

   if len(reminders) == 0:
      print("Belum ada reminder. ")

   else:
      for reminder in reminders:
         print(reminder)

   conn.close()


def update_reminder():
    
   id_reminder = input("Masukkan ID reminder yang ingin diupdate: ")
   pesan_baru = input("Masukkan pesan baru: ")

   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.execute("""
   UPDATE reminder
   SET pesan = ?
   WHERE id_reminder = ?
   """, (pesan_baru, id_reminder))

   conn.commit()
   conn.close()

   print("✅ Reminder berhasil diperbarui!")


def delete_reminder():
    
   id_reminder = input("Masukkan ID reminder yang ingin dihapus: ")

   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.execute("""
   DELETE FROM reminder
   WHERE id_reminder = ?
   """, (id_reminder,))

   conn.commit()
   conn.close()

   print("🗑️ Reminder berhasil dihapus!")