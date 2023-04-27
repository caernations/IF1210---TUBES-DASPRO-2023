import fungsi_umum

# F09 - AMBIL LAPORAN JIN

# F10 - AMBIL LAPORAN CANDI
def ambilLaporanCandi():
    candi = 0
    pasir = 0
    batu = 0
    air = 0
    termahal = 0
    termurah = -1
    id_termahal = "-"
    id_termurah = "-"
    for i in range(1, fungsi_umum.lenarr(fungsi_umum.matrikscandi)):
        candi += 1
        pasir += int(fungsi_umum.matrikscandi[i][2])
        batu += int(fungsi_umum.matrikscandi[i][3])
        air += int(fungsi_umum.matrikscandi[i][4])
        harga = (10000 * int(fungsi_umum.matrikscandi[i][2]) + 15000 * int(fungsi_umum.matrikscandi[i][3]) + 7500 * int(fungsi_umum.matrikscandi[i][4]))
        if(harga > termahal):
            id_termahal = fungsi_umum.matrikscandi[i][0]
            termahal = harga
        if(harga < termurah or termurah == -1):
            id_termurah = fungsi_umum.matrikscandi[i][0]
            termurah = harga
    print("Total Candi: " + str(candi))
    print("Total Pasir yang digunakan: "+str(pasir))
    print("Total Batu yang digunakan: "+str(batu))
    print("Total Air yang digunakan: "+str(air))
    print("ID Candi Termahal: "+id_termahal)
    print("ID Candi Termurah: "+id_termurah)