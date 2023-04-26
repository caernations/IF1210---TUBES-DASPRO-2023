import fungsi_umum

# F06 - JIN PEMBANGUN
def jinPembangun():
    print("hello world")
# F07 - JIN PENGUMPUL
# F08 - BATCH KUMPUL / BANGUN

# F11 - HANCURKAN CANDI
def hancurkanCandi():
    id = input("Masukkan ID candi: ")
    found = False
    for i in range(fungsi_umum.lenarr(fungsi_umum.datacandi)):
        if(fungsi_umum.datacandi[i][0]==id):
            found = True
    if(found):
        print("Apakah anda yakin ingin menghancurkan candi ID:", id, end = " ")
        yakin = input("(Y/N)? ")
        print()
        if(yakin == "Y" or yakin == "y"):
            for i in range(fungsi_umum.lenarr(fungsi_umum.datacandi)):
                if(fungsi_umum.datacandi[i][0]==id):
                    fungsi_umum.datacandi[i] = ""
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Candi gagal dihancurkan")
        
    else:
        print("Tidak ada candi dengan ID tersebut.")