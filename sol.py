def Coin_Combinations(coins, value):
  """
    A Generalized solution to the coins problem provided by project euler #31
    Read it for more specifications
    coins: a list of coins that can be used
    value: the value that the coins should add to
    returns:
     number of possible combinations to make value with givin coins in "coins"
  """
  coins.sort()
  l = [0]*(value+1)
  l[0] = 1
  for c in coins :
    for i in xrange(c,value+1) :
        l[i] += l[i-c]
  return l[-1]
