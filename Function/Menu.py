from os import system
from Function.LoadSave import loadUser

# Program Menu
# Program yang berisikan procedure khusus untuk penulisan menu

# ALGORITMA
def menu(type):
    system("cls")
    if type == "login":
        print("="*5 + " [Selamat Datang] " + "="*5)
        print("Siapakah Anda?\n")
        print("1. Admin\n2. Mahasiswa\n\n0. Keluar")
        print("="*28)
    elif type == "menuadmin":
        from Function.Login import holder # Mengambil global variabel holder yang ada di file login
        nama = loadUser(holder) # Mengambil nama user
        print("="*8 + " [Data Perpustakaan] " + "="*8)
        print("\nHalo, %s!\nApa yang ingin anda lakukan?\n" % nama[2])
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tabel Buku")
        print("4. Cari Buku")
        print("5. Peminjaman Buku")
        print("6. Restore Data Buku ke Default")
        print("7. Logout\n")
        print("0. Exit")
        print("="*37)
    elif type == "menumahasiswa":
        from Function.Login import holder # Mengambil global variabel holder yang ada di file login
        nama = loadUser(holder) # Mengambil nama user
        print("="*8 + " [Perpustakaan] " + "="*8)
        print("\nHalo, %s!\nApa yang ingin anda lakukan?\n" % nama[2])
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Tabel Buku")
        print("4. Cari Buku")
        print("5. Status Pribadi")
        print("6. Logout\n")
        print("0. Exit")
        print("="*30)
    elif type == "tipesearch":
        print("="*13 + " [Menu Cari Buku] " + "="*13)
        print("\nBerdasarkan apa anda ingin mencari bukunya?\n")
        print("1. Judul")
        print("2. Penulis")
        print("3. Penerbit")
        print("4. Tahun Terbit")
        print("="*44)