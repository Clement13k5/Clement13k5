#ord(z) chr(172)
def chiffrage(mot,decalage):
  nv_mot=[]
  for caractere in mot:
    nb=ord(caractere)

    if nb+decalage>122:
      decal=26-decalage
      nv_mot.append(chr(nb-decal))
    elif nb==32:
      nv_mot.append(chr(nb))
    else:
      nv_mot.append(chr(nb+decalage))
  return "".join(nv_mot)

print(chiffrage("je m appelle cesar",15))