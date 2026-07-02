import sqlite3 
import json

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

def export_json():

   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.execute("SELECT * FROM reminder")
   reminder = cursor.fetchall()

   with open("reminder_backup.json", "w") as file:
      json.dump(reminder, file, indent=4)

   conn.close()

   print("Export reminder berhasil!")

def import_json():

   with open("reminder_backup.json", "r") as file:
      reminder = json.load(file)

   conn = sqlite3.connect("taskmate.db")
   cursor = conn.cursor()

   cursor.execute("DELETE FROM reminder")

   for item in reminder:
      cursor.execute("""
      INSERT INTO reminder (id_reminder, pesan, id_task)
      VALUES (?, ?, ?)
      """, item)

   conn.commit()
   conn.close()

   print("Import reminder berhasil!")

if __name__ == "__main__":
   pilihan = input(
      "1. Tambah Reminder\n"
      "2. Lihat Reminder\n"
      "3. Update Reminder\n"
      "4. Hapus Reminder\n"
      "5. Export Reminder\n"
      "6. Import Reminder\n"
      "Pilih:"
   )

   if pilihan == "1":
      create_reminder()
   elif pilihan == "2":
      read_reminder()
   elif pilihan == "3":
      update_reminder()
   elif pilihan == "4":
      delete_reminder()
   elif pilihan == "5":
      export_json()
   elif pilihan == "6":
      import_json()
