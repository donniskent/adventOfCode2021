dataset = []

while True: 
    try:
        line = input()
    except EOFError:
        break
    dataset.append(int(line))


numGreater = 0
for i in range(len(dataset)-3):
    firstThree = dataset[i] + dataset[i+1] + dataset[i+2]
    nextThree = dataset[i+1] + dataset[i+2] + dataset[i+3]
    if nextThree > firstThree:
        numGreater+=1



print(numGreater)
