# membuat variabel
variabel_ku = "ini isi variabel"
variabel2 = 20
print(variabel_ku)
print(variabel2)

# penulisan variabel
nama = "python"
print ("nama")
del(nama)
print("nama")

# jenis jenis tipe data
nama_ku = "Maylia Rafa Niswah"
umur = 17
tinggi = 160
print(nama_ku)
print(umur)
print(tinggi)

# tipe data angka
harga = 20000 #tipe int
berat = 25 #float
jarak = 3e3 #float 3000.0, huruf e artinya eksponen 10 
print(harga)
print(berat)
print(jarak)

# tipe data teks
nama ="Maylia Rafa Niswah"
jenis_kelamin = 'P'
alamat = """
J.l Citra Hamperi, No 20. RT Kode,
Kelurahan Simpang Baru, Pekanbaru
"""
agama = 'islam'
print(nama)
print(jenis_kelamin)
print(alamat)
print(agama)

# tipe data boolean
bergerak = True
nyala = False
print(bergerak)
print(nyala)

# contoh program
nama="Maylia Rafa Niswah"
alamat='Pekanbaru'
umur=17
tinggi=160
menikah=False
print(nama)
print(alamat)
print(umur)
print(tinggi)
print(menikah)

# konversi tipe data
a = 10
b = 3
c = a / b
print (c) 

# cara mengambil input
nama_variabel = input("Sebuah Teks")
print(nama)

# cara menampilkan output
nama = "Maylia Rafa Niswah"
print ("Hello", nama)

# Mengumpulkan Input
nama_lengkap = input("Masukkan nama lengkap Anda: ")
usia_tahun = int(input("Masukkan usia Anda dalam tahun: "))
tinggi_cm = float(input("Masukkan tinggi badan Anda dalam sentimeter: "))
status_menikah = input("Apakah Anda sudah menikah? (y/n): ").lower() == 'y'

# Memproses Data
usia_bulan = usia_tahun * 12
tinggi_meter = tinggi_cm / 100

# Menampilkan Output
print("\n--- Ringkasan Informasi ---")
print(f"Nama lengkap: {nama_lengkap}")
print(f"Usia: {usia_tahun} tahun atau {usia_bulan} bulan")
print(f"Tinggi badan: {tinggi_cm} cm atau {tinggi_meter:.2f} m")
print(f"Status pernikahan: {'Sudah menikah' if status_menikah else 'Belum menikah'}")

print("==================") 
print("Numerare Numerus") 
print("==================") 
 
print("powerd by:") 
print("maylia rafa niswah") 
 
print("===============") 
print("pilihan operasi") 
print("1. Tambah") 
print("2. Kurang") 
print("3. Bagi") 
print("4. Kali") 
print("===============") 
 
operasi = int(input("Masukkan pilihan operasi (1/2/3/4)")) 
 
if operasi == 1: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x + y 
    print("Hasilnya adalah : ", x, "+", y, "=", z) 
    print("=========================") 
 
elif operasi == 2: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x + y 
    print("Hasilnya adalah : ", x, "+", y, "=", z) 
    print("=========================") 
 
elif operasi == 3: 
    x = float (input("Masukkan nilai pertama : ")) 
    y = float (input("Masukkan nilai kedua : ")) 
    z = x / y 
    print("Hasilnya adalah : ", x, "/", y, "=", z) 
    print("=========================") 
 
elif operasi == 4: 
    x = int (input("Masukkan nilai pertama : ")) 
    y = int (input("Masukkan nilai kedua : ")) 
    z = x * y 
    print("Hasilnya adalah : ", x, "x", y, "=", z) 
    print("=========================")

    # Meminta pengguna memasukkan nilai awal 
nilai = float(input("Masukkan nilai awal: ")) 
 
# Tambahkan 2 ke nilai tersebut 
nilai += 2 
print(f"Setelah ditambah 2: {nilai}") 
 
# Kurangi nilai tersebut dengan 3 
nilai -= 3 
print(f"Setelah dikurangi 3: {nilai}") 
 
# Kalikan nilai tersebut dengan 10 
nilai *= 10 
print(f"Setelah dikalikan 10: {nilai}") 
 
# Bagi nilai tersebut dengan 4 
nilai /= 4 
print(f"Setelah dibagi 4: {nilai}") 
 
# Hitung pangkat nilai tersebut dengan 10 
nilai **= 10 
print(f"Setelah dipangkatkan 10: {nilai}")