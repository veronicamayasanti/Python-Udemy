#funtion mengambil soal dari file bank_soal.txt
def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli


#function membuat soal
def buat_soal():
    soal_asli = ambil_soal()

    import random
    # untuk mengacak soal
    random.shuffle(soal_asli)

    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]  # pertanyaan | jawaban1,jawaban2,jawaban3,jawaban4
        data = soal.split("|") # ["pertanyaan, jawaban1,jawaban2,jawaban3,jawaban4"]

        pertanyaan = data[0] # pertanyaan
        semua_jawaban = data[1]  # jawaban1,jawaban2,jawaban3,jawaban4

        jawaban = semua_jawaban.split(",") # jadi array ["jawaban1", "jawaban2", "jawaban3", "jawaban4"]
        jawaban_benar = jawaban[0] # "jawaban1"

        # acak jawaban
        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan":  pertanyaan,  # Corrected key from "pertanyaan:" to "pertanyaan"
            "pertanyaan:" :  pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar  # Removed space at the end of the key
        })

    return soal_ujian

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]

    jawaban_benar = 0
    jawaban_salah = 0

    for i in range(len(soal_ujian)):
            soal = soal_ujian[i]
            print("Pertanyaan ", i + 1 ,":", soal["pertanyaan"])
            print("Jawaban:")
            for j in range(len(soal["jawaban"])):
                jawaban = soal["jawaban"][j]
                print(opsi[j],".", jawaban)

            jawaban_user = input("Pilih jawaban (A/B/C/D): ")
            jawaban_user_index = opsi.index(jawaban_user)
            jawaban_asli_user = soal["jawaban"][jawaban_user_index]

            if jawaban_asli_user == soal["jawaban_benar"]:
                print("Jawaban benar ")
                jawaban_benar += 1
            else:
                print("Jawaban salah ")
                jawaban_salah += 1

    print("Hasil Ujian")
    print("Jawaban Benar: ", jawaban_benar)
    print("Jawaban Salah: ", jawaban_salah)
    print("Hasil Ujian: ", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")

app_ujian()
