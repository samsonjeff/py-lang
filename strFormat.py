
print(r"Hello friend please enter the following!")
name = str (input("your name? "))
age = int (input("your age? "))
address = str (input("your address? "))

#two types of str format
print("\"Hello {0} your age is {1}, you live in {2},\"".format(name, age, address))
print(f"""okay {name} since you are {age}
how long you live in {address}?""")