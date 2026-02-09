word = "Hello World!"
reverseWord = ""

# for char in word:
#     reverseWord = char + reverseWord

# print(reverseWord)

for letter in range(len(word) -1, -1, -1):
    reverseWord += word[letter]

print(reverseWord)

# ------------ while loop ----------------

word = "Logic"
reversed_word = ""

# 1. Start at the last index
index = len(word) - 1

# 2. Keep going as long as the index is 0 or higher
while index >= 0:
    reversed_word += word[index]  # Add the letter
    index -= 1                     # 3. Manually move the pointer backward

print(reversed_word) # Output: cigoL
