# print("=== SIMPAN DATA NILai ===")
#
# file = open("nilai_siswa.txt", "w")
#
# while True:
#     nama = input("Nama siswa (enter untuk selesai):")
#     if nama == "":
#         break
#
#     nilai = input("nilai siswa : ")
#
#     file.write(nama + " , " + nilai +"\n")
#     print("Data", nama, "berhasil disimpan")
#
# file.close()
# print("=== PROGRAM SELESAI ===")

print("=== MENAMPILKAN ===")
try:
    with open("nilai_siswa2.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File not found")

print("=== PROGRAM SELESAI ===")