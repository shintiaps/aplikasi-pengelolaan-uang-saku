saldo = 0

def tambah_pemasukan():
    global saldo
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    saldo += jumlah
    print(f"Pemasukan sebesar Rp{jumlah:.2f} berhasil ditambahkan. Saldo sekarang: Rp{saldo:.2f}")

def tambah_pengeluaran():
    pass

def lihat_saldo():
    pass

def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")
