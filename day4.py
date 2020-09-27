first = 145852
last = 616942

def createList(r1, r2):  
  res = [] 
  while(r1 < r2+1): 
    res.append(r1) 
    r1 += 1
  return res

input = createList(first,last)

def ListOfStrings(input):
  stringlist = []
  for i in input:
    x = str(i)
    stringlist.append(x)
  return stringlist

inputX = ListOfStrings(input)

def Deconstruct(input):
  deco_list = []
  for obj in input:
    deco_obj = []
    deco_list.append(deco_obj)
    for i in obj:
      deco_obj.append(int(i))
  return deco_list

listXX = Deconstruct(inputX)

def non_decreasing(L):
  return all(x<=y for x, y in zip(L, L[1:]))

def Decrease(L):
  decrease_output = []
  for i in range(len(L)):
    if non_decreasing(L[i]) == True:
      decrease_output.append(L[i])
    else:
      None
  return decrease_output

def same_numbers(L):
  return any(x==y for x, y in zip(L, L[1:]))

def Nextnumbers(L):
  next_output = []
  for i in range(len(L)):
    if same_numbers(L[i]) == True:
      next_output.append(L[i])
    else:
      None
  return next_output

decreased_list = Decrease(listXX)
result = Nextnumbers(decreased_list)
print(len(result))