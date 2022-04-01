mydict = {"name": "Wilton", "age": 39, "city": "Sao Paulo"}

print(mydict["name"])
print(mydict)


if "Sao Paulo" in mydict.values():
    print(f'{mydict["name"]} lives in {mydict["city"]}')


for key in mydict:
    print(f"{key}: {mydict[key]}")

for key, value in mydict.items():
    print(key, value)


# copy dict
mydict_cpy = dict(mydict)
mydict_cpy = dict(name="Joseph", age=22, city="New York")
# remove last item
mydict_cpy.popitem()


print(mydict)
print(mydict_cpy)
