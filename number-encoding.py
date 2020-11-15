def NumberEncoding(mystr):
    listStr = list(mystr)
    newList = []
    for itemStr in listStr:
        if itemStr.isalpha() == True:
            if itemStr.isupper() == True:
                newList.append(ord(itemStr) - 64)
            elif itemStr.islower() == True:
                newList.append(ord(itemStr) - 96)
        else:
            newList.append(itemStr)
    return "".join(map(str,newList))

# print(NumberEncoding('Db5c##'))
print('Running test cases ... ')
if NumberEncoding('af5c a#!') == '1653 1#!':
    print('Checking the result of algorithm NumberEncdoing of string "af5c a#!" is equal to "1653 1#!".\nTest passed')
else:
    print('Test failed')