import fungsi_umum
from os import system

# F03 - SUMMON JIN
# F04 - HILANGKAN JIN
# F05 - UBAH TIPE JIN



# F03 - SUMMON JIN
def summonJin():
    system('pause')
    system('cls')
    print ("SUMMON JIN\n")

    print("""Jenis Jin yang dapat disummon:
1. Jin Pengumpul - Bertugas mengumpulkan bahan bangunan
2. Jin Pembangun - Bertugas membangun candi\n""")
    nomorjenis = str(input("Masukkan nomor jenis jin yang ingin disummon:\n> "))

    # Cek apakah nomor jenis valid atau tidak
    while not(nomorjenis == "1" or nomorjenis == "2"):
        system('cls')
        print(f"Tidak ada jin bernomor {nomorjenis}!\n")
        system('pause')
        system('cls')

        print("""Jenis Jin yang dapat disummon:
1. Jin Pengumpul - Bertugas mengumpulkan bahan bangunan
2. Jin Pembangun - Bertugas membangun candi\n""")
        nomorjenis = input("Masukkan nomor jenis jin yang ingin disummon:\n> ")

    if nomorjenis == "1":
        system('cls')
        print("Memilih jin 'Pengumpul'\n")
        cek = True

        while cek == True:
            cek = False
            usernamejin = input("Masukkan username jin:\n> ")
            for i in range (fungsi_umum.banyakuser) :
                if fungsi_umum.matriksuser[i][0] == usernamejin :
                    cek = True
            if cek == True:
                print(f"\nUsername '{usernamejin}' sudah diambil.")
                system('pause')
                system('cls')

        password = input("Masukkan password jin:\n> ")
        while(fungsi_umum.lenstr(password) < 5 or fungsi_umum.lenstr(password) > 25):
            system('cls')
            print("Password panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin:\n> ")
        fungsi_umum.matriksuser = fungsi_umum.appendlist(fungsi_umum.matriksuser, [usernamejin, password, "Jin_Pengumpul"], fungsi_umum.banyakuser)
        fungsi_umum.banyakuser += 1

    else:
        system('cls')
        print("Memilih jin 'Pembangun'\n")
        cek = True
        while(cek == True):
            cek = False
            usernamejin = input("Masukkan username jin:\n> ")
            for i in range (fungsi_umum.banyakuser) :
                if fungsi_umum.matriksuser[i][0] == usernamejin :
                    cek = True
            if cek == True:
                print(f"\nUsername '{usernamejin}' sudah diambil.")
                system('pause')
                system('cls')

        password = input("Masukkan password jin:\n> ")
        while(fungsi_umum.lenstr(password) < 5 or fungsi_umum.lenstr(password) > 25):
            system('cls')
            print("Password panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin:\n> ")
        fungsi_umum.matriksuser = fungsi_umum.appendlist(fungsi_umum.matriksuser, [usernamejin, password, "Jin_Pembangun"], fungsi_umum.banyakuser)
        fungsi_umum.banyakuser += 1
        print(fungsi_umum.matriksuser)

    system('pause')
    system('cls')
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...\n")
    system('pause')
    system('cls')
    print(f"Jin '{usernamejin}' berhasil disummon!\n")

    system('pause')
    system('cls')


# F04 - HILANGKAN JIN
def hilangkanJin() :
    system('pause')
    system('cls')
    print ("HILANGKAN JIN\n")

    found = False
    usernamejin = input("Masukkan username jin:\n>> ")
    system('cls')
    for i in range (3, fungsi_umum.banyakuser) :
        if fungsi_umum.matriksuser[i][2] == "Jin_Pengumpul" or fungsi_umum.matriksuser[i][2] == "Jin_Pembangun":
            if fungsi_umum.matriksuser[i][0] == usernamejin:
                found = True
                konfirmasihapusjin = input(f"Apakah anda yakin ingin menghapus jin dengan username '{usernamejin}' (Y / N)?\n> ").title()
                system('cls')
                if konfirmasihapusjin == "Y":
                    fungsi_umum.matriksuser = fungsi_umum.removelist(fungsi_umum.matriksuser, i, fungsi_umum.banyakuser)
                    fungsi_umum.banyakuser -= 1
                    print("Jin telah hilang dari alam gaib.")
                    break
                elif konfirmasihapusjin == "N":
                    print("Jin masih belum terhapus")
                else:
                    print("Invalid command. Please try again.")

    if not found:
        print(f"Tidak ada jin dengan username '{usernamejin}'.")

    system('pause')
    system('cls')


# F05 - UBAH TIPE JIN
def ubahTipeJin():
    system('pause')
    system('cls')
    print("UBAH TIPE JIN\n")

    usernamejin = input("Masukkan username jin:\n>> ")
    found = False
    idx = -1 # inisialisasi idx dengan nilai default apabila username tidak ditemukan

    for i in range(fungsi_umum.banyakuser):
        if fungsi_umum.matriksuser[i][0] == usernamejin:
            found = True
            idx = i
            break 

    if not found:
        print("Tidak ada jin dengan username tersebut.")
        system('pause')
        system('cls')
        return

    if fungsi_umum.matriksuser[idx][2] == "Jin_Pengumpul":
        role_awal = "Pengumpul"
        role_akhir = "Pembangun"
    else:
        role_awal = "Pembangun"
        role_akhir = "Pengumpul"

    konfirmasiubahtipejin = input((f"\nJin ini bertipe '{role_awal}'.\nIngin mengubah ke tipe '{role_akhir}' (Y / N)?\n> ")).title()
    system('cls')

    if konfirmasiubahtipejin == "Y":
        if role_akhir == "Pembangun":
            fungsi_umum.matriksuser[idx][2] = "Jin_Pembangun"
        else:
            fungsi_umum.matriksuser[idx][2] = "Jin_Pengumpul"
        system('cls')
        print("Jin telah berhasil diubah.")
    elif konfirmasiubahtipejin == "N":
        print("Jin gagal diubah")
    else:
        print("Invalid command. Please try again.")

    system('pause')
    system('cls')