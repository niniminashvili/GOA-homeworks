# 1)
my_name = "nini"

user_name = input("შეიყვანე სახელი: ")

if user_name == my_name:
    print("hello")
else:
    print("bye")

# 2)
my_number = 2

user_number = int(input("შიყვანე შენი საყვარელი რიცხვი: "))

if user_number == my_number:
    print("perfect")
elif user_number > my_number:
    print("more")
else:
    print("less")

# 3)
my_name = "nini"
my_age = 15

user_name = input("შეიყვანე სახელი: ")
user_age = int(input("შეიყვანე ასაკი: "))

if user_name == my_name and user_age == my_age:
    print("twins")
else:
    print("not twins")

# 4)
number = int(input("შეიყვანე რიცხვი: "))

if number % 3 == 0 and number % 5 == 0:
    print("რიცხვი არის 3_ის და 5_ის ჯერადი")
else:
    print("რიცხვი არ არის ერთდროულად 3_ის და 5_ის ჯერადი")

# 5)
password = input("შეიყვანე პაროლი: ")

if len(password) < 8:
    print("სუსტი პაროლი")
else:
    print("კარგი პაროლი")