def inverse(tab):
  tab_f=[]
  for i in range(1,len(tab)+1):
    tab_f.append(tab[-i])
  return tab_f

print([2,1,3,1])
print(inverse([2,1,3,1]))