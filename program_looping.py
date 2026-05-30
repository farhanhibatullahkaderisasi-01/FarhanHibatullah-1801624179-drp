print("=== PENDATAAN AKTIVITAS HARIAN ===")

# List kosong untuk menyimpan aktivitas
daftar_aktivitas = []

# Input jumlah aktivitas
jumlah = int(input("Berapa aktivitas yang ingin didata? "))

# Looping input aktivitas
for i in range(jumlah):

    print(f"\nAktivitas ke-{i + 1}")

    aktivitas = input("Masukkan nama aktivitas: ")
    durasi = input("Masukkan durasi aktivitas: ")

    data = aktivitas + " - " + durasi

    daftar_aktivitas.append(data)

# Menampilkan hasil
print("\n=== DAFTAR AKTIVITAS ===")

for i in range(len(daftar_aktivitas)):
    print(f"{i + 1}. {daftar_aktivitas[i]}")