limit=int(input())
#first half
for i in range(1,limit+1):
  for j in range(limit-i):
    print(end=" ")
  num=1
  for number in range(2*i-1):
    print(end=str(num))
    if number+1 >= i :
      num = num-1
    else:
      num = num + 1
  print()
#second half
for i in range(1,limit):
  for j in range(i):
    print(end=" ")
  num=1
  for number in range(2*(limit-i)-1):
    print(end=str(num))
    if number  >= i:
      num = num - 1
    else:
      num = num + 1
  print()
