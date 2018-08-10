import random

def smallestkNumber(k, alist):
  alist.sort()
  if k > len(alist) or k == 0:
    return None
  return alist[k-1]

def test():
  for i in range(1000, 100000, 3000):
    x = list(range(i))
    print(smallestkNumber(random.randrange(1, i+1), x))

test()