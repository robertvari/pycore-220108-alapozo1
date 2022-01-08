phonebook = {
    "+36 20 234 5678": {
        "name": "Robert",
        "address": "Budapest",
        "email": "robert@gmail.com",
        "age": 34,
        "kids": 2
    },
    "+36 20 653 7865": {"name": "Csaba", "address": "Pécs", "email": "csaba@gmail.com", "age": 19}
}

phonebook["+36 20 653 9876"] = {"name": "Kriszta", "address": "Eger", "email": "kriszta@gmail.com", "age": 32}

phonebook["+36 20 234 5678"] = "Tom"

phonebook["+36 20 653 9876"]["name"] = "Csilla"

print(phonebook["+36 20 653 9876"])

del phonebook["+36 20 653 9876"]
print(phonebook)