# Program BookChecker
# Program yang berisikan function-function keperluan pada program BookAdmin dan BookMh
# Penjelasan setiap function ada pada masing-masing function

# ALGORITMA
def getBukuSingle(listBuku, judul, penulis, penerbit, tahun): # Function untuk mendapatkan satu index buku dengan data tertentu dari listbuku
    if listBuku != None:
        for i in range(len(listBuku)):
            if (listBuku[i][1].lower() == judul.lower()) and (listBuku[i][2].lower() == penulis.lower()) and (listBuku[i][3].lower() == penerbit.lower()) and (listBuku[i][4] == tahun):
                return i
    return None

def getBukuMultiple(listBuku, type, search): # Function untuk mendapatkan multiple index yang sesuai dengan type dan search
    temp = []
    if listBuku != None:
        for i in range(len(listBuku)):
            # Menyesuaikan pencarian sesuai dengan type masukan
            if type == "id":
                if search.lower() == listBuku[i][0].lower():
                    temp.append(i)
            if type == "judul":
                if search.lower() in listBuku[i][1].lower():
                    temp.append(i)
            if type == "penulis":
                if search.lower() in listBuku[i][2].lower():
                    temp.append(i)
            if type == "penerbit":
                if search.lower() in listBuku[i][3].lower():
                    temp.append(i)
            if type == "tahun":
                if search.lower() in listBuku[i][4]:
                    temp.append(i)
    return temp

def getBukuPinjaman(listBukuPinjam, nim): # Function untuk mendapatkan data buku yang mengandung nim masukan
    temp = []
    if listBukuPinjam != None:
        for i in range(len(listBukuPinjam)):
            if listBukuPinjam[i][6] == nim:
                temp.append(listBukuPinjam[i])
    return temp

def getBukuHistory(listBukuHistory, nim): # Function untuk mendapatkan data buku yang mengandung nim
    temp = []
    if listBukuHistory != None:
        for i in range(len(listBukuHistory)):
            if listBukuHistory[i][8] == nim:
                temp.append(listBukuHistory[i])
    return temp

def getIndexBukuPinjaman(listBukuPinjam, nim): # Function untuk mendapatkan index buku
    temp = []
    if listBukuPinjam != None:
        for i in range(len(listBukuPinjam)):
            if listBukuPinjam[i][6] == nim:
                temp.append(i)
    return temp

def getJumlahBuku(listBuku, id): # Function untuk mengecek apa jumlah buku > 0
    if listBuku != None:
        for i in range(len(listBuku)):
            if listBuku[i][0].lower() == id.lower():
                if int(listBuku[i][5]) > 0:
                    return True # Jumlah > 0
    return False

def dateStripper(date): # Function untuk menghilangkan angka 0 di depan angka
    temp = date.split('/')
    for i in range(len(temp)):
        temp[i] = temp[i].lstrip('0')
    temp = "%s/%s/%s" % (temp[0], temp[1], temp[2])
    return temp

def dateValidation(date): # Function untuk memvalidasi tanggal
    from datetime import datetime
    try: # Mengantisipasi ValueError agar tidak mengeluarkan default error message
        datetime.strptime(date, '%d/%m/%Y')
    except ValueError: # Jika format tidak sesuai, akan mereturn False
        return False
    return True

def countDenda(listBukuPinjam, date, idx): # Function untuk menghitung banyak denda
    from datetime import datetime
    temp = listBukuPinjam[idx][8] # Mendapatkan tanggal, sesuai idx yang telah diinput
    d1 = datetime.strptime(temp, "%d/%m/%Y") # Tanggal Pinjam
    d2 = datetime.strptime(date, "%d/%m/%Y") # Tanggal Kembali
    delta = abs(d2-d1).days
    return int(delta/14)*10000

def getIndexDenda(listDenda, nim): # Function untuk mendapatkan index dengan yang sesuai dengan nim
    if listDenda != None:
        for i in range(len(listDenda)):
            if listDenda[i][0] == nim:
                return i
    return None # Tidak terdapat datanya