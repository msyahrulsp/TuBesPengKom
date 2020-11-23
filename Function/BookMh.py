from os import system
from time import sleep
from prettytable import PrettyTable
from Function.Menu import menu
from Function.LoadSave import *
from Function.BookChecker import *

# Program BookMh
# Program yang berisikan procedure untuk user jika masuk sebagai mahasiswa
# Penjelasan setiap procedure ada pada setiap procedure

# ALGORITMA
def pinjamBuku(): # Procedure peminjaman buku
    from Function.login import holder # Mengambil global variabel holder dari file login
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    system('cls')
    print("="*13 + " [Menu Peminjaman Buku] " + "="*13)

    if len(listBuku) > 0:
        listBukuPinjam = load("bukupinjam") # Menginisiasi listBukuPinjam sebagai list dari Pinjaman.csv
        user = loadUser(holder) # Mendapatkan list user dari User.csv
        nim = user[0]
        userfakul = user[1]
        username = user[2]

        id = input("\nID Buku: ")
        idx = getBukuMultiple(listBuku, "id", id) # Mendapatkan index buku sebagai list

        if len(idx) > 0:
            idx = idx[0] # Merubah index dari list, menjadi integer
            temp = [listBuku[idx][0], listBuku[idx][1], listBuku[idx][2], listBuku[idx][3], listBuku[idx][4]]
            t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit'])
            t.add_row(temp)
            print()
            print(t) # Menampilkan tabel buku yang idnya sesuai dengan id inputan user
            print("\nApa benar ini buku yang ingin anda pinjam?\n") 
            print("1. Ya\n2. Tidak")
            opsi = int(input("\nPilihan Anda? ")) # Opsi untuk konfirmasi peminjaman pada user

            while (opsi < 1) or (opsi > 2): # Validasi input
                print("\nPilihan yang tersedia hanya 1 dan 2!")
                sleep(1.5)
                system('cls')
                print("="*13 + " [Menu Peminjaman Buku] " + "="*13)
                print("\nID Buku: %s\n" % id)
                print(t)
                print("\nApa benar ini buku yang ingin anda pinjam?\n") 
                print("1. Ya\n2. Tidak")
                opsi = int(input("\nPilihan Anda? "))

            # Mendapatkan boolean apakah jumlah buku > 0
            buku = getJumlahBuku(listBuku, id)

            if (opsi == 1) and (buku == True): # Buku yang dicari ada
                system('cls')
                print("="*13 + " [Menu Peminjaman Buku] " + "="*13)
                print("\nID Buku: %s\n" % id)
                print(t)
                tgl = input("\nMasukkan Tanggal Sekarang (DD/MM/YYYY): ")

                while(dateValidation(tgl) != True): # Validasi tanggal
                    print("\nTanggal yang anda masukkan tidak valid")
                    print("Contoh penulisan yang benar. 1/1/0001 atau 01/01/0001")
                    sleep(1.5)
                    system('cls')
                    print("="*13 + " [Menu Peminjaman Buku] " + "="*13)
                    print("\nID Buku: %s\n" % id)
                    print(t)
                    tgl = input("\nMasukkan Tanggal Sekarang (DD/MM/YYYY): ")

                tgl = dateStripper(tgl) # Menghilangkan angka 0 di depan angka
                listBukuPinjam.append([listBuku[idx][0], listBuku[idx][1], listBuku[idx][2], listBuku[idx][3], listBuku[idx][4], username, nim, userfakul, tgl])
                listBuku[idx][5] = str(int(listBuku[idx][5]) - 1)
                listBuku[idx][6] = str(int(listBuku[idx][6]) + 1)
                save("buku", listBuku)
                save("bukupinjam", listBukuPinjam)
                print('\nBuku %s telah dipinjam' % listBuku[idx][1])

            elif buku == False: # Jumlah buku tidak memadai
                print("\nBuku %s sedang tidak tersedia" % listBuku[idx][1])

        else: # Pencari buku yang ingin dipinjam tidak ada
            print("\nBuku yang anda ingin pinjam tidak ada")

    else: # Buku tidak ada sama sekali
        print('\nMaaf, kami belum memiliki buku')
    input('\nTekan ENTER untuk kembali')

def kembaliBuku(): # Procedure untuk pengembalian buku
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    listBukuPinjam = load("bukupinjam") # Menginisiasi listBukuPinjam sebagai list dari Pinjaman.csv 
    listBukuHistory = load("bukuhistory") # Menginisiasi listBukuHistory sebagai list dari History.csv
    listDenda = load("denda") # Menginisiasi listDenda sebagai list dari Denda.csv
    from Function.Login import holder # Mengambil global variabel holder dari file login
    user = loadUser(holder) # Mendapatkan list user dari User.csv
    nim = user[0]
    system("cls")
    print("="*12 + " [Menu Pengembalian Buku] " + "="*12 + "\n")
    t = PrettyTable(['No', 'ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Tanggal Pinjam'])
    buku = getBukuPinjaman(listBukuPinjam, nim) # Mendapatkan buku sebagai list dari listBukuPinjaman yang mengandung nim

    if len(buku) > 0:
        idx = getIndexBukuPinjaman(listBukuPinjam, nim) # Mendapatkan index di peminjaman buku
        counter = 1

        for x in buku:
            temp = [counter, x[0], x[1], x[2], x[3], x[4], x[8]]
            t.add_row(temp)
            counter += 1
        print(t) # Menampilkan tabel buku yang peminjamnya user
        no = int(input("\nNo Buku yang ingin dikembalikan > "))

        while (no < 1) or (no > len(idx)): # Validasi input
            print("Pilihan yang tersedia hanya %d sampai %d" % (1, len(idx)))
            sleep(1.5)
            system("cls")
            print("="*12 + " [Menu Pengembalian Buku] " + "="*12 + "\n")
            print(t)
            no = int(input("\nNo Buku yang ingin dikembalikan > "))

        tgl = input("Masukkan Tanggal Pengembalian (DD/MM/YYYY): ")

        while(dateValidation(tgl) != True): # Validasi input
            print("Tanggal yang anda masukkan tidak valid")
            print("Contoh penulisan yang benar. 1/1/0001 atau 01/01/0001")
            sleep(1.5)
            system("cls")
            print("="*12 + " [Menu Pengembalian Buku] " + "="*12 + "\n")
            print(t)
            print("\nNo Buku yang ingin dikembalikan > %s" % no)
            tgl = input("Masukkan Tanggal Pengembalian (DD/MM/YYYY): ")

        tgl = dateStripper(tgl) # Menghilangkan 0 di depan angka
        idx = idx[no-1]
        denda = countDenda(listBukuPinjam, tgl, idx) # Mendapatkan banyak denda yang didapatkan
        
        # Menambahkan data pada list listBukuHistory
        listBukuHistory.append([listBukuPinjam[idx][0], listBukuPinjam[idx][1], listBukuPinjam[idx][2], listBukuPinjam[idx][3], listBukuPinjam[idx][4], listBukuPinjam[idx][8], tgl, denda, listBukuPinjam[idx][6]]) 

        idxbuku = getBukuMultiple(listBuku, "id", listBukuPinjam[idx][0]) # Mendapatkan list id buku yang sesuai dengan listBukuPinjam[idx][0]
        idxbuku = idxbuku[0] # Mengubah menjadi string

        print('\nBuku %s telah dikembalikan' % listBukuPinjam[idx][1])
        del listBukuPinjam[idx] # Menghapus elemen dari listBukuPinjaman

        # Mengubah jumlah buku yang sedang dan tidak sedang dipinjam
        listBuku[idxbuku][5] = str(int(listBuku[idxbuku][5]) + 1)
        listBuku[idxbuku][6] = str(int(listBuku[idxbuku][6]) - 1)

        idxdenda = getIndexDenda(listDenda, nim) # Mendapatkan index nim pada listDenda
        listDenda[idxdenda][1] = str(int(listDenda[idxdenda][1]) + denda) # Menambah denda

        # Menyimpan data pada file yang sesuai dengan tipenya
        save('buku', listBuku)
        save('bukupinjam', listBukuPinjam)
        save('bukuhistory', listBukuHistory)
        save('denda', listDenda)
        if denda > 0:
            print('Anda mendapat denda sebesar Rp.%d' % denda)
    else:
        print(t)
        print('\nAnda sedang tidak meminjam buku')
    input("\nTekan ENTER untuk kembali")
    

def showBukuMh(): # Procedure untuk menampilkan semua buku (mahasiswa)
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    system("cls")
    print("="*23 + " [Tabel Data Buku] " + "="*23 + "\n")
    t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit'])
    for x in listBuku:
        t.add_row(x[:5]) # Menambah buku yang ada pada listBuku sampai data Tahun Terbit
    print(t)
    input("\nTekan ENTER untuk kembali")

def cariBukuMh():
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    menu("tipesearch")
    temp = int(input("Pilihan Anda > "))

    # Validasi inputan
    # Opsi antara 1 sampai 4
    while (temp < 1) or (temp > 4):
        print("\nPilihan yang tersedia hanya 1 sampai 4!")
        sleep(1.5)
        menu("caribuku")
        temp = int(input("\nPilihan Anda? "))

    if temp == 1:
        name = "Judul"
    elif temp == 2:
        name = "Penulis"
    elif temp == 3:
        name = "Penerbit"
    else:
        name = "Tahun"

    system("cls")
    print("="*13 + " [Menu Cari Buku] " + "="*13)
    search = input("\nHasil %s yang dicari: " % name) # Input
    print()
    idx = getBukuMultiple(listBuku, name.lower(), search) # Mendapatkan index buku sebagai list

    t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit'])
    if len(idx) > 0:
        for x in idx:
            t.add_row(listBuku[x][:5])
    print(t) # Menampilkan tabel buku yang sesuai dengan tipe dan input pencarian user
    input("\nTekan ENTER untuk kembali")

def status():
    listBukuPinjam = load("bukupinjam")
    listBukuHistory = load('bukuhistory')
    from Function.Login import holder # Mengambil global variabel holder dari file login
    user = loadUser(holder) # Mengambil data user sebagai list
    denda = int(getDenda(holder)) # Mengambil banyak denda user sebagai int
    nim = user[0]
    userfakul = user[1]
    username = user[2]
    system("cls")
    print("="*33 + " [Status Peminjaman] " + "="*33)
    print("\nNama     : %s" % username)
    print("NIM      : %s" % nim)
    print("Fakultas : %s" % userfakul)
    print(f"Denda    : Rp{denda:,d}\n")
    print("\t\t- Buku yang Sedang Dipinjam -\n")

    t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Tanggal Pinjam'])
    buku = getBukuPinjaman(listBukuPinjam, nim)
    if len(buku) > 0:    
        for x in buku:
            temp = [x[0], x[1], x[2], x[3], x[4], x[8]]
            t.add_row(temp)
    print(t) # Menampilkan tabel buku yang sedang dipinjam oleh user
    print("\n\t\t- Buku yang Pernah Dikembalikan -\n")

    history = getBukuHistory(listBukuHistory, nim)

    u = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Tanggal Pinjam', 'Tanggal Kembali', 'Denda'])
    if len(history) > 0:
        for x in history:
            x[7] = f"Rp{int(x[7]):,d}"
            temp = [x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]]
            u.add_row(temp)
    print(u) # Menampilkan tabel buku yang sudah dikembalika oleh user
    input("\nTekan ENTER untuk kembali")