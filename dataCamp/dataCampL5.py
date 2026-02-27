# manipulating lists

x = ["a","b","c","d","e"]
y = list(x)

ny = y + ["f"]
y = ny

del x[1]

print(x)
print(y)