# print("hello world"

# print(nama)
# NameError: name 'nam' is not defined

# print("5" + 5)
# TypeError: can only concatenate str (not "int") to str

# value = int("abc")
# print(value)
# ValueError: invalid literal for int() with base 10: 'abc'

# list_data = [1,2,3]
# print(list_data[5])
# IndexError: list index out of range

# orang = {"nama" : "icha"}
# print(orang["umur"])
# KeyError: 'umur'

# print(10/0)
# ZeroDivisionError: division by zero

# try-except
# print("=== KALKULATOR SEDERHANA ===")
# try:
#     angka1 = int(input("angka1: "))
#     angka2 = int(input("angka2: "))
#     hasil = angka1 / angka2
#     print(f"hasil : {hasil}")
#
# except ValueError:
#     print("input pengguna bukan angka")
# except ZeroDivisionError:
#     print("tidak bisa dibagi dengan 0")
# except:
#     print("terjadi kesalahan program")
#
#     print("==== PROGRAM SELESAI ===")


# try-except-else
try:
    angka = int(input("masukan angka: "))
except ValueError:
    print("input tidak valid")
else:
    print("angka yang anda masukan: ", angka)
    if angka > 0:
        print("angka positif")
    elif angka < 0:
        print("angka negatif")
    else:
        print("angka nol")
finally:
    print("program selesai")