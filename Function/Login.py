from time import sleep
from os import system
from Function.LoadSave import load

# Program Login
# Program yang mengandung procedure dan function khusus untuk login user
# Untuk procedure adminLogin() dan studentLogin(), ketika dieksekusi akan menghasilkan
# global variabel 'holder' yang akan digunakan pada file lain

# ALGORITMA
def checkLogin(type, user, pw): # Procedure pengecek data login usr
    if type == "admin":
        lstAdmin = load("Admin") # Menginisiasi lstAdmin sebagai list dari User.csv

        for i in range(len(lstAdmin)):
            if (lstAdmin[i][0] == user) and (lstAdmin[i][1] == pw): # idadmin == inputanid dan passadmin == inputanpass
                return True # Sama
        return False # Beda

    if type == "mahasiswa":
        lstMaha = load("Mahasiswa") # Menginisiasi lstMaha sebagai list dari User.csv

        for i in range(len(lstMaha)):
            if (user == lstMaha[i][0]): # nim == inputan
                return True # Sama
        return False # Beda

def adminLogin():
    global holder # global variabel
    system("cls")
    print("="*5 + " [Menu Login Admin] " + "="*5 + "\n")
    id = input("Username: ")
    password = input("Password: ")

    # Validasi ID dan password
    # 1 akun admin setidaknya akan selalu terdaftar
    while checkLogin("admin", id, password) != True:
        print("Data yang anda masukkan salah!")
        sleep(1.5)
        system("cls")
        print("="*5 + " [Menu Login Admin] " + "="*5 + "\n")
        id = input("Username: ")
        password = input("Password: ")
        
    holder = id

def studentLogin():
    global holder # global variabel
    system("cls")
    print("="*5 + " [Menu Login Mahasiswa] " + "="*5 + "\n")
    nim = input("NIM: ")

    # Validasi NIM
    # NIM harus terdaftar untuk masuk (setidaknya 4 NIM akan selalu terdaftar)
    while checkLogin("mahasiswa", nim, "") != True:
        print("NIM yang anda masukkan tidak terdaftar!")
        sleep(1.5)
        system("cls")
        print("="*5 + " [Menu Login Mahasiswa] " + "="*5 + "\n")
        nim = input("NIM: ")

    holder = nim