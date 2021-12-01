with open("1_input.txt", "r") as infile:
    values = infile.read().splitlines()

# simple loop
increased_count = 0
for a, b in zip(values[1:], values[:-1]):
    if b > a:
        increased_count += 1
print(increased_count)

# more elegant mapping:
print(sum(map(lambda x: x[1] > x[0], zip(values[1:], values[:-1]))))
