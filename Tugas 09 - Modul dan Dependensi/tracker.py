def tambah_tugas():
    tugas = []

    jumlah = int(input("Berapa tugas yang ingin ditambahkan? "))

    for i in range(jumlah):
        print(f"\nTugas ke-{i+1}")

        nama = input("Nama tugas: ")
        deadline = input("Deadline: ")

        data = {
            "nama": nama,
            "deadline": deadline,
            "status": "Belum Selesai"
        }

        tugas.append(data)

    return tugas