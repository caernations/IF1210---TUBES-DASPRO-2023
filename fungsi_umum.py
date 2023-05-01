def lenstr(length):
    # Fungsi untuk menghitung panjang string
    if length == '':
        return 0
    else:
        return 1 + lenstr(length[1:])


def appendlist(list1, elemen, lenlist1):
    list2 = [0 for i in range (lenlist1 + 1)]
    for i in range (lenlist1):
        list2[i] = list1[i]
    list2[lenlist1] = elemen
    return list2


def removelist(list1, indeks, lenlist1):
    list2 = [0 for i in range (lenlist1 - 1)]
    for i in range (lenlist1):
        if i == int(indeks):
            continue
        if i > int(indeks):
            list2 = appendlist(list2, list1[i], i-1)
        else:
            list2 = appendlist(list2, list1[i], i)
    return list2

def insertlist(list1, indeks, elemen, lenlist1):
    list2 = [0 for i in range(lenlist1 + 1)]
    for i in range(lenlist1 + 1):
        if i < indeks:
            list2[i] = list1[i]
        elif i == indeks:
            list2[indeks] = elemen 
        else:
            list2[i] = list1[i - 1] 
    return list2


def lenarr(arr):
    # Fungsi untuk menghitung panjang array
    length = 0
    i = 1
    while i < len(arr):
        length += 1
        i += 1
    return length
    

def splitstr(str, sep):
    # Fungsi split()
    str1 = ""
    list1 = []
    for i in str:
        if(i != sep):
            str1 = str1 + i
        else:
            list1 = list1 + [str1]
            str1 = ""
    if(str1 != ""):
        list1 = list1 + [str1]
    return list1

    
def importcsv(folder, filename, delimeter = ';'):
    # Fungsi Untuk membaca file CSV
    file = open(f'./save/{folder}/{filename}', 'r')
    dataframe = []
    row = 0
    file.readline()
    for line in file:
        dataframe += [splitstr(line.replace('\n', ''), delimeter)]
        row += 1
    file.close()
    return dataframe, row


def joinstr(matriks, lenmatriks, rowmatriks, separator=';', header = ''):
    strmatriks = header + '\n' if header else ''

    for i in range(lenmatriks):
        for j in range(rowmatriks):
            if j > 0:
                strmatriks += separator
            strmatriks += str(matriks[i][j])
        if i < lenmatriks - 1:
            strmatriks += '\n'
    return strmatriks


# VARIABLE
username = None
matriksuser, banyakuser = importcsv('default', 'user.csv', delimeter=";")
matrikscandi, banyakcandi = importcsv('default', 'candi.csv', delimeter=";")
matriksbahanbangunan, banyakbahanbangunan = importcsv('default','bahan_bangunan.csv', delimeter=";")

matriksbahanbangunan[0][2] = int(matriksbahanbangunan[0][2])
matriksbahanbangunan[1][2] = int(matriksbahanbangunan[1][2])
matriksbahanbangunan[2][2] = int(matriksbahanbangunan[2][2])

headermatriksuser = 'username;password;role'
headermatrikscandi = 'id;pembuat;pasir;batu;air'
headermatriksbahanbangunan = 'nama;deskripsi;jumlah'

rowmatriksuser = 3
rowmatrikscandi = 5
rowmatriksbahanbangunan = 3