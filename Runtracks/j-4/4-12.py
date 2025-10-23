inversion=[]
def inverse (mot):
  for i in range(1,len(mot)+1):
      inversion.append(mot[-i])
  return ''.join(inversion)
print(inverse("salut"))