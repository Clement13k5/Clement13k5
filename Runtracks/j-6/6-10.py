def mltp_intv (intv, tab):
  tab_inter=[]
  mltp=1
  for i in range(len(tab)):
    if intv[0]<=tab[i]<=intv[1]:
      tab_inter.append(tab[i])

  for j in range(len(tab_inter)):
    mltp=mltp*tab[j]
    
  return mltp

print(mltp_intv([5,15],[4,5,9,12,17,19]))