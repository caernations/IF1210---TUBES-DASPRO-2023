import fungsi_umum
from os import system

# F03 - SUMMON JIN
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
        print(f"Tidak ada jin bernomor {nomor_jenis}!\n")
        system('pause')
        system('cls')
        nomor_jenis = input("Masukkan nomor jenis jin yang ingin dipanggil:\n> ")
    if nomor_jenis == "1":
        print("\nMemilih jin 'Pengumpul'\n")
        cek = True
        while cek == True:
            cek = False
            username = input("Masukkan username jin:\n> ")
            for x in fungsi_umum.datauser:
                if(username == x):
                    cek = True
            if(cek == True):
                print(f"\nUsername '{username}' sudah diambil.")

        password = input("Masukkan password jin:\n> ")
        while(fungsi_umum.lenstr(password) < 5 or fungsi_umum.lenstr(password) > 25):
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin: ")
        
        fungsi_umum.writedu("user.csv", username, password, "Jin_Pengumpul")

    else:
        print("Memilih jin “Pembangun”.")
        print()
        cek = True
        while(cek == True):
            cek = False
            username = input("Masukkan username jin: ")
            for x in fungsi_umum.datauser:
                if(username == x):
                    cek = True
            if(cek == True):
                print()
                print(f"Username '{username}' sudah diambil.")
                print()
        password=input("Masukkan password jin: ")
        while(fungsi_umum.lenstr(password) < 5 or fungsi_umum.lenstr(password) > 25):
            print()
            print("Password panjangnya harus 5 - 25 karakter!")
            print()
            password = input("Masukkan password jin: ")
        matriks
        fungsi_umum.writedu("user.csv", username, password, "jin_pembangun")

    print()
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...\n")
    print(f"Jin {username} berhasil dipanggil!")
    system('pause')
    system('cls')


# F04 - HILANGKAN JIN
def hilangkanJin() :
    username = input("Masukkan username jin : ")
    for i in range (1, 100) :
        if fungsi_umum.datauser [i][0] == username :
           konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
           if konfirmasi == "Y" :
               for j in range (4) :
                   fungsi_umum.datauser [i][j] = 0
                   print("Jin telah berhasil dihapus dari alam gaib.")
                   break
           else :
               print("Jin masih belum terhapus")
               break
        else :
            print("Tidak ada jin dengan username tersebut.")


# F05 - UBAH TIPE JIN
def ubahTipeJin():
    username = input("Masukkan username jin : ")
    found = False
    while not found:
        for i in range (fungsi_umum.lenarr(fungsi_umum.datauser)):
            if (fungsi_umum.datauser[i][0] == username):
                found = True
                idx = i
        if not found:
            print("Tidak ada jin dengan username tersebut.")
            username = input("Masukkan username jin : ")

    if(fungsi_umum.datauser[idx][2] == "Jin_Pengumpul"):
        role_awal = "Pengumpul"
        role_akhir = "Pembangun"
    else:
        role_awal = "Pembangun"
        role_akhir = "Pengumpul"
    print("Jin ini bertipe “"+role_awal+"”. Yakin ingin mengubah ke tipe “"+role_akhir+"”")
    jawaban=input("(Y/N)? ")
    print()
    if jawaban == "Y" or jawaban == "y":
        if role_akhir == "Pembangun":
            fungsi_umum.datauser[idx][2] = "Jin_Pembangun"
        else:
            fungsi_umum.datauser[idx][2] = "Jin_Pengumpul"
        print("Jin telah berhasil diubah.")
    else:
        print("Jin gagal diubah")