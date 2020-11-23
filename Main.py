from os import system
from time import sleep
from Function.Menu import menu
from Function.Login import adminLogin, studentLogin
from Function.BookAdmin import tambahBuku, hapusBuku, showBukuAdmin, cariBukuAdmin, pnjmBuku, restore
from Function.BookMh import pinjamBuku, kembaliBuku, showBukuMh, cariBukuMh, status

# Program Main
# Program yang menjadi tempat untuk menjalankan semua function dan procedure yang ada
# dari file lain, dengan tambahan procedure choose()

# ALGORITMA
def choose(): # Procedure yang berguna untuk menentukan tipe user
    global pick # Global variabel
    menu("login")
    pick = int(input("Pilihan Anda > "))
    while (pick < 0) or (pick > 2): # Safecase jika input yang dimasukkan tidak sesuai
        print("\nPilihan yang tersedia hanya 0 sampai 2!")
        sleep(1.5) # "Menghentikan" program selama 1.5 detik
        menu("login")
        pick = int(input("Pilihan Anda > "))
    if pick == 1:
        adminLogin() # Procedure untuk user login sebagai admin
    elif pick == 2:
        studentLogin()# Procedure untuk user login sebagai mahasiswa
    else:
        system('cls')
        exit() # Keluar program

try: # Antisipasi untuk keluar dengan CTRL + C
    choose() # Procedure untuk memilih tipe user
    # Menghasilkan global variabel pick
    while True:
        if pick == 1:
            menu("menuadmin") # Mennjukkan menu admin
            opt = int(input("Pilihan Anda > "))
            if opt == 1:
                tambahBuku() # Membuat user menambah buku
            elif opt == 2:
                hapusBuku() # Menghapus buku dari list yang ada
            elif opt == 3:
                showBukuAdmin() # Menunjukkan data buku khusus admin
            elif opt == 4:
                cariBukuAdmin() # Mencari buku sesuai tipe yang nanti dipilih (khusus mahasiswa)
            elif opt == 5:
                pnjmBuku() # Melihat data mahasiswa yang telah meminjam buku
            elif opt == 6:
                restore() # Mereset semua data ke default
            elif opt == 7:
                choose() # Kembali ke menu pilihan tipe user
            else:
                system('cls')
                exit() # Keluar dari program
        elif pick == 2:
            menu("menumahasiswa")
            opt = int(input("Pilihan Anda > "))
            if opt == 1:
                pinjamBuku() # User meminjam buku dari list yang ada
            elif opt == 2:
                kembaliBuku() # "Mengembalikan buku", setiap telat 14 hari denda 10000
            elif opt == 3:
                showBukuMh() # Menunjukkan data buku khusus admin
            elif opt == 4:
                cariBukuMh() # Mencari buku sesuai tipe yang nanti dipilih (khusus mahasiswa)
            elif opt == 5:
                status() # Menunjukkan data user (mahasiswa) dan buku yang telah dipinjam
            elif opt == 6:
                choose() # Kembali ke menu pilihan tipe user
            else:
                system('cls')
                exit() # Keluar dari program
        else:
            exit()
except KeyboardInterrupt: # Exit alternatif dengan CTRL + C
    system('cls')