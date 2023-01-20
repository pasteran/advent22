from functools import reduce
import re

in_file = open ("input.txt", "r")

def isContained (a,b,c,d):
# a-b contained in c-d
    if ((a>=c) and (b<=d)):
        #print (a,b,c,d)
        return True
    return False

def overLaps (a,b,c,d):
    if (a>=c) and (a<=d):
        return True
    return False
        
def parseNCheck (line):
   # [first, second] = line.split(",")
    [minfirst,maxfirst,minsecond,maxsecond] = [int(x) for x in re.findall("\d+", line)]
    if overLaps(minfirst,maxfirst,minsecond,maxsecond) or overLaps(minsecond,maxsecond,minfirst,maxfirst):
        return True
    return False

contained = filter (parseNCheck , in_file.read().splitlines())
    
print ("final sum is " + str(len(list(contained))))
