def fls (type,saison):
  if type=="legumes":
    if saison=="ete":
      return "artichaut, aubergine,navet"
    elif saison=="hiver":
      return "carotte, topinambour, endive"
    else:
      return "je sais pas je suis pas agriculteur"
  elif type=="fruits":
    if saison=="ete":
      return "Poire, fraise, cassis"
    elif saison=="hiver":
      return "orange, mandarine et kiwi"
    else:
      return "je sais pas je suis pas agriculteur"
  else:
    return "t'es khapta chef ?"
    

print(fls("legumes","ete"))
print(fls("legumes","hiver"))
print(fls("legumes","juin"))
print(fls("fruits","ete"))
print(fls("fruits","hiver"))
print(fls("fruits","primtemps"))
print(fls("jus","ete"))