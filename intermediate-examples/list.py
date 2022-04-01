mylist = ["banana", "cherry", "apple"]

# insert into position 4
mylist.insert(4, "blueberry")
print(mylist)

# last item
item = mylist[-1]
print(item)

# remove item
mylist.remove("cherry")

# if find banana print yes
if "banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

# reverse list
item = mylist.reverse()

# copy list without use the same mem address
list_copied = mylist.copy()
print(list_copied)

# clear all
item = mylist.clear()
