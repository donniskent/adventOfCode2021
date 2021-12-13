dataset = []

while True: 
    try:
        line = input()
    except EOFError:
        break
    dataset.append(line)
horizontal = 0
depth = 0
aim = 0
for i in dataset:
    splitter = i.split()
    direction = splitter[0]
    magnitude = int(splitter[1])
    print(direction)
    print(magnitude)
    if direction == "forward":
        horizontal +=magnitude
        depth += (aim * magnitude)
    elif direction == "down":
        aim+=magnitude
    elif direction == "up":
        aim-=magnitude

print(horizontal * depth)




