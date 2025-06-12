# ternary / conditional expression in function
def even():
    userInput = int(input("Enter a number: "))
    print(f"{userInput} is EVEN" if is_even(userInput) else f"{userInput} is ODD")

def is_even(number):
    return number % 2 == 0
#calling particular function
even()
