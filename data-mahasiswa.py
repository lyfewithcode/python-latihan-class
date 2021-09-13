import os

from MhsClass.Mahasiswa import *
from MhsClass.ProgramStudi import *

pilih = None   
while(pilih != "0"):
    pilih = input("1.Masukkan data\n2.Tampilkan data\n0.Keluar\nPilihan: ")
    if(pilih == "1"):
        os.system("cls||clear")
        nim = input('Masukan NIM: ')
        nama = input('Masukan Nama: ')
        telepon = input('Masukan No. Telepon: ')
        prodi = input('Masukan Nama Prodi: ')
        kepala_prodi = input('Masukan Nama Kepala Prodi: ')

        nim = int(nim) #nim integer
        telepon = int(telepon) #telepon integer

    elif(pilih == "2"):
        os.system("cls||clear")

        print(f'DATA MAHASISWA\n--------------------\nNIM: {nim} \nNAMA: {nama} \nTELEPON: {telepon} \nPRODI: {prodi} ({kepala_prodi})')

        input("Tekan enter untuk melanjutkan...")
