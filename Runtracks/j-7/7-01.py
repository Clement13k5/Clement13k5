def rectangle(hauteur,largeur):

  for i in range(hauteur):
    if i==0 or i==hauteur-1:
      print(end="|")
      for i in range (largeur):
        print(end="-")
      print("|")
    else:
      print(end="|")
      for i in range(largeur):
        print(end=" ")
      print("|")

print(rectangle(3,10))