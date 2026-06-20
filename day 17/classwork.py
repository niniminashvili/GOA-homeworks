# 1)
email = "random@gmail.com"
password = "12345"

user_email = input("enter email: ")
user_password = input("enter password: ")

while user_email != email or user_password:
    print("incorrect email or password ")
    user_email = input("enter email: ")
    user_password = input("enter password: ")

print("welcome!")

# 2)
for i in "group 91 is the best":
    print(i)