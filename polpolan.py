class Pembayaran:
    def __init__(self, id_pembayaran: str, jumlah: float, tanggal: str, status: bool = False):
        self.id_pembayaran = id_pembayaran
        self.jumlah = jumlah
        self.tanggal = tanggal
        self.status = status

    def set_status(self, status: bool):
        self.status = status

    def info_pembayaran(self):
        return {
            "ID Pembayaran": self.id_pembayaran,
            "Jumlah": self.jumlah,
            "Tanggal": self.tanggal,
            "Status": "Sudah Dibayar" if self.status else "Belum Dibayar"
        }

daftar_pembayaran = []
dict_pembayaran = {}

def tambah_pembayaran(id_pembayaran: str, jumlah: str, tanggal: str, status: bool = False):
    try:
        jumlah = float(jumlah)
        pembayaran_baru = Pembayaran(id_pembayaran, jumlah, tanggal, status)
        daftar_pembayaran.append(pembayaran_baru)
        dict_pembayaran[id_pembayaran] = pembayaran_baru
        print(f"Pembayaran dengan ID {id_pembayaran} berhasil ditambahkan.")
    except ValueError:
        print("Kesalahan: Jumlah pembayaran harus berupa angka.")

def tampilkan_semua_pembayaran():
    if not daftar_pembayaran:
        print("Belum ada pembayaran yang tercatat.")
        return
    
    for pembayaran in daftar_pembayaran:
        print(pembayaran.info_pembayaran())

def cari_pembayaran(id_pembayaran: str):
    pembayaran = dict_pembayaran.get(id_pembayaran)
    if pembayaran:
        print(pembayaran.info_pembayaran())
    else:
        print(f"Kesalahan: Pembayaran dengan ID {id_pembayaran} tidak ditemukan.")

def ubah_status_pembayaran(id_pembayaran: str, status: bool):
    pembayaran = dict_pembayaran.get(id_pembayaran)
    if pembayaran:
        pembayaran.set_status(status)
        print(f"Status pembayaran dengan ID {id_pembayaran} berhasil diubah.")
    else:
        print(f"Kesalahan: Pembayaran dengan ID {id_pembayaran} tidak ditemukan.")

def menu_program():
    while True:
        print("\n=== Program Manajemen Pembayaran ===")
        print("1. Tambah Pembayaran Baru")
        print("2. Tampilkan Semua Pembayaran")
        print("3. Cari Pembayaran Berdasarkan ID")
        print("4. Ubah Status Pembayaran")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            id_pembayaran = input("Masukkan ID Pembayaran: ")
            jumlah = input("Masukkan Jumlah Pembayaran: ")
            tanggal = input("Masukkan Tanggal Pembayaran (YYYY-MM-DD): ")
            status_input = input("Apakah sudah dibayar? (y/n): ").lower()
            status = True if status_input == "y" else False
            tambah_pembayaran(id_pembayaran, jumlah, tanggal, status)

        elif pilihan == "2":
            print("\nDaftar Semua Pembayaran:")
            tampilkan_semua_pembayaran()

        elif pilihan == "3":
            id_pembayaran = input("Masukkan ID Pembayaran yang dicari: ")
            cari_pembayaran(id_pembayaran)

        elif pilihan == "4":
            id_pembayaran = input("Masukkan ID Pembayaran: ")
            status_input = input("Ubah status menjadi sudah dibayar? (y/n): ").lower()
            status = True if status_input == "y" else False
            ubah_status_pembayaran(id_pembayaran, status)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

menu_program()
