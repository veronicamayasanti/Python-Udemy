for i in range(5):
    print("Hello python")
    print(i)


for i in range(2, 6):
    print("range", i)

for i in range(10, 0, -1):
    print("range -1 ", i)

#for loop dengan string
#for loop juga bisa digunakan untuk mengiterasi setiap karakter dalam string

nama = "python"
for huruf in nama :
    print(huruf)

nama = input("masukan nama : ")
for huruf in nama:
    print("-", huruf)