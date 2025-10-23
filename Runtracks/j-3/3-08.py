c1=float(input("cote1: "))
c2=float(input("cote2: "))
c3=float(input("cote3: "))

if c1>c2 and c1>c3:
  if c2+c3>c1:
    print("c'est un triangle")
    if c2**2+c3**2==c1**2:
      print("triangle rectangle")
    elif c1==c2 and c1==c3:
      print("triangle equilateral")
    elif c1==c2 or c1==c3 or c3==c2:
      print("isocele")
    else:
      print("triangle quelconque")
  else:
    print("c'est pas un triangle")
elif c2>c1 and c2>c3:
  if c1+c3>c2:
    print("c'est un triangle")
    if c1**2+c3**2==c2**2:
      print("triangle rectangle")
    elif c1==c2 and c1==c3:
      print("triangle equilateral")
    elif c1==c2 or c1==c3 or c3==c2:
      print("isocele")
    else:
      print("triangle quelconque")
  else:
    print("c'est pas un triangle")
else:
  if c2+c1>c3:
    print("c'est un triangle")
    if c2**2+c1**2==c3**2:
      print("triangle rectangle")
    elif c1==c2 and c1==c3:
      print("triangle equilateral")
    elif c1==c2 or c1==c3 or c3==c2:
      print("isocele")
    else:
      print("triangle quelconque")
  else:
    print("c'est pas un triangle")