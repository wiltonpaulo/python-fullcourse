# Sets: unordered, mutable, do duplicates
myset = set()  # if you put only {} will be recognized as dict
myset = {1, 2, 3, 4, 5, 2, 2, 4}
myset.add(8)
myset.add(99)
myset.discard(2)
myset.pop()
print(myset)
myset.clear()
print(myset)


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# combine elements without duplicate them
u = odds.union(evens)
print(u)

# merge only items that appears in both set lists
i = evens.intersection(primes)
print(i)

# gets only the difference
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)
