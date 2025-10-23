def anti_double(tab):
  
  for i in range(4):
    val=tab[i]
    for j in range(i,len(tab)-1):
      if tab[j]==val:
        tab.pop(j)
  return tab

print(anti_double([10,10,20,20,52,50,25,25]))