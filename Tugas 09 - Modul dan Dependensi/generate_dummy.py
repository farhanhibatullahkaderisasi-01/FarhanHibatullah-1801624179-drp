import json
import random 

print("Program dimulai")

data = []

status_list = ["Selesai", "Belum Selesai"]
prioritas_list = ["Rendah", "Sedang", "Tinggi"]

for i in range(1, 60000):
    task = {
        "id_task": i,
        "nama_task": f"Task {i}",
        "prioritas": random.choice(prioritas_list),
        "status": random.choice(status_list)
       
    }
    data.append(task)

with open("data/dummy_task.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Data dummy berhasil dibuat!")