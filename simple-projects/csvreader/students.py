import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "home"])
    write.writerow({"name": name, "home": home})
