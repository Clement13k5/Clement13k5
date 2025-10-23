def tapis (taille):

  print(end="+")
  for i in range (taille+1):
    print(end="-")
  print("+")

  for y in range(taille):
    print(end="|")
    for k in range(taille):
      if k == taille - 1 - y:
        print(" ", end="")
      else:
        print("#", end="")
    print("|")

  print(end="+")
  for i in range (taille+1):
    print(end="-")
  print("+")




  



print(tapis(50))