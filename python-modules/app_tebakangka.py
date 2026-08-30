from tebak_angka import app

if __name__ == "__main__":
    while True:
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("=== PROGRAM TEBAK ANGKA SEDERHANA ===")

        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
           app.tebak_angka()
        elif pilihan == 2:
            print("=== Program tebak angka selesai ===")
            break
        else:
            print("Error: Pilihan tidak valid")
