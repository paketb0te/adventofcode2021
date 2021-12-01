with open("1_input.txt", "r") as infile:
    values = infile.read().split("\n")

# Part 1

print(3 * "~" + "Part 1" + 3 * "~")
# simple loop
increased_count = 0
for a, b in zip(values[1:], values[:-1]):
    if int(a) > int(b):
        increased_count += 1
print(increased_count)

# more elegant mapping:
print(sum(map(lambda val: int(val[0]) > int(val[1]), zip(values[1:], values[:-1]))))

# Part 2

print(3 * "~" + "Part 2" + 3 * "~")
# loop:

increased_count = 0
for i in range(len(values) - 3):
    a = int(values[i])
    b = int(values[i + 1])
    c = int(values[i + 2])
    d = int(values[i + 3])
    x = a + b + c
    y = b + c + d
    if y > x:
        increased_count += 1

print(increased_count)

# mapping:


def winsum(i: int, values: list) -> int:
    return sum(int(x) for x in values[i : i + 3])


print(sum([winsum(i + 1, values) > winsum(i, values) for i in range(len(values) - 3)]))
