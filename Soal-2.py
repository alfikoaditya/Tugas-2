nama = []
kontak = []
def ambil_data():
    input_nama = str(input("Nama: "))
    nama.append(input_nama)
def ambil_data2():
    input_kontak = int(input("No Telepon: "))
    kontak.append(input_kontak)
def tampil_data():
    for i in range(len(nama)):
        print("Nama: {}".format(nama[i]))
        print("Kontak: {}".format(kontak[i]))
        print("+==================+")
while True:
    print()
    print("Selamat datang!")
    print()
    print("------Menu------")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()
    inputan = int(input("Pilih Menu: "))
    if inputan == 1:
        print()
        print("Daftar Kontak:")
        print()
        tampil_data()
    elif inputan == 2:
        print()
        ambil_data()
        ambil_data2()
        print()
        print("Kontak berhasil ditambahkan")
    elif inputan == 3:
        print()
        print("Program selesai, sampai jumpa!")
        print()
        break
    else:
        print()
        print("Menu tidak tersedia")