#funtion mengambil soal dari file bank_soal.txt
def ambil_soal(lokasi_file):
    soal_asli = []
    with open(lokasi_file, "r") as file:
        for line in file:
            soal_asli.append(line.strip())
    return soal_asli


#function membuat soal
def buat_soal(lokasi_file):
    soal_asli = ambil_soal(lokasi_file)

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
