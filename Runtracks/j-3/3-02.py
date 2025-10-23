age=int(input("T'a quel age chef? "))
if age>=18:
  print("Vas voter chef")
else:
  print("T'a pas le droit de vote chef")








def droit_de_vote(age):
  if age>=18:
    return "Vas voter chef"
  else:
    return "T'a pas le droit de vote chef"

print(droit_de_vote(19))
print(droit_de_vote(15))