import sqlite3
import json 

def export_json():

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    #Export Task
    cursor.execute("SELECT * FROM task")
    tasks = cursor.fetchall()

    #Export Priority
    cursor.execute("SELECT * FROM priority")
    priority = cursor.fetchall()

    #Export Progress
    cursor.execute("SELECT * FROM progress")
    progress = cursor.fetchall()

    #Export Reminder
    cursor.execute("SELECT * FROM reminder")
    reminder = cursor.fetchall()

    data = {}

    data ["task"] = tasks
    data ["priority"] = priority
    data ["progress"] = progress
    data ["reminder"] = reminder

    with open ("backup.json", "w") as file:
        json.dump(data, file, indent=4)

    conn.close()

    print("✅ Export berhasil!")


def import_json(): 
    
    with open ("backup.json", "r") as file:
        data = json.load(file)

    conn = sqlite3.connect("taskmate.db")
    cursor = conn.cursor()

    #Hapus data lama
    cursor.execute("DELETE FROM task")
    cursor.execute("DELETE FROM priority")
    cursor.execute("DELETE FROM progress")
    cursor.execute("DELETE FROM reminder")

    #Reset auto increment
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='task'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='priority'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='progress'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='reminder'")

    #Import Task
    for task in data["task"]:
        cursor.execute ("""
        INSERT INTO task (id, nama_task, deadline, status, id_user, id_priority) VALUES (?, ?, ?, ?, ?, ?)
        """, task)

    #Import Priority
    for priority in data["priority"]:
        cursor.execute ("""
        INSERT INTO priority (id_priority, kategori) VALUES (?, ?)
        """, priority)

    #Import Progress
    for progress in data["progress"]:
        cursor.execute ("""
        INSERT INTO progress (id_progress, persentase, id_task) VALUES (?, ?, ?)
        """, progress)

    #Import Reminder
    for reminder in data["reminder"]:
        cursor.execute ("""
        INSERT INTO reminder (id_reminder, pesan, id_task) VALUES (?, ?, ?)
        """, reminder)

    conn.commit()
    conn.close()

    print("✅ Import berhasil!")

if __name__ == "__main__":
    pilihan = input ("1. Export\n2. Import\nPilih:")

    if pilihan == "1":
        export_json()
    elif pilihan == "2":
        import_json()