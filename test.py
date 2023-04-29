import fungsi_umum
import os

fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser)
filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi)
filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan)

listfile = [fileuser, filecandi, filebahanbangunan]
listfilename = ["user.csv", "candi.csv", "bahanbangunan.csv"]

def save(data, filename, foldername):
    global folder_path
    folder_path = f"./save/{foldername}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Membuat folder save/{foldername} ...")
    file_path = f"{folder_path}/{filename}"
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(data)

foldername = input("Masukkan nama folder:\n>>  ")
print("Saving ...")
for i in range(3):
    save(listfile[i], listfilename[i], foldername)
print(f"Berhasil menyimpan data di folder save/{foldername}.")
