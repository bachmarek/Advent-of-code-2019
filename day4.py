first = 145852
last = 616942

def PartOne(L):
  n = [x for x in str(L)]
  if (n[0] > n[1] or n[1] > n[2] or n[2] > n[3] or n[3] > n[4] or n[4] > n[5]):
    return False
  if (
      not(n[0] == n[1] ) and
      not(n[1] == n[2] and n[1] != n[0]) and
      not(n[2] == n[3] and n[2] != n[1]) and
      not(n[3] == n[4] and n[3] != n[2]) and
      not(n[4] == n[5] and n[4])):
    return False
  else: 
    return True

answer1 = 0
num = first
while num < last:
  if PartOne(num) == True:
    answer1 +=1
  num +=1

def PartTwo(L):
  n = [x for x in str(L)]
  if (n[0] > n[1] or n[1] > n[2] or n[2] > n[3] or n[3] > n[4] or n[4] > n[5]):
    return False
  if (
      not(n[0] == n[1] and n[0] != n[2]) and
      not(n[1] == n[2] and n[1] != n[0] and n[1] != n[3]) and
      not(n[2] == n[3] and n[2] != n[1] and n[2] != n[4]) and
      not(n[3] == n[4] and n[3] != n[2] and n[3] != n[5]) and
      not(n[4] == n[5] and n[4] != n[3])):
    return False
  else: 
    return True

answer2 = 0
number = first
while number < last:
  if PartTwo(number) == True:
    answer2 +=1
  number +=1

print("Part 1: " + str(answer1))
print("Part 2: " + str(answer2))
