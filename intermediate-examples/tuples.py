import sys
import timeit

# tuple is immutable, you cant change element item
mytuple = (["Max", 1, "John", 4])
print(type(mytuple))
print(mytuple[0])

mytuple = ('a', 'b', 'd', 'd', 'c', 'e', 'd')
print(mytuple.index('d'))
print(mytuple.count('d'))

# comparison tuples and lists
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list, "bytes"))
print(sys.getsizeof(my_tuple, "bytes"))  # smaller in mem
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # faster
