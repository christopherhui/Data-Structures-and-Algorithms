def gallonSolver(fourGallon, threeGallon, target, cache):

  if fourGallon == target:
    return cache

  else:
    if fourGallon + 3 >= 4:
      cache.append(str(4 - fourGallon) + 'kg added to 4kg gallon, then emptied')
      cache.append(str(fourGallon - 1) + 'kg remaining from 3kg gallon')
      return gallonSolver(0, fourGallon - 1, target, cache)

    else:
      if threeGallon != 0:
        cache.append(str(fourGallon + threeGallon) + 'kg added to 4kg gallon')
        return gallonSolver(fourGallon + threeGallon, threeGallon, target, cache)
      else:
        cache.append(str(fourGallon + 3) + 'kg added to 4kg gallon')
        return gallonSolver(fourGallon + 3, threeGallon, target, cache)

print(gallonSolver(0,0,1,[]))

# jugOne > jugTwo
# Amount corresponds to each jug respectively

def gengallonSolver(jugOne, jugTwo, amountOne, amountTwo, target, cache):

  if amountOne == target:
    return cache

  else:

    if amountOne + jugTwo > jugOne:
      cache.append(str(jugOne - amountOne) + ' to jug ' + str(jugOne) + ' and emptied')
      cache.append(str(jugTwo - jugOne + amountOne) + ' remaining from ' + str(jugTwo) + ' gallon')

      return gengallonSolver(jugOne, jugTwo, 0, jugTwo - jugOne + amountOne, target, cache)

    else:
      if amountTwo != 0:
        cache.append(str(amountOne + amountTwo) + ' to jug ' + str(jugOne))
        return gengallonSolver(jugOne, jugTwo, amountOne + amountTwo, amountTwo, target, cache)
      else:
        cache.append(str(amountOne + jugTwo) + ' to jug ' + str(jugOne))
        return gengallonSolver(jugOne, jugTwo, amountOne + jugTwo, amountTwo, target, cache)

print(gengallonSolver(4,3,0,0,1,[]))

