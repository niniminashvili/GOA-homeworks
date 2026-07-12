# 1)
# პირობით განცხადებებს ვიყენებთ იმისთვის რომ პროგრამამ შეამოწმოს 
# პირობა და ამის მიხედვით შეასრულოს სხვადასხვა მოქმედება.

# სტრუქტურა:
# if : პირველი პირობა
# elif : დამატებითი პირობა
# else : სხვა ყველა შემთხვევა

# 2)
age = int(input("შეიყვანე ასაკი: "))

if age > 18:
    print("გამარჯობა")
elif age == 18:
    print("როგორ ხარ")
else:
    print("ნახვამდის")

# 3)
name = input("შეიყვანე სახელი: ")

if name == "vano":
    print("mentor")
elif name == "giorgi":
    print("assistant")
elif name == "nika":
    print("leader control")
else:
    print("student")

# 4)
email = "random@gmail.com"
password = "random123"

user_email = input("შეიყვანე ემაილი: ")
user_password = input("შეიყვანე პაროლი: ")

if user_email == email and user_password == password:
    print("correct info")
else:
    print("incorrect credentials")