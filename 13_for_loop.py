names = ["robert", "csaba", "kriszta", "csilla", "Tom", "Balázs"]

for i in names:
    print(i)


for i in names:
    if i == "kriszta":
        break
    print(i)
    pass

for i in names:
    if i == "kriszta":
        continue
    print(i)

print("End of code")