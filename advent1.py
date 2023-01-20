in_str = open ("input.txt", "r")
calories = 0
elves = []
for l in in_str:
    if (l == "\n"):
        elves.append(calories)
        calories = 0
    else:
        calories += int(l)




print ("calories = " + str(max(elves)) )
print ("top 3 = " + str(sum(sorted(elves)[-3:])))


in_str.close()
