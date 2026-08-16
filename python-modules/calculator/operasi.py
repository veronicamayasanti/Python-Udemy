def app_penjumlahan():
    print("=== PROGRAM PENJUMLAHAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 + angka2
        print(f"hasil penjumlahan: {hasil}")
    except ValueError:
        print("Error: masukan angka yang valid")
    print("=== program penjumlahan selesai ===")
    print("Enter untuk lanjut")

def app_pengurangan():
    print("=== PROGRAM PENGURANGAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 - angka2
        print(f"hasil pengurangan: {hasil}")
    except ValueError:
        print("Error: masukan angka yang valid")
    print("=== program selesai ===")
    print("Enter untuk lanjut")

def app_perkalian():
    print("=== PROGRAM PERKALIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 * angka2
        print(f"hasil perkalian: {hasil}")
    except ValueError:
        print("Error: masukan angka yang valid")
    print("=== program selesai ===")
    print("Enter untuk lanjut")

def app_pembagian():
    print("=== PROGRAM PEMBAGIAN ===")
    try:
        angka1 = int(input("angka1: "))
        angka2 = int(input("angka2: "))
        hasil = angka1 / angka2
        print(f"hasil pembagian: {hasil}")
    except ValueError:
        print("Error: masukan angka yang valid")
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol")
    print("=== program selesai ===")
    print("Enter untuk lanjut")
