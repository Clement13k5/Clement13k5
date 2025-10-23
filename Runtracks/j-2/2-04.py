n=int(input("Combien de table de multiplication voulez-vous ? "))
i=0
if n>0:
  while i<=n:
    print("La table de ", i)
    for j in range(11):
      print(j, "x", i, "=", j*i)
    i+=1
else:
  print("Choisissez un nombre non-nul")