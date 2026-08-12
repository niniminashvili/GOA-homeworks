# 0) სია არის მონაცემთა ტიპი რომელიც ინახავს რამდენიმე ელემენტს ერთ ცვლადში.
# სიას ვიყენებთ როცა გვინდა ერთ ადგილას შევინახოთ ბევრი მონაცემი.

# 1)
names = ["nini", "mari", "ani"]

# 2)
numbers = [10, 20, 30, 40, 50]
print(numbers[2])

# 3)
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[5])
print(numbers[-1])

# 4)
colors = ["black," "white", "grey"]
colors[0] = "red"
print(colors)

# 5)
names = ["sali", "taso", "gvanca", "lika"]

index = int(input("შეიყვანე ინდექსი: "))

if index > 4:
    print("index out of range")
elif index < 0:
    print("only positive index")
else:
    print(names[index])