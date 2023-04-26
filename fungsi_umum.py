def lenstr(length):
    # Fungsi untuk menghitung panjang string
    if length == '':
        return 0
    else:
        return 1 + lenstr(length[1:])


def appendlist(list1, elemen):
    list2 = [0 for i in range (lenarr + 1)]
    for i in range (lenarr):
        list2[i] = list1[i]
    list2[lenarr] = elemen
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

    
def importcsv(filename, delimeter = ';'):
    # Fungsi Untuk membaca file CSV
    file = open(f'./save/default/{filename}', 'r')
    dataframe = []
    row = 0
    file.readline()
    for line in file:
        dataframe += [splitstr(line.replace('\n', ''), delimeter)]
        row += 1
    file.close()
    return dataframe


# matriksuser = importcsv('user.csv', delimeter=";")
# matrikscandi = importcsv('user.csv', delimeter=";")
# matriksbahanbangunan = importcsv('user.csv', delimeter=";")

# usercsv = importcsv('user.csv', delimeter=";")
# datauser = importcsv('user.csv', delimeter=";")
# datacandi = importcsv('user.csv', delimeter=";")

def writedu(filename, username, password, role):
    # Fungsi untuk menulis di datauser
    file = open(filename,'a')
    file.write("\n" + username + ";" + password + ";" + role)
    file.close()

def tuliscsv(filename, data):
    if filename == "user.csv":
        idx2 = 3
    elif filename== "candi.csv":
        idx2 = 5
    file=open(filename,'w')
    for i in range(lenstr(data)):
        for j in range(idx2):
            if(data[i]==""):
                continue
            else:
                file.write(data[i][j])
                if(j != idx2 -1):
                    file.write(";")
                else:
                    file.write("\n")
    file.close()
