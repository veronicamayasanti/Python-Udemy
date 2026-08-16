from calculator import operasi


if __name__ == "__main__":
    while True:
        print("=== PROGRAM KALKULATOR SEDERHANA ===")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. keluar")
        print("=== PROGRAM KALKULATOR SEDERHANA ===")

        try:
            pilihan = int(input("Pilihan: "))

            if pilihan == 1:
                operasi.app_penjumlahan()
            elif pilihan == 2:
                operasi.app_pengurangan()
            elif pilihan == 3:
                operasi.app_perkalian()
            elif pilihan == 4:
                operasi.app_pembagian()
            elif pilihan == 5:
                print("=== SAMPAI JUMPA LAGI ===")
                break
            else:
                print("Error: pilihan tidak valid")
        except ValueError:
            print("Error: masukan pilihan yang valid")
