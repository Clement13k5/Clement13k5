def nb_mltp_trs (tab):
  nb=0
  for i in range(len(tab)):
    if tab[i]%3==0:
      nb+=1
  return "nb mltp 3: ", nb
print(nb_mltp_trs([9,6,2,4,57,33]))
