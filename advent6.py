in_str = open ("input.txt", "r")
diff_size = 4
def alldiff (st):
    return len(set(st)) == len(st)
    

buffer = in_str.read(i:=diff_size-1)
    
while (c:=in_str.read(1)):
    i+=1
    #print((buffer + c))
    if (alldiff(buffer + c)):
        print (i)
        break
    else:
        buffer = buffer[1:] + c


print ("end = " + buffer+c)


in_str.close()
