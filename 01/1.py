with open("1_input.txt", "r") as infile:
    values = infile.read().split("\n")


# simple loop
increased_count = 0
for a, b in zip(values[1:], values[:-1]):
    if int(a) > int(b):
        increased_count += 1
print(increased_count)

# more elegant mapping:
print(sum(map(lambda val: int(val[0]) > int(val[1]), zip(values[1:], values[:-1]))))
