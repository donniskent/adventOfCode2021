dataset = []

while True: 
    try:
        line = input()
    except EOFError:
        break
    dataset.append(line)

binLength = len(dataset[0])
numOnes = 0
numZeros = 0
index = 0
ones = [0] * binLength
zeroes = [0] * binLength

for bin in dataset:
    
    for i in range(len(bin)):
        if bin[i] == "1":
            ones[i] += 1
        if bin[i] == "0":
            zeroes[i] += 1


print(ones[0])
print(zeroes[0])
gamma = ""
epsilon = ""
for i in range(len(ones)):
    print("zeroes", zeroes[i])
    print("ones", ones[i])
    if ones[i] > zeroes[i]:
        gamma += "1"
        epsilon +="0"
    else:
        gamma  += "0"
        epsilon +="1"

print(gamma,"\n")
print(epsilon)
print(len(ones))
print(len(zeroes))
