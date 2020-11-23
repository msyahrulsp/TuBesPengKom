from os import system
from time import sleep
from prettytable import PrettyTable
from Function.Menu import menu
from Function.LoadSave import *
from Function.BookChecker import getBukuSingle, getBukuMultiple

# Program BookAdmin
# Program yang berisikan procedure untuk user jika masuk sebagai admin
# Penjelasan setiap procedure ada pada setiap procedure

# ALGORITMA
def tambahBuku(): # Procedure untuk menambahkan buku (admin)
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    system("cls")
    print("="*8 + " [Menu Tambah Buku] " + 8*"=" + "\n")
    judul = input("Judul Buku: ")
    penulis = input("Penulis Buku: ")
    penerbit = input("Penerbit Buku: ")
    tahun = int(input("Tahun Terbit: "))
    n = int(input("Banyak Buku: "))
    idx = getBukuSingle(listBuku, judul, penulis, penerbit, str(tahun)) # Mengecek apa buku yang dimasukkan sudah ada

    if idx != None: # Buku sudah ada
        print('\n%d buku %s telah ditambahkan' % (n, listBuku[idx][1]))
        listBuku[idx][5] = str(int(listBuku[idx][5]) + n) # Menambahkan jumlah buku
    else: # Buku belum ada
        temp = listBuku[len(listBuku)-1][0].split('K')
        id = "BK" + str(int(temp[1])+1)
        listBuku.append([id, judul, penulis, penerbit, str(tahun), str(n), str(0)])
        print('\nBuku %s telah ditambahkan' % listBuku[len(listBuku)-1][1])

    save("buku", listBuku) # Menyimpan list listBuku ke Buku.csv
    input('\nTekan ENTER untuk kembali')

def hapusBuku(): # Procedure untuk menghapus buku
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    system("cls")
    print("="*8 + " [Menu Hapus Buku] " + 8*"=" + "\n")

    if len(listBuku) == 0: # Jika tidak ada buku di Buku.csv, otomatis tidak menjalankan pengecekan yang lain
        print('Belum ada buku yang bisa anda hapus')
        input("\nTekan ENTER untuk kembali")
    else: # Ada buku
        id = input("ID Buku: ")
        index = getBukuMultiple(listBuku, "id", id) # Mendapat 1 index yg disimpan sebagai list
        if len(index) > 0:
            index = index[0] # Index di list diubah menjadi integer
            n = int(input("Banyak Buku: "))

            while n > int(listBuku[index][5]) or (n < 0): # Safecase untuk n yang tidak sesuai
                if n > int(listBuku[index][5]):
                    print("\nMax buku yang bisa dihapus ialah %d!" % (int(listBuku[index][5])))
                else:
                    print("\nBanyak buku yang dimasukkan harus lebih dari -1!")
                sleep(1.5)
                system("cls")
                print("="*8 + " [Menu Hapus Buku] " + 8*"=" + "\n")
                print("ID Buku: " + id)
                n = int(input("Banyak Buku: "))

            if (n == int(listBuku[index][5])) and (int(listBuku[index][6]) == 0):
                print('\nBuku %s telah dihapus' % listBuku[index][1])
                del listBuku[index] # Buku akan otomatis terhapus n sama dengan stok buku dan sedang tidak ada yang meminjam
            else: # n != jumlah or ada yang meminjam
                print('\n%d buku %s telah dihapus' % (n, listBuku[index][1]))
                listBuku[index][5] = str(int(listBuku[index][5]) - n) # Hanya mengurangi stok buku

            save("buku", listBuku) # Menyimpan list listBuku ke Buku.csv

        else:
            print("\nBuku yang anda ingin hapus tidak ada!")
        input("\nTekan ENTER untuk kembali")

def showBukuAdmin(): # Procedure untuk menampilkan semua buku (khusus admin)
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    system('cls')
    print("="*39 + " [Tabel Data Buku] " + "="*39 + "\n")

    t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Banyak Buku', 'Banyak Dipinjam'])
    for x in listBuku:
        t.add_row(x)
    print(t) # Menampilkan tabel buku
    input("\nTekan ENTER untuk kembali")

def cariBukuAdmin(): # Procedure untuk mencari buku
    listBuku = load("buku") # Menginisiasi listBuku sebagai list dari Buku.csv
    menu("tipesearch")
    temp = int(input("Pilihan Anda > "))

    while (temp < 1) or (temp > 4): # Safecase jika opsi yang dimasukkan tidak sesuai
        print("\nPilihan yang tersedia hanya 1 sampai 4!")
        sleep(1.5)
        menu("caribuku")
        temp = int(input("\nPilihan Anda? "))

    if temp == 1:
        name = "Judul" # Tipe pencarian dari judul
    elif temp == 2:
        name = "Penulis" # Tipe pencarian dari penulis
    elif temp == 3:
        name = "Penerbit" # Tipe pencarian dari penerbit
    else:
        name = "Tahun" # Tipe pencarian dari tahun

    system("cls")
    print("="*13 + " [Menu Cari Buku] " + "="*13)
    search = input("\nHasil %s yang dicari: " % name) # Mencari buku dari tipe yang telah ditentukan
    print()
    idx = getBukuMultiple(listBuku, name.lower(), search)

    t = PrettyTable(['ID', 'Judul', 'Penulis', 'Penerbit', 'Tahun Terbit', 'Banyak Buku', 'Banyak Dipinjam']) # Inisiasi header tabel
    if len(idx) > 0:
        for x in idx:
            t.add_row(listBuku[x])
    print(t) # Menampilkan tabel buku yang mengandung string inputan user
    input("\nTekan ENTER untuk kembali")

def pnjmBuku(): # Procedure untuk menampilkan peminjam buku
    listBukuPinjam = load("bukupinjam") # Menginisiasi listPinjam sebagai list dari Pinjaman.csv
    system("cls")
    print("="*24 + " [Tabel Data Buku Pinjaman] " + "="*24 + "\n")

    t = PrettyTable(['ID', 'Judul', 'Nama', 'NIM', 'Fakultas', 'Tanggal Pinjam']) # Inisiasi header tabel
    if listBukuPinjam != None:
        for x in listBukuPinjam:
            temp = [x[0], x[1], x[5], x[6], x[7], x[8]]
            t.add_row(temp)
    print(t) # Menampilkan tabel data peminjam buku
    input("\nTekan ENTER untuk kembali")

def restore(): # Procedure untuk mereset data ke default
    system("cls")
    print("="*10 + " [Restore Data] " + "="*10)
    print("\nApakah anda yakin?\n\n1. Ya\n2. Tidak")
    pil = int(input("\nPilihan Anda > ")) # Konfirmasi untuk user
    
    if pil == 1: # Telah dikonfirmasi
        # Reset semua data ke default
        file = open('Data/Buku.csv', 'w')
        temp = "BK1,Phi-Wiki,Tim Phi-Wiki,HIMAFI ITB,2014,14,0\nBK2,MathCo,Tim MathCo,ITB,2020,5,0\nBK3,Purcell,Varberg,Rigdon,2007,4,0\nBK4,Halliday,Resnick,Walker,2003,5,0\nBK5,Kimia Dasar,Raymond Chang,Erlangga,2005,12,0"
        file.write('%s' % temp)
        file.close()
        file = open('Data/Pinjaman.csv', 'w')
        file.write('')
        file.close()
        file = open('Data/History.csv', 'w')
        file.write('')
        file.close()
        file = open('Data/Denda.csv', 'w')
        file.write('16520450,0\n16520440,0\n16520430,0\n16520460,0')
        file.close()
        print('\nData telah direstore ke default')
        input('\nTekan ENTER untuk kembali')