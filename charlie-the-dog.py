import itertools

def move_and_return(d, e):
    dist1 = d[0] - e[0]
    dist2 = d[1] - e[1]
    dist = abs(dist1) + abs(dist2)
    return int(dist)

def CharlieTheDog(strArr):
    mydict = [
        [{"content": "", "coor": (0, 0)}, {"content": "", "coor": (0, 1)}, {"content": "", "coor": (0, 2)},
         {"content": "", "coor": (0, 3)}],
        [{"content": "", "coor": (1, 0)}, {"content": "", "coor": (1, 1)}, {"content": "", "coor": (1, 2)},
         {"content": "", "coor": (1, 3)}],
        [{"content": "", "coor": (2, 0)}, {"content": "", "coor": (2, 1)}, {"content": "", "coor": (2, 2)},
         {"content": "", "coor": (2, 3)}],
        [{"content": "", "coor": (3, 0)}, {"content": "", "coor": (3, 1)}, {"content": "", "coor": (3, 2)},
         {"content": "", "coor": (3, 3)}],

    ]
    food_locations = []
    charlie_locations = []
    home_locations = []
    lengths = []
    for index in range(len(strArr)):
        tmplist = list(strArr[index])
        for subindex in range(len(tmplist)):
            mydict[index][subindex]["content"] = tmplist[subindex]
            if mydict[index][subindex]["content"] == 'F':
                food_locations.append(mydict[index][subindex]["coor"])
            elif mydict[index][subindex]["content"] == 'C':
                charlie_locations.append(mydict[index][subindex]["coor"])
            elif mydict[index][subindex]["content"] == 'H':
                home_locations.append(mydict[index][subindex]["coor"])
    list_perm = list(itertools.permutations(food_locations))

    for i in range(len(list_perm)):
        list_perm[i] = list_perm[i][:0] + (tuple(charlie_locations[0]),) + list_perm[i][0:] + (tuple(home_locations[0]),)

    for i in range(len(list_perm)):
        length = 0
        for j in range(len(list_perm[i]) - 1):
            length += move_and_return(list_perm[i][j], list_perm[i][j+1])
        lengths.append(length)
    return min(lengths)


print('Running test cases ... ')
if CharlieTheDog(['FOOF','OCOO','OOOH','FOOO']) == 11:
    print('Checking the result of algorithm Charlie the Dog of list ["FOOF","OCOO","OOOH","FOOO"] is equal to 11.\nTest passed')
else:
    print('Test failed')