def tampilkan_progress(tugas):

    selesai = 0

    for item in tugas:
        if item["status"] == "Selesai":
            selesai += 1

    total = len(tugas)

    print("\n=== PROGRESS TUGAS ===")
    print(f"Total tugas : {total}")
    print(f"Selesai     : {selesai}")
    print(f"Belum       : {total - selesai}")