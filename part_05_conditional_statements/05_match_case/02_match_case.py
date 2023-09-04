response_code = int(input("What's your response code? "))

match response_code:
    case 200:
        print("Everything's OK!")
    case 300:
        print("You're going somewhere else!")
    case 400:
        print("Uh oh. Are you lost?")
    case 500:
        print("Something went wrong!")
    case _:
        print("I don't know what you're talking about.")
