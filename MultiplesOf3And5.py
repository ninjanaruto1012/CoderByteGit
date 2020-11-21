def SumOfMulti(num):
    listOfInterest = []
    for i in range(num):
        if ((i % 3) == 0) or ((i % 5) == 0):
            listOfInterest.append(i)
    return sum(listOfInterest)

print(SumOfMulti(1000))