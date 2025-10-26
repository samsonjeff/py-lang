#mini game / guess and win nothing
pets = ["cat", "dog", "bird", "fish", "rabbit"]
guess_count = set()
life = 3
#sets of conditions
print("""GUESS & WIN NOTHING -- Game life: ❤️❤️❤️ """)
while life != 0:
    print(f"life: {life}")
    guess = str(input("guess a common pet in the house: ")).lower()

    if guess in pets:
        if guess not in guess_count:
            guess_count.add(guess)

        else:
            life -= 1
            print(f"already guessed that pet", end = " ")
#user score statement ↓↓↓
        if len(guess_count) == len(pets):
            print("You win nothing!")
            break
    else:
        life -= 1
    if life == 0:
        print(f"life: {life} \nbawi ka nalang next life!")
