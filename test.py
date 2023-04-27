from os import system
import fungsi_umum


def summonJin():
    system('pause')
    system('cls')
    print ("SUMMON JIN\n")
    print("""Jenis Jin yang dapat dipanggil:
1. Jin Pengumpul - Bertugas mengumpulkan bahan bangunan
2. Jin Pembangun - Bertugas membangun candi\n""")
    nomor_jenis = str(input("Masukkan nomor jenis jin yang ingin dipanggil:\n> "))
    # Cek apakah nomor jenis valid atau tidak
    while not(nomor_jenis == "1" or nomor_jenis == "2"):
        system('cls')
        print(f"Tidak ada jin bernomor {nomor_jenis}!\n")
        system('pause')
        system('cls')
        print("""Jenis Jin yang dapat dipanggil:
1. Jin Pengumpul - Bertugas mengumpulkan bahan bangunan
2. Jin Pembangun - Bertugas membangun candi\n""")
        nomor_jenis = input("Masukkan nomor jenis jin yang ingin dipanggil:\n> ")
    if nomor_jenis == "1":
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
            system('pause')
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
            system('pause')
            system('cls')
            print("Password panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin:\n> ")
        fungsi_umum.matriksuser = fungsi_umum.appendlist(fungsi_umum.matriksuser, [usernamejin, password, "Jin_Pembangun"], fungsi_umum.banyakuser)
        fungsi_umum.banyakuser += 1

    system('pause')
    system('cls')
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...\n")
    system('pause')
    system('cls')
    print(f"Jin {usernamejin} berhasil dipanggil!\n")
    system('pause')
    system('cls')