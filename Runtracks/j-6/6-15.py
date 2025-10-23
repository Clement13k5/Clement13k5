def arrondi (num):
  if num-int(num)<0.5:
    return int(num)
  else:
    return int(num)+1
  

def m (tab):
  m=tab[0]
  for j in range (1,len(tab)):
    if m>tab[j]:
      m=tab[j]
  return "le min est: ", m



def tri (tab):
  mini=0
  for i in range(len(tab)):
      mini=m(tab)
      tab[i],mini=mini,tab[i]
  return tab






tablo=[22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
tblo=[]
for i in range (len(tablo)):
  x=arrondi(tablo[i])
  tblo.append(x)
print(tblo)
print(tri(tblo))