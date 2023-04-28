import fungsi_umum
from os import system
import random

# F06 - JIN PEMBANGUN
def jinPembangun():
    system('pause')
    system('cls')
    print ("JIN PEMBANGUN\n")

    pasirneeded = random.randint(1, 5)
    batuneeded = random.randint(1, 5)
    airneeded = random.randint(1, 5)
    
    if (pasirneeded > fungsi_umum.intpasir) or (batuneeded > fungsi_umum.intpasir) or (airneeded > fungsi_umum.intair):
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
    else:
        if fungsi_umum.banyakcandi > 100:
            print("Candi berhasil dibangun!\nSisa candi yang perlu dibangun: 0")
        else:
            fungsi_umum.banyakcandi += 1
            print("Candi berhasil dibangun!")
            print(f"Sisa candi yang perlu dibangun: {(100 - fungsi_umum.banyakcandi)}")
            cnt = 1
            cek = False
            for x in range(fungsi_umum.banyakcandi):
                if fungsi_umum.matrikscandi[x][0] != str(x + 1):
                    fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [cnt, fungsi_umum.username, pasirneeded, batuneeded, airneeded], (fungsi_umum.banyakcandi))
                    fungsi_umum.banyakcandi += 1
                    cek = True
                    break
                else:
                    cnt += 1
            if not cek :
                fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [cnt, fungsi_umum.username, pasirneeded, batuneeded, airneeded], (fungsi_umum.banyakcandi))
        print(fungsi_umum.matrikscandi)

        fungsi_umum.intpasir -= pasirneeded
        fungsi_umum.intbatu -= batuneeded
        fungsi_umum.intair -= airneeded

        fungsi_umum.matriksbahanbangunan[0][2] = str(fungsi_umum.intpasir)
        fungsi_umum.matriksbahanbangunan[1][2] = str(fungsi_umum.intbatu)
        fungsi_umum.matriksbahanbangunan[2][2] = str(fungsi_umum.intair)

            
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
        print(fungsi_umum.matriksbahanbangunan)
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
    system('pause')
    system('cls')
    print("HANCURKAN CANDI\n")
    idhancurkancandi = input("Masukkan ID candi:\n> ")

    found = False
    for i in range (fungsi_umum.banyakcandi):
        if (fungsi_umum.matrikscandi[i][0] == idhancurkancandi):
            found = True
    if (found):
        konfirmasihancurkancandi = input("Apakah anda yakin ingin menghancurkan candi dengan ID {idhancurkancandi} (Y / N)?\n> ").title()
        if konfirmasihancurkancandi == "Y":
            for i in range (fungsi_umum.banyakcandi):
                if (fungsi_umum.matrikscandi[i][0] == idhancurkancandi):
                    fungsi_umum.removelist(fungsi_umum.matrikscandi, idhancurkancandi, fungsi_umum.banyakcandi)
            print("Candi telah berhasil dihancurkan.")
            print(fungsi_umum.matrikscandi)
        else:
            print("Candi gagal dihancurkan")
    else:
        print("Tidak ada candi dengan ID tersebut.")