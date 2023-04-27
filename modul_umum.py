import fungsi_umum
import modul_jin
import modul_candi
import modul_laporan
import os
from os import system
from datetime import datetime as dt
import fungsi_umum

# F02 - LOGOUT
# F12 - AYAM BERKOKOK
# F13 - LOAD
# F14 - SAVE
# F16 - EXIT
# F02 - LOGOUT

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
    print("Kukuruyuk.. Kukuruyuk..")
    print()
    jumlahcandi=-1
    for i in range(fungsi_umum.lenstr(fungsi_umum.matrikscandi)):
        if(fungsi_umum.matrikscandi!=""):
            jumlahcandi+=1
    if(jumlahcandi<=100):
        print("jumlah candi:",jumlahcandi)
        print()
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print()
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("jumlah candi:",jumlahcandi)
        print()
        print("Yah, Bandung Bondowoso memenangkan permainan!")

# F15 - help
def help(role):
    if role == "Bandung_Bondowoso":
        while True:
            print("1. Summon Jin\n2. Hilangkan Jin\n3. Ubah Tipe Jin\n4. Batch Kumpul\n5. Batch Bangun\n6. Ambil Laporan Jin\n7. Ambil Laporan Candi\n8. Logout")
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
                modul_laporan.ambilLaporanCandi
            elif command == "8" or command == "Logout":
                logout()
                break
            elif command == "Login":
                system('cls')
                print("Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")
                system('pause')
                system('cls')

    elif role == "Roro_Jonggrang":
        while True:
            print("1. Hancurkan Candi\n2. Ayam Berkokok\n3. Logout")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Hancurkan Candi":
                modul_candi.hancurkanCandi()
            elif command == "2" or command == "Ayam Berkokok":
                ayamBerkokok()
            elif command == "3" or command == "Logout":
                logout()
                break
            elif command == "Login":
                system('cls')
                print("Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")

    elif role == "Jin_Pengumpul":
        while True:
            print("1. Jin Pengumpul\n2. Logout")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Jin Pengumpul":
                modul_jin.jinPengumpul()
            elif command == "2" or command == "Logout":
                logout()
                break
            elif command == "Login":
                system('cls')
                print("Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")

    elif role == "Jin_Pembangun":
        while True:
            print("1. Jin Pembangun\n2. Logout")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Jin Pembangun":
                modul_jin.jinPembangun()
            elif command == "2" or command == "Logout":
                logout()
                break
            elif command == "Login":
                system('cls')
                print("Login gagal!\nAnda telah login dengan username {fungsi_umum.username}, silahkan lakukan 'logout' sebelum melakukan login kembali.")
                system('pause')
                system('cls')
            else:
                print("Invalid command, please try again.")

    elif role == None:
        while True:
            print("1. Login\n2. Exit\n3. Save\n4. Logout")
            command = str(input("\nPlease type a command:\n>> ")).title()
            if command == "1" or command == "Login":
                login()
            elif command == "2 " or command == "Exit":
                print("anjay2")
                exit()
            elif command == "3" or command == "Save":
                print("anjay3")
            elif command == "4" or command == "Logout":
                logout()
                break
            else:
                print("Invalid command, please try again.")