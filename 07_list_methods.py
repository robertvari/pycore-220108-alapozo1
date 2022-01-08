my_name = "Robert Vari"
names = ["Robert", "Kriszta", "Csaba", "Robert", my_name]

# add item to list
names.append("Balázs")
names.append("Tom")
names.append("Jane")
print(names)

names.insert(0, "John")
names.insert(3, "Csilla")
print(names)


# del, remove item from list
names.remove('Tom')
print(names)

del names[0]
print(names)

# removes the first occurrence
names.remove("Robert")
print(names)

names.clear()
print(names)