v1=int(input("choisissez la v1: "))
v2=int(input("choisissez la v2: "))
if v1==v2:
  print("les valeurs sont egal")
else:
  print("les valeurs ne sont pas egal")

def egaux (val1, val2):
  if val1==val2:
    return True
  else:
    return False
  

print(egaux(2,2))
print(egaux(2,8))