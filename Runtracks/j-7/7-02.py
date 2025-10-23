def triangle (hauteur):
  espace=hauteur
  for i in range(hauteur):
    for k in range(espace):
      print(end=" ")
    espace-=1
    if i==hauteur-1:
      print(end="/")
      for x in range(hauteur-1):
        print(end="_")
        print(end="_")
      print("\\")
    else:
      
      print(end="/")
      for j in range(i):
        print(end=" ")
        print(end=" ")
      print("\\")
    
          

print(triangle(10))
