def reussite_test(note_eleve):

  nb_tb_cq_un=(note_eleve//5)+1
  nb_sup=nb_tb_cq_un*5
  print(nb_sup)
  if note_eleve-nb_sup<3:
    note_eleve+=nb_sup

  if note_eleve>=40:
    return "test reussi!"
  else:
    return "test echoue gros nullos!"
  
  
print(reussite_test(83))   