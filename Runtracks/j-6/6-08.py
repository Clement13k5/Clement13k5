def som_paire (lst):
  lst_f=[]
  for i in range(0,len(lst),2):
    nb_paire=0
    nb_paire=lst[i]+lst[i+1]
    lst_f.append(nb_paire)  
  return lst_f
print(som_paire([1,0,2,1,1,0,1,1]))