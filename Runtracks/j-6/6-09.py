def M (tab):
  M=tab[0]
  for i in range(1,len(tab)):
    if M<tab[i]:
      M=tab[i]
  return "le max est: ", M

def m (tab):
  m=tab[0]
  for i in range (1,len(tab)):
    if m>tab[i]:
      m=tab[i]
  return "le min est: ", m

print(M([1,2,3,4,5,6,7,8,9]))
print(m([1,2,3,4,5,6,7,8,9]))
