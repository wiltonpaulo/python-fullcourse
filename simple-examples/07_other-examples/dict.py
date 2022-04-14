print("Way to transform two lists into one dict")

purchases = ["rice", "beans", "pasta"]
prices = ["2.00", "3.80", "4.90"]

new_list = {}

# for x in range(len(purchases)):
#    new_list[purchases[x]] = prices[x]

# for id, item in enumerate(compras):
#    new_list[purchases[id]] = prices[id]

new_list = {item: prices[purchases.index(item)] for item in purchases}

# new_list = dict(zip(purchases, prices))

print(new_list)
