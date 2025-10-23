def plus_ou_moins (nombre):
  if nombre>=0:
    return "Positif"
  else:
    return "Negatif"
  

def pairs_impairs (num):
  if num%2==0:
    if plus_ou_moins(num)=="Positif":
      return "Nombre pair et positif"
    else:
      return "Nombre pair et negatif"
  else:
    if plus_ou_moins(num)=="Positif":
      return "Nombre impair et positif"
    else:
      return "Nombre impair et negatif"
    
print(pairs_impairs(5))
print(pairs_impairs(-5))
print(pairs_impairs(10))
print(pairs_impairs(-10))