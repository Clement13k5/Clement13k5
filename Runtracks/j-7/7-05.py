def gardien(nb_marches,h_marches):
  nb_marche_sem=35*nb_marches*2
  h_sem=h_marches*nb_marche_sem
  h_sem/=100
  print(f"Pour {nb_marches} de {h_marches}cm, le gardien parcours {h_sem}m par semaine")

print(gardien(50,17))