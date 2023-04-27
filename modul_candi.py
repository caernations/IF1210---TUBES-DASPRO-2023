import fungsi_umum
from os import system
import random

# F06 - JIN PEMBANGUN
def jinPembangun(matriksbahanbangunan, matrikscandi):
    import random
    pasir = 0
    batu = 0
    air = 0
    for i in range(1, fungsi_umum.lenarr(matriksbahanbangunan)):
        if matriksbahanbangunan[i][0] == "pasir":
            pasir += int(matriksbahanbangunan[i][2])
        elif matriksbahanbangunan[i][0] == "batu":
            batu += int(matriksbahanbangunan[i][2])
        elif matriksbahanbangunan[i][0] == "air":
            air += int(matriksbahanbangunan[i][2])
    
    bahan_diperlukan = [random.randint(1,5), random.randint(1,5), random.randint(1,5)]
    nama_bahan = ["pasir", "batu", "air"]

    if pasir < bahan_diperlukan[0] or batu < bahan_diperlukan[1] or air < bahan_diperlukan[2]:
        print("Bahan bangun candi tidak mencukupi")
        print("Candi tidak bisa dibangun!")
    else:
        id_count = fungsi_umum.lenarr(matrikscandi)
        if id_count < 100:
            sisa_candi = 0
            matrikscandi += [[str(id_count), str(f"{fungsi_umum.username}"), str(bahan_diperlukan[0]),str (bahan_diperlukan[1]), str(bahan_diperlukan[2])]]
            for i in range(fungsi_umum.lenarr(bahan_diperlukan)):
                bahan_diperlukan[i]= -bahan_diperlukan[i]
            for i in range(fungsi_umum.lenarr(bahan_diperlukan)):
                matriksbahanbangunan +=[[nama_bahan[i],str(f"dipakai oleh {fungsi_umum.username}"),str(bahan_diperlukan[i])]]
            sisa_candi = 100 - id_count
            print("Candi berhasil dibangun")
            print(f"Sisa candi yang perlu dibangun : {sisa_candi}")
        else:
            for i in range(fungsi_umum.lenarr(bahan_diperlukan)):
                bahan_diperlukan[i]= -bahan_diperlukan[i]
            for i in range(fungsi_umum.lenarr(bahan_diperlukan)):
                matriksbahanbangunan +=[[nama_bahan[i],str(f"dipakai oleh {fungsi_umum.username} (namun candi yang udah dibangun sudah melebihi)"),str(bahan_diperlukan[i])]]
            print("Candi berhasil dibangun")
            print("Sisa candi yang perlu dibangun: 0") 

            
# F07 - JIN PENGUMPUL
def jinPengumpul():
    system('pause')
    system('cls')
    print ("JIN PENGUMPUL\n")

    # Hasil jin pengumpul
    pasirfound = random.randint(0, 5)
    batufound = random.randint(0, 5)
    airfound = random.randint(0, 5)

    # Menambahkan hasil jin pengumpul ke dalam jumlah awal bahan bangunan
    fungsi_umum.intpasir += pasirfound
    fungsi_umum.intbatu += batufound
    fungsi_umum.intair += airfound

    # Assign nilai matriksbahanbangunan
    fungsi_umum.matriksbahanbangunan[0][2] = str(fungsi_umum.intpasir)
    fungsi_umum.matriksbahanbangunan[1][2] = str(fungsi_umum.intbatu)
    fungsi_umum.matriksbahanbangunan[2][2] = str(fungsi_umum.intair)

    print(f"Jin {fungsi_umum.username} menemukan {pasirfound} pasir, {batufound} batu, dan {airfound} air.")
    print(fungsi_umum.matriksbahanbangunan)
    system('pause')
    system('cls')


# F08 - BATCH KUMPUL
def batchKumpul():
    system('pause')
    system('cls')
    print("BATCH KUMPUL\n")
    banyakjinpengumpul = 0
    pasirbatchkumpul = 0
    batubatchkumpul = 0
    airbatchkumpul = 0

    for i in range(fungsi_umum.banyakuser):
        if fungsi_umum.matriksuser[i][2] == "Jin_Pengumpul":
            banyakjinpengumpul += 1

    if banyakjinpengumpul == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {banyakjinpengumpul} jin untuk mengumpulkan bahan.")
        for i in range(banyakjinpengumpul):
            pasirbatchkumpul += random.randint(0, 5)
            batubatchkumpul += random.randint(0, 5)
            airbatchkumpul += random.randint(0, 5)
        
        fungsi_umum.intpasir += pasirbatchkumpul
        fungsi_umum.intbatu += batubatchkumpul
        fungsi_umum.intair += airbatchkumpul

        # Assign nilai matriksbahanbangunan
        fungsi_umum.matriksbahanbangunan[0][2] = str(fungsi_umum.intpasir)
        fungsi_umum.matriksbahanbangunan[1][2] = str(fungsi_umum.intbatu)
        fungsi_umum.matriksbahanbangunan[2][2] = str(fungsi_umum.intair)

        print(f"Jin menemukan total {pasirbatchkumpul} pasir, {batubatchkumpul} batu, dan {airbatchkumpul} air.")
        system('pause')
        system('cls')






# F09 - BATCH BANGUN
def batchBangun(role, matriksuser):
    jin_pembangun = 0
    for i in range(1, fungsi_umum.lenarr(matriksuser)):
        if matriksuser[i][2] == "jin_pembangun":
            jin_pembangun += 1
    print(jin_pembangun)
    if jin_pembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")


# F11 - HANCURKAN CANDI
def hancurkanCandi():
    id = input("Masukkan ID candi: ")
    found = False
    for i in range(fungsi_umum.lenarr(fungsi_umum.matrikscandi)):
        if(fungsi_umum.matrikscandi[i][0]==id):
            found = True
    if(found):
        print("Apakah anda yakin ingin menghancurkan candi ID:", id, end = " ")
        yakin = input("(Y/N)? ")
        print()
        if(yakin == "Y" or yakin == "y"):
            for i in range(fungsi_umum.lenarr(fungsi_umum.matrikscandi)):
                if(fungsi_umum.matrikscandi[i][0]==id):
                    fungsi_umum.matrikscandi[i] = ""
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Candi gagal dihancurkan")
        
    else:
        print("Tidak ada candi dengan ID tersebut.")