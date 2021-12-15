#pull in the data 
def counter(dataset, i):
    ones= 0
    zeroes = 0
    for bin in dataset:
        
    
        if bin[i] == "1":
            ones += 1
        if bin[i] == "0":
            zeroes += 1
    
    return [zeroes,ones]

def removal(numToRemove, index, dataset):
    for i in dataset[:]:
        print(i[index], "index before")
        if i[index] == numToRemove:
          # print(i[index], "index after")
           dataset.remove(i)
    return dataset


def oxygen(ones, zeroes, dataset,index):
    if ones >= zeroes: 
        #remove all the zeroes from the dataset 
        data = removal("0", index,dataset)
    else:
        #remove all the ones 
        data = removal("1", index, dataset)
    return data 

def carbon(ones, zeroes, dataset,index):
    if ones >= zeroes: 
        #remove all the zeroes from the dataset 
        data = removal("1", index,dataset)
    else:
        #remove all the ones 
        data = removal("0", index, dataset)
    return data
    
def forOxygen(dataset):
    i=0
    while len(dataset) > 1:
        
        b = counter(dataset, i)
        zeroes = b[0]
        ones = b[1]
        dataset = oxygen(ones, zeroes, dataset, i)
        print(len(dataset))
        print(dataset)
        
        i+=1
    return dataset

def forCarbon(dataset):
    i=0
    while len(dataset) > 1:
        
        b = counter(dataset, i)
        zeroes = b[0]
        ones = b[1]
        dataset = carbon(ones, zeroes, dataset, i)
        
        
        i+=1
    return dataset






def main():
    dataset1 = []
    dataset2 = []
    while True: 
        try:
            line = input()
        except EOFError:
            break
        
        dataset1.append(line)
        dataset2.append(line)

    
    oxy = forOxygen(dataset1)
    carb = forCarbon(dataset2)
    print(oxy)
    print(carb)

main()