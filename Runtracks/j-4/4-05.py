def calcule (num1, operateur, num2):
  if operateur=="+":
    return num1+num2   
  elif operateur=="-":
    return num1-num2
  elif operateur=="*":
    return num1*num2
  elif operateur=="/":
    return num1/num2
  else:
    return "l'operateur n'est pas un operateur "

print(calcule(4,"*",5))