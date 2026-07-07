import json 
from functools import reduce

def mapreduce_analysis():

    with open("data/dummy_task.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print(f"Total data : {len(data)}")

    # MAP
    
    def ubah_prioritas(task):

        skor = {
            "Rendah": 1,
            "Sedang": 2,
            "Tinggi": 3
        }

        return {
            "nama_task": task["nama_task"],
            "prioritas": task["prioritas"],
            "status": task["status"],
            "skor_prioritas": skor[task["prioritas"]]
        }

    mapped_data = list(map(ubah_prioritas, data))

    print("\n=== MAP ===")
    for task in mapped_data[:5]:
        print(task)

    # FILTER

    filtered_data = list(
        filter(lambda task: task["skor_prioritas"] == 3, mapped_data)
    )

    print("\n=== FILTER ===")
    for task in filtered_data[:5]:
        print(task)

    print(f"Jumlah task prioritas tinggi: {len(filtered_data)}") 

    # SORT

    sorted_data = sorted(
        mapped_data,
        key=lambda task: task["nama_task"]
    )

    print("\n=== SORT ===")
    for task in sorted_data[:5]:
        print(task)

    # REDUCE
    
    total_selesai = reduce(
        lambda x, y: x + y, 
        map(lambda task: 1 if task["status"] == "Selesai" else 0, mapped_data)
    )

    print("\n=== REDUCE ===")
    print(f"Total task selesai      : {total_selesai}")
    print(f"Total task keseluruhan  : {len(mapped_data)}")

if __name__ == "__main__":
    print("Program dimulai")
    mapreduce_analysis()