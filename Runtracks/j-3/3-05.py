def is_prime(i) :
  for j in range(2,i) :
    if (i%j) == 0 :
      return False
  return True

for i in range(1,1001):
  if is_prime(i)==True:
    print(i)