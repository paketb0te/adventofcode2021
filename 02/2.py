from os import linesep


with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

# Part 1

commands = [tuple(line.split()) for line in lines]

x = 0
y = 0

for command, value in commands:
    if command.lower() == "forward":
        x += int(value)
    if command.lower() == "down":
        y += int(value)
    if command.lower() == "up":
        y -= int(value)

print(x * y)

# Part 2

x = 0
y = 0
aim = 0

for command, value in commands:
    if command.lower() == "forward":
        x += int(value)
        y += int(value) * aim
    if command.lower() == "down":
        aim += int(value)
    if command.lower() == "up":
        aim -= int(value)

print(x * y)
