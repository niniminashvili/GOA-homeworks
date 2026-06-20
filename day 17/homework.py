# 0)
for i in range(20):
    print("Nini")

# 1)
total = 0

while total < 20:
    print("Nini")
    total += 1

# 2)
num1 = int(input("შეიყვანე პირვეელი რიცხვი: "))
num2 = int(input("შიყვანე მეორე რიცხვი: "))

for i in range(num1, num2 + 1):
    print(i)

# 3)
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))

while num1 != num2:
    print("რიცხვები არ ემთხვევა, თავიდან სცადე.")

    num1 = int(input("შეიყვანე პირველი რიცხვი: "))
    num2 = int(input("შეიყვანე მეორე რიცხვი: "))

print("რიცხვები დაემთხვა!")