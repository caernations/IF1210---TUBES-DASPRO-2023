import fungsi_umum
from os import system

# F09 - AMBIL LAPORAN JIN

# F10 - AMBIL LAPORAN CANDI
def ambilLaporanCandi():
    system('pause')
    system('cls')
    print ("LAPORAN CANDI\n")

    totalpasir = 0 
    totalbatu = 0
    totalair = 0
    hargacanditermahal = 0
    hargacanditermurah = 0
    idcanditermahal = "-"
    idcanditermurah = "-"

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
ID Candi Termahal\t\t: {idcanditermahal}
ID Candi Termurah\t\t: {idcanditermurah}
""")
    system('pause')
    system('cls')