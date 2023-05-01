from os import system
import modul_umum
import fungsi_umum
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder", nargs="?")
args = parser.parse_args()
if args.folder is None:
    parser.error("Tidak ada nama folder yang diberikan!")
else:
    path = args.folder
    if not (os.path.isdir(f'./save/{path}')):
        parser.error(f"Folder {path} tidak ditemukan!")
    else:
        fungsi_umum.matriksuser, fungsi_umum.banyakuser = fungsi_umum.importcsv(path, 'user.csv')
        fungsi_umum.matrikscandi, fungsi_umum.banyakcandi = fungsi_umum.importcsv(path, 'candi.csv')
        fungsi_umum.matriksbahanbangunan, fungsi_umum.banyakbahanbangunan = fungsi_umum.importcsv(path, 'bahan_bangunan.csv')

role = None
while True:
    print("Welcome to Roro Jonggrang & Bandung Bondowoso's Adventure Game!")
    modul_umum.help(None)