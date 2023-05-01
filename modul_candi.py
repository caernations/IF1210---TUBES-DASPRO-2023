import fungsi_umum
from os import system
import random

# F06 - JIN PEMBANGUN
# F07 - JIN PENGUMPUL
# F08 - BATCH KUMPUL
# F09 - BATCH BANGUN
# F11 - HANCURKAN CANDI

# F06 - JIN PEMBANGUN
def jinPembangun():
    system('pause')
    system('cls')
    print ("JIN PEMBANGUN\n")

    pasirneeded = random.randint(1, 5)
    batuneeded = random.randint(1, 5)
    airneeded = random.randint(1, 5)

    if (pasirneeded > fungsi_umum.matriksbahanbangunan[0][2]) or (batuneeded > fungsi_umum.matriksbahanbangunan[1][2]) or (airneeded > fungsi_umum.matriksbahanbangunan[2][2]):
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")
    else:
        if fungsi_umum.banyakcandi >= 100:
            print("Candi berhasil dibangun!\nSisa candi yang perlu dibangun: 0")
        else:
            if fungsi_umum.banyakcandi == 0:
                fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [1, fungsi_umum.username, pasirneeded, batuneeded, airneeded], fungsi_umum.banyakcandi)
            else:
                for i in range(fungsi_umum.banyakcandi):
                    if (i == fungsi_umum.banyakcandi - 1):
                        fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [i + 2, fungsi_umum.username, pasirneeded, batuneeded, airneeded], fungsi_umum.banyakcandi)
                    elif (int(fungsi_umum.matrikscandi[i][0]) != int(fungsi_umum.matrikscandi[i + 1][0]) - 1):
                        fungsi_umum.matrikscandi = fungsi_umum.insertlist(fungsi_umum.matrikscandi, i + 1, [i + 2, fungsi_umum.username, pasirneeded, batuneeded, airneeded], fungsi_umum.banyakcandi)
                        break
                
            fungsi_umum.banyakcandi += 1
            print("Candi berhasil dibangun!")
            print(f"Sisa candi yang perlu dibangun: {(100 - fungsi_umum.banyakcandi)}")

        fungsi_umum.matriksbahanbangunan[0][2] -= pasirneeded
        fungsi_umum.matriksbahanbangunan[1][2] -= batuneeded
        fungsi_umum.matriksbahanbangunan[2][2] -= airneeded

    system('pause')
    system('cls')

            
# F07 - JIN PENGUMPUL
def jinPengumpul():
    system('pause')
    system('cls')
    print ("JIN PENGUMPUL\n")

    # Hasil jin pengumpul
    pasirfound = random.randint(0, 5)
    batufound = random.randint(0, 5)
    airfound = random.randint(0, 5)

    # Assign nilai matriksbahanbangunan
    fungsi_umum.matriksbahanbangunan[0][2] += pasirfound
    fungsi_umum.matriksbahanbangunan[1][2] += batufound
    fungsi_umum.matriksbahanbangunan[2][2] += airfound

    print(f"Jin {fungsi_umum.username} menemukan {pasirfound} pasir, {batufound} batu, dan {airfound} air.")
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
        print("Batch kumpul gagal karena Anda tidak memiliki Jin Pengumpul.\nSilahkan summon terlebih dahulu.")
    else:
        print(f"Mengerahkan {banyakjinpengumpul} jin untuk mengumpulkan bahan.")
        for i in range(banyakjinpengumpul):
            pasirbatchkumpul += random.randint(0, 5)
            batubatchkumpul += random.randint(0, 5)
            airbatchkumpul += random.randint(0, 5)
            
        # Assign nilai matriksbahanbangunan
        fungsi_umum.matriksbahanbangunan[0][2] += pasirbatchkumpul
        fungsi_umum.matriksbahanbangunan[1][2] += batubatchkumpul
        fungsi_umum.matriksbahanbangunan[2][2] += airbatchkumpul

        print(f"Jin menemukan total {pasirbatchkumpul} pasir, {batubatchkumpul} batu, dan {airbatchkumpul} air.")

    system('pause')
    system('cls')


# F09 - BATCH BANGUN
def batchBangun():
    system('pause')
    system('cls')
    print("BATCH BANGUN\n")

    banyakjinpembangun = 0
    for i in range(1, fungsi_umum.banyakuser):
        if fungsi_umum.matriksuser[i][2] == "Jin_Pembangun":
            banyakjinpembangun += 1
    if banyakjinpembangun == 0:
        print("Batch bangun gagal karena Anda tidak memiliki Jin Pembangun.\nSilahkan summon terlebih dahulu.")
    else:
        pasirneeded = 0
        batuneeded = 0
        airneeded = 0

        for i in range(banyakjinpembangun):
            pasirneeded += random.randint(1, 5)
            batuneeded += random.randint(1, 5)
            airneeded += random.randint(1, 5)
        print(f"Mengerahkan {banyakjinpembangun} jin untuk membangun candi dengan total bahan {pasirneeded} pasir, {batuneeded} batu, dan {airneeded} air.")
        system('pause')
        system('cls')
        if (pasirneeded > fungsi_umum.matriksbahanbangunan[0][2]) and (batuneeded > fungsi_umum.matriksbahanbangunan[0][2]) and (airneeded > fungsi_umum.matriksbahanbangunan[2][2]):
            print(f"Bangun gagal. Kurang {pasirneeded - fungsi_umum.matriksbahanbangunan[0][2]} pasir, {batuneeded - fungsi_umum.matriksbahanbangunan[1][2]} batu, dan {airneeded - fungsi_umum.matriksbahanbangunan[2][2]} air")
        elif (pasirneeded > fungsi_umum.matriksbahanbangunan[0][2]) and (batuneeded > fungsi_umum.matriksbahanbangunan[0][2]):
            print(f"Bangun gagal. Kurang {pasirneeded - fungsi_umum.matriksbahanbangunan[0][2]} pasir dan {batuneeded - fungsi_umum.matriksbahanbangunan[1][2]} batu")
        elif (pasirneeded > fungsi_umum.matriksbahanbangunan[0][2]) and (airneeded > fungsi_umum.matriksbahanbangunan[2][2]):
            print(f"Bangun gagal. Kurang {pasirneeded - fungsi_umum.matriksbahanbangunan[0][2]} pasir dan {airneeded - fungsi_umum.matriksbahanbangunan[2][2]} air")
        elif (batuneeded > fungsi_umum.matriksbahanbangunan[0][2]) and (airneeded > fungsi_umum.matriksbahanbangunan[2][2]):
            print(f"Bangun gagal. Kurang {batuneeded - fungsi_umum.matriksbahanbangunan[1][2]} batu dan {airneeded - fungsi_umum.matriksbahanbangunan[2][2]} air")
        elif (pasirneeded > fungsi_umum.matriksbahanbangunan[0][2]):
            print(f"Bangun gagal. Kurang {pasirneeded - fungsi_umum.matriksbahanbangunan[0][2]} pasir")
        elif (batuneeded > fungsi_umum.matriksbahanbangunan[0][2]):
            print(f"Bangun gagal. Kurang {batuneeded - fungsi_umum.matriksbahanbangunan[1][2]} batu")
        elif (airneeded > fungsi_umum.matriksbahanbangunan[2][2]):
            print(f"Bangun gagal. Kurang {airneeded - fungsi_umum.matriksbahanbangunan[2][2]} air")
        else:
            if fungsi_umum.banyakcandi > 100:
                print("Candi berhasil dibangun!\nSisa candi yang perlu dibangun: 0")
            else:
                for i in range(1, fungsi_umum.banyakuser):
                    if fungsi_umum.matriksuser[i][2] == "Jin_Pembangun":
                        username = fungsi_umum.matriksuser[i][0]
                        if(fungsi_umum.banyakcandi == 100):
                            break
                        else:
                            if fungsi_umum.banyakcandi == 0:
                                fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [1, username, pasirneeded, batuneeded, airneeded], fungsi_umum.banyakcandi)
                            else:
                                for j in range(fungsi_umum.banyakcandi):
                                    if(j == fungsi_umum.banyakcandi - 1):
                                        fungsi_umum.matrikscandi = fungsi_umum.appendlist(fungsi_umum.matrikscandi, [j+2, username, pasirneeded, batuneeded, airneeded], fungsi_umum.banyakcandi)
                                    elif(int(fungsi_umum.matrikscandi[j][0]) != int(fungsi_umum.matrikscandi[j+1][0]) - 1):
                                        fungsi_umum.matrikscandi = fungsi_umum.insertlist(fungsi_umum.matrikscandi,j+1,[j+2, username, pasirneeded, batuneeded, airneeded],fungsi_umum.banyakcandi)
                                        break
                            fungsi_umum.banyakcandi += 1
            print(f"Jin berhasil membangun total {banyakjinpembangun} candi.")
            fungsi_umum.matriksbahanbangunan[0][2] -= pasirneeded
            fungsi_umum.matriksbahanbangunan[1][2] -= batuneeded
            fungsi_umum.matriksbahanbangunan[2][2] -= airneeded
    system('pause')
    system('cls')


# F11 - HANCURKAN CANDI
def hancurkanCandi():
    system('pause')
    system('cls')
    print("HANCURKAN CANDI\n")
    idhancurkancandi = int(input("Masukkan ID candi:\n>> "))

    found = False

    for i in range (fungsi_umum.banyakcandi):
        if fungsi_umum.matrikscandi[i][0] == str(idhancurkancandi):
            found = True
            break
    if (found):
        konfirmasihancurkancandi = input(f"\nApakah anda yakin ingin menghancurkan candi dengan ID {idhancurkancandi} (Y / N)?\n> ").title()
        system('cls')
        if konfirmasihancurkancandi == "Y":
            fungsi_umum.matrikscandi = fungsi_umum.removelist(fungsi_umum.matrikscandi, i, fungsi_umum.banyakcandi)
            fungsi_umum.banyakcandi -= 1
            print("Candi telah berhasil dihancurkan.")
        else:
            print("Candi gagal dihancurkan.")
    else:
        print("Tidak ada candi dengan ID tersebut.")
    
    system('pause')
    system('cls')