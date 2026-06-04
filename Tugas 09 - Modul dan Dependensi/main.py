from menu import tampilkan_menu
from tracker import tambah_tugas
from progress import tampilkan_progress
from reminder import cek_stres

daftar_tugas = []

while True:

    tampilkan_menu()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":

        daftar_tugas = tambah_tugas()

    elif pilihan == "2":

        tampilkan_progress(daftar_tugas)

    elif pilihan == "3":

        cek_stres(daftar_tugas)

    elif pilihan == "4":

        print("Program selesai.")
        break

    else:

        print("Pilihan tidak tersedia.")