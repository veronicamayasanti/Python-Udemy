import datetime

sekarang = datetime.datetime.now()
print(f"sekarang : {sekarang}")


hari_ini = datetime.date.today()
print(f"hari ini {hari_ini}")

waktu_sekarang = datetime.datetime.now().time()
print(f"waktu sekarang {waktu_sekarang}")

ulang_tahun = datetime.date(2000, 1, 5)
print(f"ulang tahun {ulang_tahun}")

acara = datetime.datetime(2025, 10, 10, 20, 0, 0, 1)
print(f"acara {acara}")

print(f"format panjang, {sekarang.strftime('%a, %d %b %y')}")