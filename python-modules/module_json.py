import json
file = open("contoh.json", "r")
text = file.read()
file.close()

print(text)

murid = json.loads(text)
print(type(murid))
print(murid.get("nama"))
print(murid.get("umur"))
print(murid.get("nilai"))

sekolah = {
    "nama": "Universitas Programmer Zaman Now",
    "alamat" : "Jakarta",
    "jurusan" : [
        "Teknik Informatika",
        "Sistem Informasi"
    ]
}
text_json = json.dumps(sekolah)
print(text_json)

file = open("sekolah.json", "w")
file.write(text_json)
file.close()