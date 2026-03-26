
def app_tebak_angka():
    import random
    angka_acak = random.randint(1,10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan :
        tebakan += 1
        angka_user = int(input("masukan angka : "))
        if angka_user > angka_acak:
            print("Angka terlalu besar")
        elif angka_user < angka_acak:
            print("Angka terlalu kecil")
        else:
            print(f"selamat angka benar ")
            break
    else:
        print("kamu telah melewati maksimal tebakan anda")
        print(f"angka acak adalah {angka_acak}")

    input("enter untuk lanjut")

def app_menu_tebak_angka():
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("=== Program tebak angka selesai ===")
            break
        else:
            print("Error: Pilihan tidak valid")

app_menu_tebak_angka()