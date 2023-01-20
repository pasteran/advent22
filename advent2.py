in_str = open ("input.txt", "r")
#move_score = {"X":1, "Y":2, "Z":3}
#round_score = {"C X":6, "C Y":0, "C Z":3, "B X":0, "B Y":3, "B Z":6, "A X":3, "A Y":6,"A Z":0}
move_score = {"X":0, "Y":3, "Z":6}
round_score = {"C X":2, "C Y":3, "C Z":1, "B X":1, "B Y":2, "B Z":3, "A X":3, "A Y":1,"A Z":2}

score = 0
for l in in_str:
    score += move_score[l[2]] + round_score[l[:-1]]

print ("final score is " + str(score))
