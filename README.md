# mini-project2-fina-salsabila-prasetyo
# penjelasan program
Program sistem menajemen line_up konser merupakan pengembangan dari mini project 1 yang digunakan unutuk mengelola data band, lagu, dan line-up penampilan dalam sebuah konser.

Perogram ini memliki dua role pengguna yaitu:

1.admin : memiliki hak akses untuk mengelola data band, lagu, dan line-up 

2.user : memiliki hah akses untuk melihat data line up

program ini dilengkapi dengan sistem login menggunkan username dan password serta validasi input menggunakan conditional statement.Data program disimpan menggunakan stuktur data dictionary dan program dibuat menggunakan beberapa function agar setiap proses dapat dipisahkan berdasarkan fungsinya.

# flowchat


<img width="1062" height="846" alt="image" src="https://github.com/user-attachments/assets/047ad077-5cd8-4a0b-ad3f-354f83e31b66" />


# penjelsan alur

Alur program dimulai dari proses "Mulai" kemudian program melakukan inisialisasi data "users", "bands", "songs", dan "lineups".

Setelah itu program menampilkan menu login yang terdiri dari tiga pilihan:

1. Admin
2. User
3. Keluar

Pengguna memasukkan pilihan menu. Lalu orogram kemudian melakukan pengecekan menggunakan Decision (percabangan).

 Pilihan Admin

Jika pengguna memilih "Admin", program meminta:

- Username
- Password

Program melakukan validasi username dan password.

Jika username atau password salah, program menampilkan pesan kesalahan dan pengguna dapat mencoba kembali.

Jika login berhasil, pengguna masuk ke "Menu Admin".

Menu Admin terdiri dari:

1. Kelola Band
2. Kelola Lagu
3. Kelola Line-Up
4. Logout

Kelola Band

Admin dapat melakukan:

- Tambah Band
- Lihat Band
- Ubah Band
- Hapus Band
- Kembali

Kelola Lagu

Admin dapat melakukan:

- Tambah Lagu
- Lihat Lagu
- Ubah Lagu
- Hapus Lagu
- Kembali

Kelola Line-Up

Admin dapat melakukan:

- Tambah Line-Up
- Lihat Line-Up
- Ubah Line-Up
- Hapus Line-Up
- Kembali

Pada proses Line-Up terdapat validasi nomor urutan, pemilihan band, pemilihan lagu, format jam tampil, serta pengecekan agar jadwal tidak bentrok.

Setelah selesai melakukan proses pengelolaan data, Admin dapat kembali ke Menu Admin.

Jika Admin memilih "Logout", program kembali ke Menu Login.

Pilihan User

Jika pengguna memilih "User", program meminta username dan password.

Program melakukan validasi username dan password.

Jika login berhasil, pengguna masuk ke "Menu User".

Menu User terdiri dari:

1. Lihat Line-Up
2. Logout

User hanya memiliki akses untuk melihat data Line-Up dan tidak dapat menambah, mengubah, maupun menghapus data.

Jika User memilih "Logout", program kembali ke Menu Login.

Pilihan Keluar

Jika pengguna memilih menu "Keluar", program menampilkan pesan bahwa program selesai digunakan dan program berhenti.

Pilihan Tidak Valid

Jika pengguna memasukkan pilihan yang tidak tersedia, program menampilkan pesan:

> Pilihan tidak tersedia!

Kemudian pengguna diarahkan kembali untuk memilih menu yang tersedia.

# dokumentasi Program & output


<img width="447" height="485" alt="image" src="https://github.com/user-attachments/assets/8609ed4b-fa0a-447b-871f-3f9b21e8bd6d" />

Bagian ini merupakan tahap awal program untuk menyiapkan library dan struktur data.

Terdapat tiga library yang digunakan:

datetime digunakan untuk melakukan validasi format jam.
os digunakan untuk membersihkan tampilan terminal.
time digunakan untuk memberikan jeda waktu dan efek loading.
Program juga menggunakan Dictionary untuk menyimpan data pengguna.

Dictionary users menyimpan:

username
password
role pengguna

Pada bagian ini belum ada output nya karena program baru melalukan periapan data.


<img width="558" height="341" alt="image" src="https://github.com/user-attachments/assets/fe683695-7a16-4549-9289-9c5459453775" />

Function bersihkan_layar() digunakan untuk membersihkan tampilan terminal sebelum menu baru ditampilkan.

Function loading() digunakan untuk memberikan efek proses ketika program sedang melakukan login atau proses lainnya.
Penggunaan function membuat kode lebih terstruktur karena proses yang sama tidak perlu ditulis berulang kali.

**output**

<img width="142" height="43" alt="image" src="https://github.com/user-attachments/assets/88b00425-589c-433a-b250-27a5968cc01b" />

Penggunaan function membuat program menjadi lebih rapi, modular, dan mudah dikembangkan. Selain itu, library os dan time tidak hanya digunakan sebagai syarat, tetapi juga memberikan fungsi nyata pada program.


<img width="600" height="437" alt="image" src="https://github.com/user-attachments/assets/d68ba874-f62f-46d9-a127-43b019be5655" />

Function login() digunakan sebagai pintu masuk utama program.

Pengguna diberikan tiga pilihan:

1. Admin
2. User
3. Keluar

Program menggunakan if, elif, dan else untuk menentukan proses berdasarkan pilihan pengguna.

Jika memilih Admin, program meminta username dan password Admin.

Jika memilih User, program meminta username dan password User.

Jika memilih Keluar, function mengembalikan

**output**

<img width="342" height="210" alt="image" src="https://github.com/user-attachments/assets/e55ee1f1-2ec3-43c6-a2b1-c796d4c3e81c" />

Dari output tersebut dapat diketahui bahwa program sudah memiliki alur awal yang jelas. Pengguna tidak langsung masuk ke pengelolaan data, tetapi harus menentukan role terlebih dahulu.


<img width="523" height="350" alt="image" src="https://github.com/user-attachments/assets/267f93fe-f477-4994-8b8c-1dfdc70b7a35" />

Bagian ini digunakan untuk melakukan validasi login Admin.
Program mengecek dua hal:

Apakah username yang dimasukkan adalah admin.
Apakah password sesuai dengan password yang tersimpan di Dictionary users.

**output**

<img width="392" height="161" alt="image" src="https://github.com/user-attachments/assets/1b881360-df5f-4b4c-833a-3a96520a45cb" />

Validasi ini mencegah pengguna masuk ke menu Admin tanpa password yang benar.
Dari sini terlihat bahwa role Admin tidak hanya berupa tampilan menu, tetapi benar-benar menentukan akses pengguna ke fungsi pengelolaan data.


<img width="598" height="362" alt="image" src="https://github.com/user-attachments/assets/131e3086-6b66-4adf-8ef6-52e4d2185b5a" />

Bagian ini digunakan untuk melakukan login sebagai User.

Jika username dan password sesuai, program mengembalikan role, Role tersebut kemudian digunakan oleh program utama untuk menentukan menu yang dapat diakses.

**output**

<img width="356" height="207" alt="image" src="https://github.com/user-attachments/assets/1fabe548-42d7-43cc-a6ff-2ceaa2dd45bb" />

Program memiliki dua role dengan hak akses berbeda.Admin dapat melakukan pengelolaan data, sedangkan User mendapatkan akses yang lebih terbatas.

<img width="532" height="750" alt="image" src="https://github.com/user-attachments/assets/996439d0-1e28-4d05-95a4-ea3c3066ab83" />

Function tambah_band() digunakan untuk menambahkan data Band ke Dictionary bands.

Sebelum data disimpan, program melakukan validasi:

Nama Band tidak boleh kosong.
Nama Band tidak boleh sama.
Genre tidak boleh kosong.

Jika semua validasi terpenuhi, data dimasukkan ke Dictionary.

**output**


<img width="262" height="173" alt="image" src="https://github.com/user-attachments/assets/325e98fb-b176-42a5-becf-e5a0c8f8feb1" />


Program tidak langsung menyimpan input pengguna. Data diperiksa terlebih dahulu sehingga kemungkinan data kosong atau data duplikat dapat dikurangi.


<img width="502" height="395" alt="image" src="https://github.com/user-attachments/assets/2a235d43-d03a-4371-adbd-8566742dc887" />

Function ini digunakan untuk menampilkan seluruh data Band yang tersimpan dalam Dictionary bands.
Program terlebih dahulu mengecek apakah Dictionary kosong.

Jika kosong:

Belum ada data band.

Jika terdapat data, program melakukan perulangan untuk menampilkan seluruh Band.

**output**

<img width="252" height="197" alt="image" src="https://github.com/user-attachments/assets/98dca54d-2a09-44a3-9f02-4ae0aead5986" />
Fungsi ini merupakan bagian dari Read pada konsep CRUD karena digunakan untuk membaca dan menampilkan data.


<img width="387" height="183" alt="image" src="https://github.com/user-attachments/assets/41c63573-ceb6-4306-b66c-1de17640176a" />

Program mengecek terlebih dahulu apakah Band yang ingin diubah atau dihapus memang terdapat dalam Dictionary. Jika ditemukan, data dapat diubah atau dihapus.

**output**


<img width="457" height="245" alt="image" src="https://github.com/user-attachments/assets/277a693d-6490-4b6b-87a4-7c4f54fc6025" />

Dari proses ini terlihat bahwa Admin memiliki CRUD lengkap terhadap data Band


<img width="516" height="440" alt="image" src="https://github.com/user-attachments/assets/cc12491b-61eb-4b12-a305-445b33965866" />

Kemudian program meminta Admin memilih Band sebelum memasukkan lagu. Penjelasan Function tambah_lagu() digunakan untuk menambahkan lagu.Program memastikan bahwa Band sudah tersedia terlebih dahulu. Setelah Band dipilih, pengguna memasukkan judul lagu. Data kemudian disimpan ke Dictionary songs.

**output**


<img width="288" height="258" alt="image" src="https://github.com/user-attachments/assets/b278fb17-eb2a-472d-9e7b-a2169a78c990" />

Program menerapkan hubungan antara Band dan Lagu. Lagu tidak dapat dibuat jika belum terdapat Band.
Hal ini membuat data yang dimasukkan lebih terstruktur.


<img width="628" height="751" alt="image" src="https://github.com/user-attachments/assets/88025b4d-4e92-446e-899b-fe3998ad0cbc" />

Menu Line-Up merupakan bagian utama pengelolaan jadwal konser.

Admin dapat:

Menambahkan Line-Up.
Melihat Line-Up.
Mengubah Line-Up.
Menghapus Line-Up.
Kembali ke Menu Admin.

Dengan demikian, Line-Up juga menerapkan konsep CRUD.

**output**


<img width="347" height="190" alt="image" src="https://github.com/user-attachments/assets/7d201eef-9165-4137-ae1f-712373d46e18" />

Menu ini menunjukkan bahwa program tidak hanya menyimpan data Band dan Lagu, tetapi juga menghubungkan keduanya dalam sebuah jadwal penampilan konser.


<img width="645" height="852" alt="image" src="https://github.com/user-attachments/assets/497f968b-968b-43f0-9d7a-da11b61a2f28" />

Function menu_admin() menjadi pusat pengelolaan data untuk Admin. Admin dapat memilih menu Band, Lagu, Line-Up, atau Logout.


<img width="356" height="221" alt="image" src="https://github.com/user-attachments/assets/162200d1-6f11-4c84-9a81-34e68974e9f0" />

Dari bagian ini terlihat dengan jelas hak akses Admin. Semua fungsi CRUD dapat diakses melalui Menu Admin.

<img width="642" height="726" alt="image" src="https://github.com/user-attachments/assets/419e5fbd-ef6c-4070-a10a-3c112baa94fd" />

Menu User memiliki akses yang lebih terbatas dibandingkan Admin.

User hanya dapat:

Melihat Line-Up.
Logout.

User tidak memiliki menu untuk menambah, mengubah, atau menghapus data.


<img width="380" height="175" alt="image" src="https://github.com/user-attachments/assets/06b98b22-443f-4cbd-acbc-4c380c822702" />

Pembagian role berhasil diterapkan karena menu yang diterima User berbeda dengan menu Admin. User hanya berperan sebagai pengguna yang melihat informasi Line-Up, sedangkan Admin bertugas mengelola data.

# nilai tambah

<img width="426" height="187" alt="image" src="https://github.com/user-attachments/assets/0cfc39a1-5e83-48e4-87fd-ee75c22fedac" />

<img width="166" height="71" alt="image" src="https://github.com/user-attachments/assets/c7f7b5c6-bd69-4d6f-866d-805c0c7277c5" />


Program memiliki validasi input menggunakan error handling, sehingga ketika pengguna memasukkan data yang tidak sesuai, program dapat menangani kesalahan tersebut dan menampilkan pesan peringatan tanpa langsung menghentikan program. Validasi diterapkan pada beberapa proses, seperti pemilihan menu, pengisian data, dan validasi waktu pada Line-Up.
Program menerapkan 3 library atau lebih sesuai dengan kebutuhan program, yaitu:
datetime → digunakan untuk melakukan pengecekan dan pengolahan waktu pada jadwal Line-Up.
os → digunakan untuk membersihkan tampilan layar agar tampilan program di terminal lebih rapi.
time → digunakan untuk memberikan efek jeda/loading pada program sehingga perpindahan proses terlihat lebih teratur.Dengan adanya validasi menggunakan error handling dan penggunaan beberapa library sesuai kebutuhan, program menjadi lebih aman terhadap kesalahan input, lebih terstruktur, dan lebih nyaman digunakan.
