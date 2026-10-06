import datetime
import os
import time

# data program

users = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

bands = {}
songs = {}
lineups = {}


# os
def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


# time
def loading():
    print("Memproses", end="")

    for i in range(3):
        time.sleep(0.5)
        print(".", end="")

    print()


# login
def login():

    while True:

        bersihkan_layar()

        print("===================================")
        print("     SISTEM MANAJEMEN LINE-UP")
        print("              KONSER")
        print("===================================")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")
        print("===================================")

        pilihan = input("Pilih menu: ")

        # LOGIN ADMIN
        if pilihan == "1":

            print("----------- LOGIN ADMIN -----------")

            username = input("Username : ")
            password = input("Password : ")

            if username == "admin":
                if users[username]["password"] == password:
                    print("\nLogin Admin berhasil!")
                    print("Selamat datang,", username)

                    loading()

                    return username, "admin"

                else:
                    print("\nPassword Admin salah!")

            else:
                print("\nUsername Admin salah!")

            time.sleep(1)

        # LOGIN USER
        elif pilihan == "2":

            print("\n------------ LOGIN USER ------------")

            username = input("Username : ")
            password = input("Password : ")

            if username == "user":
                if users[username]["password"] == password:
                    print("\nLogin User berhasil!")
                    print("Selamat datang,", username)

                    loading()

                    return username, "user"

                else:
                    print("\nPassword User salah!")

            else:
                print("\nUsername User salah!")

            time.sleep(1)

        # keluar
        elif pilihan == "3":

            return "", "keluar"

        else:

            print("\nPilihan tidak tersedia!")
            time.sleep(1)


# datetime
def cek_jam():

    while True:
        jam = input("Jam tampil (HH:MM): ")

        try:
            datetime.datetime.strptime(jam, "HH:MM")

            return jam

        except:
            print("Format jam salah!")
            print("Gunakan format HH:MM")
            print("Contoh: 19:30")


# tambah band
def tambah_band():

    print("\n----- TAMBAH BAND -----")

    nama = input("Nama band: ")

    if nama == "":
        print("Nama band tidak boleh kosong!")
        time.sleep(1)
        return

    if nama in bands:
        print("Band sudah terdaftar!")
        time.sleep(1)
        return

    genre = input("Genre band: ")

    if genre == "":
        print("Genre tidak boleh kosong!")
        time.sleep(1)
        return

    bands[nama] = {
        "genre": genre
    }

    print("\nBand berhasil ditambahkan!")
    time.sleep(1)


# data band
def tampilkan_band():

    print("\n------ DATA BAND -----")

    if len(bands) == 0:
        print("Belum ada data band.")
        time.sleep(1)
        return

    nomor = 1

    for nama in bands:
        print(nomor, ".", nama)
        print("   Genre:", bands[nama]["genre"])

        nomor += 1

    time.sleep(1)


# ubah band
def ubah_band():

    tampilkan_band()

    if len(bands) == 0:
        return

    nama = input("\nMasukkan nama band yang ingin diubah: ")

    if nama not in bands:
        print("Band tidak ditemukan!")
        time.sleep(1)
        return

    genre_baru = input("Genre baru: ")

    if genre_baru == "":
        print("Genre tidak boleh kosong!")
        time.sleep(1)
        return

    bands[nama]["genre"] = genre_baru

    print("\nData band berhasil diubah!")
    time.sleep(1)


# hapus band
def hapus_band():

    tampilkan_band()

    if len(bands) == 0:
        return

    nama = input("\nMasukkan nama band yang ingin dihapus: ")

    if nama not in bands:
        print("Band tidak ditemukan!")
        time.sleep(1)
        return

    del bands[nama]

    print("\nBand berhasil dihapus!")
    time.sleep(1)


# menu band
def menu_band():

    while True:

        bersihkan_layar()

        print("========== MENU BAND ==========")
        print("1. Tambah Band")
        print("2. Lihat Band")
        print("3. Ubah Band")
        print("4. Hapus Band")
        print("5. Kembali")
        print("===============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_band()

        elif pilihan == "2":
            tampilkan_band()

        elif pilihan == "3":
            ubah_band()

        elif pilihan == "4":
            hapus_band()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia!")
            time.sleep(1)


# tambah lagu
def tambah_lagu():

    bersihkan_layar()

    print("\n----- TAMBAH LAGU -----")

    if len(bands) == 0:
        print("Belum ada band.")
        print("Tambahkan band terlebih dahulu.")
        time.sleep(1)
        return

    daftar_band = list(bands.keys())

    print("\nDaftar Band:")

    nomor = 1

    for nama in daftar_band:
        print(nomor, ".", nama)
        nomor += 1

    pilihan = input("\nPilih band: ")

    try:
        pilihan = int(pilihan)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan < 1 or pilihan > len(daftar_band):
        print("Nomor band tidak tersedia!")
        time.sleep(1)
        return

    band = daftar_band[pilihan - 1]

    print("\nBand dipilih:", band)

    judul = input("Judul lagu: ")

    if judul == "":
        print("Judul lagu tidak boleh kosong!")
        time.sleep(1)
        return

    if judul in songs:
        print("Lagu sudah terdaftar!")
        time.sleep(1)
        return

    songs[judul] = {
        "band": band
    }

    print("\nLagu berhasil ditambahkan!")
    print("Band :", band)
    print("Lagu :", judul)

    time.sleep(1)


# data lagu
def tampilkan_lagu():

    print("\n------ DATA LAGU ------")

    if len(songs) == 0:
        print("Belum ada data lagu.")
        time.sleep(1)
        return

    nomor = 1

    for judul in songs:
        print(nomor, ".", judul)
        print("   Band:", songs[judul]["band"])

        nomor += 1

    time.sleep(1)


# ubah lagu
def ubah_lagu():

    tampilkan_lagu()

    if len(songs) == 0:
        return

    judul = input("\nMasukkan judul lagu yang ingin diubah: ")

    if judul not in songs:
        print("Lagu tidak ditemukan!")
        time.sleep(1)
        return

    daftar_band = list(bands.keys())

    print("\nDaftar Band:")

    nomor = 1

    for nama in daftar_band:
        print(nomor, ".", nama)
        nomor += 1

    pilihan = input("\nPilih band baru: ")

    try:
        pilihan = int(pilihan)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan < 1 or pilihan > len(daftar_band):
        print("Nomor band tidak tersedia!")
        time.sleep(1)
        return

    band_baru = daftar_band[pilihan - 1]

    songs[judul]["band"] = band_baru

    print("\nData lagu berhasil diubah!")
    time.sleep(1)


# hapus lagu
def hapus_lagu():

    tampilkan_lagu()

    if len(songs) == 0:
        return

    judul = input("\nMasukkan judul lagu yang ingin dihapus: ")

    if judul not in songs:
        print("Lagu tidak ditemukan!")
        time.sleep(1)
        return

    del songs[judul]

    print("\nLagu berhasil dihapus!")
    time.sleep(1)


# menu lagu
def menu_lagu():

    while True:

        bersihkan_layar()

        print("========== MENU LAGU ==========")
        print("1. Tambah Lagu")
        print("2. Lihat Lagu")
        print("3. Ubah Lagu")
        print("4. Hapus Lagu")
        print("5. Kembali")
        print("===============================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_lagu()

        elif pilihan == "2":
            tampilkan_lagu()

        elif pilihan == "3":
            ubah_lagu()

        elif pilihan == "4":
            hapus_lagu()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia!")
            time.sleep(1)


# tambah line-up
def tambah_lineup():

    print("\n----- TAMBAH LINE-UP -----")

    if len(bands) == 0:
        print("Belum ada band.")
        time.sleep(1)
        return

    if len(songs) == 0:
        print("Belum ada lagu.")
        time.sleep(1)
        return

    nomor = input("Nomor urutan tampil: ")

    if nomor == "":
        print("Nomor tidak boleh kosong!")
        time.sleep(1)
        return

    try:
        nomor = int(nomor)

    except:
        print("Nomor harus berupa angka!")
        time.sleep(1)
        return

    if nomor <= 0:
        print("Nomor harus lebih dari 0!")
        time.sleep(1)
        return

    if nomor in lineups:
        print("Nomor urutan sudah digunakan!")
        time.sleep(1)
        return

    daftar_band = list(bands.keys())

    print("\nDaftar Band:")

    angka = 1

    for nama in daftar_band:
        print(angka, ".", nama)
        angka += 1

    pilihan_band = input("\nPilih band: ")

    try:
        pilihan_band = int(pilihan_band)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan_band < 1 or pilihan_band > len(daftar_band):
        print("Nomor band tidak tersedia!")
        time.sleep(1)
        return

    band = daftar_band[pilihan_band - 1]

    print("\nBand dipilih:", band)

    lagu_band = []

    for judul in songs:

        if songs[judul]["band"] == band:
            lagu_band.append(judul)

    if len(lagu_band) == 0:

        print("\nBand ini belum memiliki lagu.")
        time.sleep(1)
        return

    print("\nDaftar Lagu", band, ":")

    angka = 1

    for judul in lagu_band:

        print(angka, ".", judul)
        angka += 1

    pilihan_lagu = input("\nPilih lagu: ")

    try:
        pilihan_lagu = int(pilihan_lagu)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan_lagu < 1 or pilihan_lagu > len(lagu_band):

        print("Nomor lagu tidak tersedia!")
        time.sleep(1)
        return

    lagu = lagu_band[pilihan_lagu - 1]

    jam = cek_jam()

    lineups[nomor] = {
        "band": band,
        "lagu": lagu,
        "jam": jam
    }

    print("\nLine-up berhasil ditambahkan!")
    print("Band :", band)
    print("Lagu :", lagu)
    print("Jam  :", jam)

    time.sleep(1)


# data line-up
def tampilkan_lineup():

    print("\n------ DATA LINE-UP ------")

    if len(lineups) == 0:
        print("Belum ada data line-up.")
        time.sleep(1)

        return

    for nomor in sorted(lineups):

        print("Nomor Urutan:", nomor)
        print("Band:", lineups[nomor]["band"])
        print("Lagu:", lineups[nomor]["lagu"])
        print("Jam:", lineups[nomor]["jam"])
        print("-----------------------------")

    time.sleep(1)


# ubah line-up
def ubah_lineup():

    tampilkan_lineup()

    if len(lineups) == 0:
        return

    try:
        nomor = int(input("\nMasukkan nomor urutan yang ingin diubah: "))

    except:
        print("Nomor harus berupa angka!")
        time.sleep(1)
        return

    if nomor not in lineups:
        print("Line-up tidak ditemukan!")
        time.sleep(1)
        return

    daftar_band = list(bands.keys())

    print("\nDaftar Band:")

    angka = 1

    for nama in daftar_band:
        print(angka, ".", nama)
        angka += 1

    pilihan_band = input("\nPilih band baru: ")

    try:
        pilihan_band = int(pilihan_band)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan_band < 1 or pilihan_band > len(daftar_band):
        print("Nomor band tidak tersedia!")
        time.sleep(1)
        return

    band = daftar_band[pilihan_band - 1]

    lagu_band = []

    for judul in songs:

        if songs[judul]["band"] == band:
            lagu_band.append(judul)

    if len(lagu_band) == 0:
        print("Band ini belum memiliki lagu.")
        time.sleep(1)
        return

    print("\nDaftar Lagu", band, ":")

    angka = 1

    for judul in lagu_band:
        print(angka, ".", judul)
        angka += 1

    pilihan_lagu = input("\nPilih lagu baru: ")

    try:
        pilihan_lagu = int(pilihan_lagu)

    except:
        print("Pilihan harus berupa angka!")
        time.sleep(1)
        return

    if pilihan_lagu < 1 or pilihan_lagu > len(lagu_band):
        print("Nomor lagu tidak tersedia!")
        time.sleep(1)
        return

    lagu = lagu_band[pilihan_lagu - 1]

    jam = cek_jam()

    lineups[nomor] = {
        "band": band,
        "lagu": lagu,
        "jam": jam
    }

    print("\nData line-up berhasil diubah!")
    time.sleep(1)


# hapus line-up
def hapus_lineup():

    tampilkan_lineup()

    if len(lineups) == 0:
        return

    try:
        nomor = int(input("\nMasukkan nomor urutan yang ingin dihapus: "))

    except:
        print("Nomor harus berupa angka!")
        time.sleep(1)
        return

    if nomor not in lineups:
        print("Line-up tidak ditemukan!")
        time.sleep(1)
        return

    del lineups[nomor]

    print("\nLine-up berhasil dihapus!")
    time.sleep(1)


# menu line-up
def menu_lineup():

    while True:

        bersihkan_layar()

        print("========== MENU LINE-UP ==========")
        print("1. Tambah Line-Up")
        print("2. Lihat Line-Up")
        print("3. Ubah Line-Up")
        print("4. Hapus Line-Up")
        print("5. Kembali")
        print("==================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_lineup()

        elif pilihan == "2":
            tampilkan_lineup()

        elif pilihan == "3":
            ubah_lineup()

        elif pilihan == "4":
            hapus_lineup()

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak tersedia!")
            time.sleep(1)


# menu admin
def menu_admin():

    while True:

        bersihkan_layar()

        print("===================================")
        print("             MENU ADMIN")
        print("===================================")
        print("1. Kelola Band")
        print("2. Kelola Lagu")
        print("3. Kelola Line-Up")
        print("4. Logout")
        print("===================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_band()

        elif pilihan == "2":
            menu_lagu()

        elif pilihan == "3":
            menu_lineup()

        elif pilihan == "4":

            print("\nAdmin logout...")
            loading()
            break

        else:

            print("Pilihan tidak tersedia!")
            time.sleep(1)


# menu user
def menu_user():

    while True:

        bersihkan_layar()

        print("===================================")
        print("              MENU USER")
        print("===================================")
        print("1. Lihat Line-Up")
        print("2. Logout")
        print("===================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":

            tampilkan_lineup()
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":

            print("\nUser logout...")
            loading()
            break

        else:

            print("Pilihan tidak tersedia!")
            time.sleep(1)


# program utama
while True:

    username, role = login()

    # keluar
    if role == "keluar":

        bersihkan_layar()

        print("\n===================================")
        print("       TERIMA KASIH TELAH")
        print("   MENGGUNAKAN SISTEM INI")
        print("===================================")

        break

    # admin
    elif role == "admin":

        menu_admin()

    # user
    elif role == "user":

        menu_user()

    print("\nKembali ke menu login...")
    time.sleep(1)