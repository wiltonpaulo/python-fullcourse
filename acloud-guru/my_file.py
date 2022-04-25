my_file = open("xmen.txt", "w+")
my_file.write("Beast\n")
my_file.write("Phoenix\n")
my_file.writelines(["Cyclops\n", "Bishop\n", "Nightcrawler\n"])
my_file.close()


with open("xmen.txt", "r") as my_file:
    print(my_file.read())
    print("I'm reading again")
    print(my_file.read())
