import random

def tebak_angka():

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

