status = 404

if status == 100:
    print("Continue")
elif status == 200:
    print("OK")
elif status == 300:
    print("Multiple Choices")
elif status == 400:
    print("Bad Request")
else:
    print("Something went wrong that I can't handle... :(")


match status:
    case 100:
        print("match: Continue")
    case 200:
        print("match: OK")
    case 300:
        print("match: Multiple Choices")
    case 400:
        print("match: Bad Request")
    case _:
        print("match: Something went wrong that I can't handle... :(")