import json
import os
from datetime import datetime

DATA_FILE = "data.json"

saldo = 0
transactions = []


def load_data():
    global saldo, transactions
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                saldo = float(data.get("saldo", 0))
                transactions = data.get("transactions", [])
        except (ValueError, json.JSONDecodeError, OSError):
            print("Gagal memuat data. Menggunakan saldo awal 0.")
            saldo = 0
            transactions = []


def save_data():
    try:
        tmp = DATA_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"saldo": saldo, "transactions": transactions}, f, ensure_ascii=False, indent=2)
        os.replace(tmp, DATA_FILE)
    except OSError as e:
        print("Gagal menyimpan data:", e)


def tambah_pemasukan():
    global saldo, transactions
    try:
        jumlah = float(input("Masukkan jumlah pemasukan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    saldo += jumlah
    transactions.append({"type": "pemasukan", "amount": jumlah, "time": datetime.now().isoformat()})
    save_data()
    print(f"Pemasukan sebesar Rp{jumlah:.2f} berhasil ditambahkan. Saldo sekarang: Rp{saldo:.2f}")


def tambah_pengeluaran():
    global saldo, transactions
    try:
        jumlah = float(input("Masukkan jumlah pengeluaran: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
        return

    if jumlah > saldo:
        print("Saldo tidak cukup. Transaksi dibatalkan.")
        return

    saldo -= jumlah
    transactions.append({"type": "pengeluaran", "amount": jumlah, "time": datetime.now().isoformat()})
    save_data()
    print(f"Pengeluaran sebesar Rp{jumlah:.2f} berhasil dikurangkan. Saldo sekarang: Rp{saldo:.2f}")


def lihat_saldo():
    global saldo
    # Menampilkan saldo saat ini dengan format ribuan dan 2 desimal
    print("=== Saldo Saat Ini ===")
    print(f"Saldo: Rp{saldo:,.2f}")
    print("======================")


def laporan():
    global transactions
    total_pemasukan = sum(t.get("amount", 0) for t in transactions if t.get("type") == "pemasukan")
    total_pengeluaran = sum(t.get("amount", 0) for t in transactions if t.get("type") == "pengeluaran")

    print("=== Laporan Rekap ===")
    print(f"Total pemasukan   : Rp{total_pemasukan:,.2f}")
    print(f"Total pengeluaran : Rp{total_pengeluaran:,.2f}")
    print("----------------------")

    if not transactions:
        print("Tidak ada transaksi.")
    else:
        print("Riwayat transaksi:")
        for i, t in enumerate(transactions, 1):
            ttype = "Pemasukan" if t.get("type") == "pemasukan" else "Pengeluaran"
            amt = t.get("amount", 0)
            ttime = t.get("time", "")
            try:
                tform = datetime.fromisoformat(ttime).strftime('%Y-%m-%d %H:%M:%S')
            except Exception:
                tform = ttime
            print(f"{i}. {tform} - {ttype}: Rp{amt:,.2f}")
    print("======================")


def menu():
    print("=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Laporan")
    print("5. Keluar")


if __name__ == '__main__':
    load_data()
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
            laporan()
        elif pilihan == "5":
            save_data()
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid")
