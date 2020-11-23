import csv

# Program LoadSave
# Program yang berisikan function dan procedure yang berguna untuk mengambil data dari
# file pada folder Data ataupun menyimpan data pada Folder data

# ALGORITMA
def load(type): # Function untuk membantu menginisiasi list sesuai tipe
    temp = []
    # Data yang akan di load, akan mengikuti tipe yang diinput
    if type == "Mahasiswa" or type == "Admin":
        with open('Data/User.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == type:
                    temp.append(row[:3])
    elif type == "buku":
        with open('Data/Buku.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                temp.append(row)
    elif type == "bukupinjam":
        with open('Data/Pinjaman.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                temp.append(row)
    elif type == "denda":
        with open('Data/Denda.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                temp.append(row)
    elif type == "bukuhistory":
        with open('Data/History.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                temp.append(row)
    return temp

def loadUser(search): # Function untuk mendapatkan data user (mahasiswa)
    with open('Data/User.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search:
                return row[:3] # Data tipe user (Mahasiswa ataupun Admin) tidak diikut sertakan

def getDenda(search): # Function untuk mendapatkan denda sesuai dengan search (nim)
    with open('Data/Denda.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search:
                return row[1] # Denda

def save(type, fl): # Procedure untk menyimpan data pada file csv
    # Penyimpanan data menyesuaikan dengan tipe yang dimasukkan
    if type == "buku":
        with open('Data/Buku.csv', 'w', newline='') as csvfile:
            savean = csv.writer(csvfile, delimiter=',')
            for i in range(len(fl)):
                savean.writerow(fl[i])
    elif type == "bukupinjam":
        with open('Data/Pinjaman.csv', 'w', newline='') as csvfile:
            savean = csv.writer(csvfile, delimiter=',')
            for i in range(len(fl)):
                savean.writerow(fl[i])
    elif type == "bukuhistory":
        with open('Data/History.csv', 'w', newline='') as csvfile:
            savean = csv.writer(csvfile, delimiter=',')
            for i in range(len(fl)):
                savean.writerow(fl[i])
    elif type == "denda":
        with open('Data/Denda.csv', 'w', newline='') as csvfile:
            savean = csv.writer(csvfile, delimiter=',')
            for i in range(len(fl)):
                savean.writerow(fl[i])