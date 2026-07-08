import sqlite3 

def create_reminder():
    
   pesan = input("Masukkan pesan reminder: ")
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

   cursor.execute("SELECT * FROM reminder")
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

def stress_reminder():

   while True:
      print("\n=== STRESS REMINDER ===")
      print("1. Tambah Reminder")
      print("2. Lihat Reminder")
      print("3. Update Reminder")
      print("4. Hapus Reminder")
      print("5. Kembali")

      pilihan = input("Pilih: ")

      if pilihan == "1":
         create_reminder()
      elif pilihan == "2":
         read_reminder()
      elif pilihan == "3":
         update_reminder()
      elif pilihan == "4":
         delete_reminder()
      elif pilihan == "5":
         break
      else:
         print("Pilihan tidak valid")
         