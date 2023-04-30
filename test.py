import fungsi_umum
import modul_jin
import os

modul_jin.summonJin()
# fungsi_umum.matriksbahanbangunan = [['pasir', 'pasir bagus', '5011'], ['batu', 'batu cool', '5014'], ['air', 'air suci', '5011']]
# fungsi_umum.matriksuser = [['Bondowoso', 'cintaroro', 'Bandung_Bondowoso'], ['Roro', 'gasukabondo', 'Roro_Jonggrang'], ['owen', 'owen21', 'Jin_Pembangun'], ['tobias', 'tobias21', 'Jin_Pengumpul'], ['jincakep', 'anjayani', 'Jin_Pembangun'], ['jinganteng', 'cihyu', 'Jin_Pengumpul'], ['', 'jkads', 'Jin_Pengumpul'], ['adsllkad', 'asdaad', 'Jin_Pengumpul'], ['ajdskalksd', '213124', 'Jin_Pembangun']]
# fungsi_umum.matrikscandi = [['1', 'owen', '1', '1', '1'], ['2', 'owen', '5', '5', '5'], ['3', 'jincakep', '1', '2', '3'], [4, 'jincakep', 9, 4, 4], [5, 'owen', 8, 9, 6], [6, 'jincakep', 8, 9, 6], [7, 'owen', 3, 6, 5], [8, 'jincakep', 3, 6, 5], [3, 'owen', 9, 4, 4]]
# fungsi_umum.banyakuser = 9
# fungsi_umum.banyakbahanbangunan = 3
# fungsi_umum.banyakcandi = 9

headermatriksuser = 'username;password;role'
headermatrikscandi = 'id;pembuat;pasir;batu;air'
headermatriksbahanbangunan = 'nama;deskripsi;jumlah'

rowmatriksuser = 3
rowmatrikscandi = 5
rowmatriksbahanbangunan = 3

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

print(fungsi_umum.banyakuser)
print(fungsi_umum.matriksuser)
print(fungsi_umum.matrikscandi)
print(fungsi_umum.matriksbahanbangunan)


fileuser = joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = headermatriksuser)
filecandi = joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = headermatrikscandi)
filebahanbangunan = joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = headermatriksbahanbangunan)

listfile = [fileuser, filecandi, filebahanbangunan]
listfilename = ["user.csv", "candi.csv", "bahanbangunan.csv"]

def save(datas, filename, foldername):
    print(datas)
    print(filename)
    print(foldername)
    folder_path = (f"./save/{foldername}")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Membuat folder save/{foldername} ...")
    file_path = (f"{folder_path}/{filename}")
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(datas)

foldername = input("Masukkan nama folder:\n>>  ")
print(foldername)

print("\nSaving ...\n")
for i in range(3):
    print(listfile[i])
    print()
    save(listfile[i], listfilename[i], foldername)
print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")