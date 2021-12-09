dataset = []

while True: 
    try:
        line = input()
    except EOFError:
        break
    dataset.append(int(line))


numGreater = 0
for i in range(len(dataset)-1):
    
    if dataset[i] < dataset[i+1]:
        numGreater+=1



print(numGreater)
