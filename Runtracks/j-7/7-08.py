def my_sort(lst):
  ancien_swap=0
  swap=1
  while swap-ancien_swap>=1:
    ancien_swap+=swap
    for i in range(len(lst)-1):
      if lst[i]>lst[i+1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
        swap+=1
  return lst, swap-1 

print(my_sort([11,90,25,12,22,34,64]))