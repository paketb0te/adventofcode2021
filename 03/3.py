with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

# Part 1

a = [[int(char) for char in line] for line in lines]

result = []
half = len(lines) // 2

for position in zip(*a):
    x = sum(position)
    result.append(int(x > half))

gamma = int("".join(str(x) for x in result), 2)

epsilon = int("".join(str(int(not bool(x))) for x in result), 2)

print(gamma * epsilon)
