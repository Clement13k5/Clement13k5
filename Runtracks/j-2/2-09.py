for i in range(1,31,2):
  print("impairs: ", i)

for j in range(2,31,2):
  print("pairs: ", j)


x=1
while x<=30:
  print("impairs: ", x)
  x+=2

y=2
while y<=30:
  print("pairs: ", y)
  y+=2


a=1
while a<=30:
  if a%2==0:
    print("pairs:", a )
    a+=1
  else:
    print("impairs :",a)
    a+=1