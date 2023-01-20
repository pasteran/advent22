import re

def move(num, fro, to):
    #print(fro,to)

    for i in range(0,num):
        to.append(fro.pop(i-num))
   # print(fro,to)


txt_file = open("input.txt", "r")
[stacks_str, moves_str] = txt_file.read().split("\n\n")
[stacks_str, cols] = stacks_str.rsplit("\n",1)
line_len = len(cols)
stacks = []
for j in range(1,line_len,4):
    stack_str = stacks_str[j::line_len+1].strip(" ")
    stacks.append(list(stack_str[::-1]))
print (stacks)
moves = moves_str.split("\n")
moves.pop()
#print(moves)
for move_str in moves:
    #print(move_str)
    [num, fro, to] = re.findall("\d+", move_str)
    move(int(num), stacks[int(fro)-1], stacks[int(to)-1])
print(stacks)
print("".join([stack[-1] for stack in stacks]))
