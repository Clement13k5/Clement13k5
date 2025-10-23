nom="ordi"
prix=500
qte=10
print(nom, prix, qte)

qte+=5
achat=int(input("Combien voulez vous en acheter?"))
if achat>qte:
  print("Il n'y a pas assez de stock il reste seulement ", qte, "exemplaires")
else:
  qte-=achat
  prix=prix*1.1
print(nom, prix, qte)
