def nama_function():
    print("hello world Iam here")

def sapa_nama(nama):
    print("hello", nama)
    print(f"nice to meet you {nama}" )

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f"luas persegi panjang {luas}")

nama_function()
sapa_nama("maya")
hitung_luas_persegi_panjang(10, 20)

#function dengan return value
def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas
luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)
print(f"luas lingkaran radius 5: {luas1}")
print(f"luas lingkaran radius 10: {luas2}")
print(f"Total luas ", luas1 + luas2)


# default parameter
def sapa(nama, sapaan="halo "):
    print(sapaan, nama)
sapa("maya") # halo maya
sapa("santi", "Hi") # Hi santi

# keyword argument
def perkenalan(nama, umur, kota):
    print(f"Nama: {nama}")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")
    print("----------------")

# position arguments (urutan harus sesuai)
perkenalan("alice", 25, "jakarta")

# keyword arguments (urutan bebas)
perkenalan(kota="bandung", nama="dody", umur=33)


def buat_profil(nama, umur, kota="Jakarta", pekerjaan="Belum bekerja"):
    print(f"====={nama.upper()}====")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")
    print(f"Pekerjaan: {pekerjaan}")
    print("--------------")

# position + keyword arguments
buat_profil("alice", 25) # menggunakan default
buat_profil("bob", 30, kota="bandung")
buat_profil("charlie", 28, pekerjaan="developer")
buat_profil("diana", 33, kota="bogor", pekerjaan="chef")

# local variable
def fungsi_test():
    x = 10
    print(f"nilai x adalah {x}")

fungsi_test()
# print(x) x tidak bisa diakses luar, karena local variable


# global variable
nama_global = "sinta"
def tampilkan_nama():
    print(f"Nama : {nama_global}")

def ubah_nama_global():
    global nama_global
    nama_global = "jojo" # mengubah global variable
    print(f"Nama : {nama_global}")

tampilkan_nama()
ubah_nama_global()

# parameter dinamis
def cetak_list(*list):
    for item in list:
        print(item)

cetak_list(1,2,3,4,5)
cetak_list("veronica", "maya", "santi", "wijaya")

def cetak_dict(**dict):
    for key, value in dict.items():
        print(key, value)
cetak_dict(a=1, b=2, c=3)
