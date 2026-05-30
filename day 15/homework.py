# 0) for ციკლი გამოიყენება მაშინ როდესაც წინასწარ ვიცით რამდენჯერ უნდა განმეორდეს მოქმედება
#    while ციკლი გამოიყენება მაშინ როდესაც არ ვიცით რამდენჯერ უნდა განმეორდეს მოქმედება 
#    და ციკლი უნდა გაგრძელდეს მანამ სანამ პრიობა ჭეშმარიტია

# 1)
for i in range(21):
    print(i)

# 2)
num = 10
while num < 46:
    print(num)
    num = 1

# 3)
for i in range(18, 61, 2):
    print(i)

# 4)
name = input("შეიყვანე სახელი: ")

for letter in name:
    print(letter)

# 5)
num = 10

while num > 0:
    print(num)
    num = num 

# 6)
email = "nini@gmail.com"
password = "12345"

user_email = input("შეიყვანე ემაილი: ")
user_password = input("შეიყვანე პაროლი: ")

while user_email != email or user_password != password:
 print("ემაილი არასწორია! ")

user_email = input("შეიყვანე ემაილი: ")
user_password = input("შიყვანე პაროლი: ")


