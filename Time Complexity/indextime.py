import random
import time

def indexTime():
  for i in range(10000,1000002,10000):
    x = list(range(i))
    start = time.time()
    find = x[random.randrange(0,i)]
    end = time.time()
    print(end-start)

indexTime()