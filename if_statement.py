from datetime import datetime

print("=== MANAJEMEN AKTIVITAS ===")

aktivitas = input("Masukkan aktivitas (sarapan/kerja): ")

# Aktivitas sarapan
if aktivitas == "sarapan":
    menu = input("Pilih menu (telur/ikan/nugget): ")

    if menu == "telur":
        print("Telur tersedia, silakan dimasak terlebih dahulu.")

    elif menu == "ikan":
        print("Ikan tersedia, silakan dimasak terlebih dahulu.")

    elif menu == "nugget":
        print("Nugget tersedia, silakan dimasak terlebih dahulu.")

    else:
        print("Menu tidak tersedia, silakan beli bahan terlebih dahulu.")

# Aktivitas kerja
elif aktivitas == "kerja":
    sekarang = datetime.now()

    jam = sekarang.hour
    menit = sekarang.minute

    print(f"Waktu sekarang: {jam}:{menit}")

    if jam >= 8:
        print("Anda terlambat masuk kerja!")

    else:
        print("Anda masih tepat waktu untuk kerja.")

# Jika input salah
else:
    print("Aktivitas tidak dikenali.")