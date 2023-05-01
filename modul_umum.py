import fungsi_umum
import modul_jin
import modul_candi
import modul_laporan
import os
import argparse
from os import system

# F01 - LOGIN
# F02 - LOGOUT
# F12 - AYAM BERKOKOK
# F14 - LOAD
# F15 - SAVE
# F16 - HELP
# F17 - EXIT

# F01 - LOGIN
def login():
    while True:
        system('pause')
        system('cls')
        print("LOGIN PAGE\n")
        fungsi_umum.username = input("Username: ")
        password = input("Password: ")
        user_exist = False
        
        for user in fungsi_umum.matriksuser:
            if user[0] == fungsi_umum.username:
                user_exist = True
                if user[1] == password:
                    system('pause')
                    system('cls')
                    print(f"Selamat datang, {fungsi_umum.username}!")
                    role = user[2]
                    if role == "Bandung_Bondowoso":
                        help("Bandung_Bondowoso")
                    elif role == "Roro_Jonggrang":
                        help("Roro_Jonggrang")
                    elif role == "Jin_Pengumpul":
                        help("Jin_Pengumpul")
                    elif role == "Jin_Pembangun":
                        help("Jin_Pembangun")
                    return role
                else:
                    print("Password salah!")
                    break

        if not user_exist:
            print("Username tidak terdaftar!")


# F02 - LOGOUT
def logout():
    if fungsi_umum.username == None:
        system('cls')
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        system('pause')
        system('cls')
    else:
        system('cls')
        print("Anda berhasil logout dari akun.")
        fungsi_umum.username = None
        system('pause')
        system('cls')


# F12 - AYAM BERKOKOK
def ayamBerkokok():
    system('pause')
    system('cls')
    print("AYAM BERKOKOK\n")

    print("Kukuruyuk..! Kukuruyuk..!")
    print("Kukuruyuk..! Kukuruyuk..!")
    print("Kukuruyuk..! Kukuruyuk..!\n")
    print(f"Jumlah Candi: {fungsi_umum.banyakcandi}\n")
    system('pause')
    system('cls')
    
    if(fungsi_umum.banyakcandi < 100):
        print("""Selamat, Roro Jonggrang memenangkan permainan!\n*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.\n""")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!\n")
        exit()
    system('pause')
    system('cls')
    exit()


# F14 - SAVE
def save(data, filename, foldername):
    folder_path = f"./save/{foldername}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"Membuat folder save/{foldername} ...")
    file_path = f"{folder_path}/{filename}"
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w') as f:
        f.write(data)


# F16 - HELP
def help(role):
    if role == "Bandung_Bondowoso":
        while True:
            print("1. Summon Jin\n2. Hilangkan Jin\n3. Ubah Tipe Jin\n4. Batch Kumpul\n5. Batch Bangun\n6. Ambil Laporan Jin\n7. Ambil Laporan Candi\n8. Save\n9. Logout\n10. Exit")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Summon Jin":
                modul_jin.summonJin()
            elif command == "2" or command == "Hilangkan Jin":
                modul_jin.hilangkanJin()
            elif command == "3" or command == "Ubah Tipe Jin":
                modul_jin.ubahTipeJin()
            elif command == "4" or command == "Batch Kumpul":
                modul_candi.batchKumpul()
            elif command == "5" or command == "Batch Bangun":
                modul_candi.batchBangun()
            elif command == "6" or command == "Ambil Laporan Jin":
                modul_laporan.ambilLaporanJin()
            elif command == "7" or command == "Ambil Laporan Candi":
                modul_laporan.ambilLaporanCandi()
            elif command == "8" or command == "Save":
                fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
                filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
                filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
                listfile = [fileuser, filecandi, filebahanbangunan]
                listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
                system('pause')
                system('cls')
                foldername = input("Masukkan nama folder:\n>>  ")
                print("\nSaving ...\n")
                system('pause')
                system('cls')
                for i in range(3):
                    save(listfile[i], listfilename[i], foldername)
                print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
                system('pause')
                system('cls')
            elif command == "9" or command == "Logout":
                logout()
                break
            elif command == "10" or command == "Exit":
                exitprogram()
            elif command == "Login":
                system('cls')
                print(f"Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')

    elif role == "Roro_Jonggrang":
        while True:
            print("1. Hancurkan Candi\n2. Ayam Berkokok\n3. Save\n4. Logout\n5. Exit")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Hancurkan Candi":
                modul_candi.hancurkanCandi()
            elif command == "2" or command == "Ayam Berkokok":
                ayamBerkokok()
            elif command == "3" or command == "Save":
                fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
                filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
                filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
                listfile = [fileuser, filecandi, filebahanbangunan]
                listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
                system('pause')
                system('cls')
                foldername = input("Masukkan nama folder:\n>>  ")
                print("\nSaving ...\n")
                system('pause')
                system('cls')
                for i in range(3):
                    save(listfile[i], listfilename[i], foldername)
                print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
                system('pause')
                system('cls')
            elif command == "4" or command == "Logout":
                logout()
                break
            elif command == "5" or command == "Exit":
                exitprogram()
            elif command == "Login":
                system('cls')
                print(f"Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Jin":
                system('cls')
                print("Laporan Jin hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Candi":
                system('cls')
                print("Laporan Candi hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')

    elif role == "Jin_Pengumpul":
        while True:
            print("1. Jin Pengumpul\n2. Save\n3. Logout\n4. Exit")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Jin Pengumpul":
                modul_candi.jinPengumpul()
            elif command == "2" or command == "Save":
                fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
                filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
                filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
                listfile = [fileuser, filecandi, filebahanbangunan]
                listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
                system('pause')
                system('cls')
                foldername = input("Masukkan nama folder:\n>>  ")
                print("\nSaving ...\n")
                system('pause')
                system('cls')
                for i in range(3):
                    save(listfile[i], listfilename[i], foldername)
                print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
                system('pause')
                system('cls')
            elif command == "3" or command == "Logout":
                logout()
                break
            elif command == "4" or command == "Exit":
                exitprogram()
            elif command == "Login":
                system('cls')
                print(f"Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Jin":
                system('cls')
                print("Laporan Jin hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Candi":
                system('cls')
                print("Laporan Candi hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')

    elif role == "Jin_Pembangun":
        while True:
            print("1. Jin Pembangun\n2. Save\n3. Logout\n4. Exit")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Jin Pembangun":
                modul_candi.jinPembangun()
            elif command == "2" or command == "Save":
                fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
                filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
                filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
                listfile = [fileuser, filecandi, filebahanbangunan]
                listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
                system('pause')
                system('cls')
                foldername = input("Masukkan nama folder:\n>>  ")
                print("\nSaving ...\n")
                system('pause')
                system('cls')
                for i in range(3):
                    save(listfile[i], listfilename[i], foldername)
                print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
                system('pause')
                system('cls')
            elif command == "3" or command == "Logout":
                logout()
                break
            elif command == "4" or command == "Exit":
                exitprogram()
            elif command == "Login":
                system('cls')
                print(f"Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Jin":
                system('cls')
                print("Laporan Jin hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            elif command == "Ambil Laporan Candi":
                system('cls')
                print("Laporan Candi hanya dapat diakses oleh akun Bandung Bondowoso")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')

    elif role == None:
        while True:
            print("1. Login\n2. Exit\n3. Save\n4. Logout")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Login":
                login()
            elif command == "2 " or command == "Exit":
                exitprogram()
            elif command == "3" or command == "Save":
                fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
                filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
                filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
                listfile = [fileuser, filecandi, filebahanbangunan]
                listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
                system('pause')
                system('cls')
                foldername = input("Masukkan nama folder:\n>>  ")
                print("\nSaving ...\n")
                system('pause')
                system('cls')
                for i in range(3):
                    save(listfile[i], listfilename[i], foldername)
                print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
                system('pause')
                system('cls')
            elif command == "4" or command == "Logout":
                logout()
                break
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')


# F17 - EXIT
def exitprogram():
    system('pause')
    system('cls')
    print("EXIT\n")

    while True:
        wanttosave = str(input("Apakah Anda ingin melakukan penyimpanan file yang sudah diubah? (Y / N )\n>> ")).title()
        if wanttosave == "Y":
            fileuser = fungsi_umum.joinstr(fungsi_umum.matriksuser, fungsi_umum.banyakuser, rowmatriks = 3, header = fungsi_umum.headermatriksuser)
            filecandi = fungsi_umum.joinstr(fungsi_umum.matrikscandi, fungsi_umum.banyakcandi, rowmatriks = 5, header = fungsi_umum.headermatrikscandi)
            filebahanbangunan = fungsi_umum.joinstr(fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan, rowmatriks = 3, header = fungsi_umum.headermatriksbahanbangunan)
            listfile = [fileuser, filecandi, filebahanbangunan]
            listfilename = ["user.csv", "candi.csv", "bahan_bangunan.csv"]
            system('pause')
            system('cls')
            foldername = input("Masukkan nama folder:\n>>  ")
            print("\nSaving ...\n")
            system('pause')
            system('cls')
            for i in range(3):
                save(listfile[i], listfilename[i], foldername)
            print(f"Berhasil menyimpan data di folder 'save/{foldername}'!\n")
            system('pause')
            system('cls')
            exit()
        elif wanttosave == "N":
            # system('pause')
            # system('cls')
            exit()
        else:
            system('cls')
            continue