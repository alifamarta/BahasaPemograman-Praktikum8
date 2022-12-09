class Mahasiswa:
    nama = ""
    nim = ""
    uts = ""
    uas = ""
    tugas = ""
    akhir = ""

DataMhs = []

def add():
    Mhs = Mahasiswa()
    print("TAMBAH DATA")

    Mhs.nama = input("Nama        : ")
    Mhs.nim  = input("NIM         : ")
    Mhs.tugas = int(input("Nilai Tugas : "))
    Mhs.uts = int(input("Nilai UTS   : "))
    Mhs.uas = int(input("Nilai UAS   : "))
    Mhs.akhir = (Mhs.tugas * 30/100) + (Mhs.uts * 35/100) + (Mhs.uas * 35/100)

    DataMhs.append(Mhs)

def show():
    if len(DataMhs) <= 0:
        print("\n")
        print("      DAFTAR NILAI MAHASISWA")
        print("=================================")
        print("         TIDAK ADA DATA")
    
    else:
        for Mhs in DataMhs:
            print("\n")
            print("      DAFTAR NILAI MAHASISWA")
            print("=================================")
            print("Nama        : {} ".format(Mhs.nama))
            print("NIM         : {} ".format(Mhs.nim))
            print("Nilai Tugas : {} ".format(Mhs.tugas))
            print("Nilai UTS   : {} ".format(Mhs.uts))
            print("Nilai UAS   : {} ".format(Mhs.uas))
            print("Nilai Akhir : {:.1f} ".format(Mhs.akhir))

def delete():
    print("HAPUS DATA")
    nama = Mahasiswa()
    nama = input("Nama : ")
    for a in DataMhs:
        if nama == a.nama:
            DataMhs.remove(a)

            print("Berhasil Dihapus")
    
        else:
            print("DATA TIDAK DITEMUKAN")

def update():
    print("UBAH DATA")
    nama = Mahasiswa()
    nama = input("Nama : ")
    print("\n")

    for a in DataMhs:
        if nama == a.nama:
            a.tugas = int(input("Nilai Tugas : "))
            a.uts = int(input("Nilai UTS   : "))
            a.uas = int(input("Nilai UAS   : "))
            a.akhir = (a.tugas * 30/100) + (a.uts * 35/100) + (a.uas * 35/100)

        else:
            print("DATA TIDAK DITEMUKAN")

while True:
    print("\n")
    print("==========================")
    print("    Program Input Nilai   ")
    print("==========================")

    print("[1] LIHAT DATA")
    print("[2] TAMBAH DATA")
    print("[3] UBAH DATA ")
    print("[4] HAPUS DATA")
    print("[5] KELUAR ")

    ask = input("PILIH MENU >")

    if ask == '1':
        show()

    elif ask == '2':
        add()
    
    elif ask == '3':
        update()
    
    elif ask == '4':
        delete()
    
    elif ask == '5':
        print("\n")
        print("thank you for using the code :) ")

        exit()