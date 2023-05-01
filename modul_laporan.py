import fungsi_umum
from os import system

# F10 - AMBIL LAPORAN JIN
# F11 - AMBIL LAPORAN CANDI


# F10 - AMBIL LAPORAN JIN
def ambilLaporanJin():
    system('pause')
    system('cls')
    print ("LAPORAN JIN\n")

    totaljinpengumpul = 0
    totaljinpembangun = 0
    candiownedterbanyak = 0
    candiownedtersedikit = 100
    jinterajin = '-'
    jintermalas = '-'

    for i in range(fungsi_umum.banyakuser):
        if fungsi_umum.matriksuser[i][2] == "Jin_Pengumpul":
            totaljinpengumpul += 1
        elif fungsi_umum.matriksuser[i][2] == "Jin_Pembangun":
            totaljinpembangun += 1

    for i in range(fungsi_umum.banyakuser):
        if fungsi_umum.matriksuser[i][2] == "Jin_Pembangun":
            candiowned = 0
            for j in range(fungsi_umum.banyakcandi):
                if fungsi_umum.matrikscandi[j][1] == fungsi_umum.matriksuser[i][0]:
                    candiowned += 1
            if candiowned > candiownedterbanyak:
                jinterajin = fungsi_umum.matriksuser[i][0]
                candiownedterbanyak = candiowned
            if candiowned == candiownedterbanyak:
                if fungsi_umum.matriksuser[i][0] < jinterajin:
                    jinterajin = fungsi_umum.matriksuser[i][0]
            if candiowned < candiownedtersedikit:
                jintermalas = fungsi_umum.matriksuser[i][0]
                candiownedtersedikit = candiowned
            if candiowned == candiownedtersedikit:
                if fungsi_umum.matriksuser[i][0] > jintermalas:
                    jintermalas = fungsi_umum.matriksuser[i][0]
            
    print(f"""Total Jin\t\t: {(fungsi_umum.banyakuser - 2)}
Total Jin Pengumpul\t: {totaljinpengumpul}
Total Jin Pembangun\t: {totaljinpembangun}
Jin Terajin\t\t: {jinterajin}
Jin Termalas\t\t: {jintermalas}
Jumlah Pasir\t\t: {fungsi_umum.matriksbahanbangunan[0][2]}
Jumlah Batu\t\t: {fungsi_umum.matriksbahanbangunan[1][2]}
Jumlah Air\t\t: {fungsi_umum.matriksbahanbangunan[2][2]}
""")
    system('pause')
    system('cls')


# F11 - AMBIL LAPORAN CANDI
def ambilLaporanCandi():
    system('pause')
    system('cls')
    print ("LAPORAN CANDI\n")

    totalpasir = 0 
    totalbatu = 0
    totalair = 0
    hargacanditermahal = 0
    hargacanditermurah = 0
    idcanditermahal = '-'
    idcanditermurah = '-'

    for i in range(fungsi_umum.banyakcandi):
        totalpasir += int(fungsi_umum.matrikscandi[i][2])
        totalbatu += int(fungsi_umum.matrikscandi[i][3])
        totalair += int(fungsi_umum.matrikscandi[i][4])
        
        hargacandi = ((10000 * int(fungsi_umum.matrikscandi[i][2])) + (15000 * int(fungsi_umum.matrikscandi[i][3])) + (7500 * int(fungsi_umum.matrikscandi[i][4])))

        if(hargacandi > hargacanditermahal):
            idcanditermahal = fungsi_umum.matrikscandi[i][0]
            hargacanditermahal = hargacandi

        if fungsi_umum.banyakcandi == 1:
            idcanditermurah = fungsi_umum.matrikscandi[1][0]
            hargacanditermurah = hargacandi
        
        else:
            if (idcanditermurah == "-") or (hargacandi < hargacanditermurah):
                idcanditermurah = fungsi_umum.matrikscandi[i][0]
                hargacanditermurah = hargacandi

    print(f"""Total Candi\t\t\t: {fungsi_umum.banyakcandi}
Total Pasir yang Digunakan\t: {totalpasir}
Total Batu yang Digunakan\t: {totalbatu}
Total Air yang Digunakan\t: {totalair}
ID Candi Termahal\t\t: {idcanditermahal} (Rp {format(hargacanditermahal, ',').replace(',', '.')})
ID Candi Termurah\t\t: {idcanditermurah} (Rp {format(hargacanditermurah, ',').replace(',', '.')})
""")
    system('pause')
    system('cls')