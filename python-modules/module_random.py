import random

print("random 1-10", random.randint(1, 10))
print("random 1-100", random.randint(1, 100))

list = ["veronica", "maya", "santi", "michelina"]
pilih = random.choice(list)
print("pilih dari list ", pilih)

random.shuffle(list)
print("list random ", list)
