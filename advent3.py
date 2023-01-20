from functools import reduce

in_file = open ("input.txt", "r")

def priority(item):
    b=1
    if item.islower():
        b-= ord("a")
    else:
        b-= ord("A")-26
    return ord(item)+b

def findItem(sack):
    return sameChar(sack[:int(len(sack)/2)],sack[int(len(sack)/2):])

def sameChar(str1, str2):
    for item in str1:
        if item in str2:
            return item

def sameChar3(str1, str2, str3):
    for item in str1:
        if item in str2:
            if item in str3:
                return item


badges = 0
#file_iter = iter(in_file)
for line in in_file:

    badges+= priority(sameChar3(line,in_file.readline(),in_file.readline()))

sum = reduce (lambda x,y: x + priority(findItem(y)) , [0] + in_file.read().splitlines())
    
print ("final sum is " + str(sum))
print ("badge sum is " + str(badges))
