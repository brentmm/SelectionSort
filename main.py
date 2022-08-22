from random import randint

#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a

#sorts list of random numbers
def selectionSort(c):
    n = len(c)
    for i in range(0, n):
        storedIndex = i
        for x in range(i + 1, n):  
            if c[storedIndex] > c[x]: #compares values
                storedIndex = x
        c[i], c[storedIndex] = c[storedIndex], c[i] #moves index to front of list
        print(c)
        print()

    return c

b = test()

print("Original: " + str(b))
print()
print("Sorted: " + str(selectionSort(b)))





























"""
M = len(C)-1
  nextValue = C[M]
  for i in range(0, M-1):
      if C[i] > nextValue:
          nextValue = C[i]
  while (M > 0) and (C[M] == nextValue):
      M = M - 1
  
  while M > 0:
      value = nextValue
      nextValue = C[M]
      for i in range(0, M-1):
          if C[i] == value:
              (C[i], C[M]) = (C[M], C[i])
              M = M-1
              print(C)
              print(M)
          elif C[i] > nextValue:
              nextValue = C[i]
      while M > 0 and C[M] > nextValue:
          M = M - 1
  return C"""