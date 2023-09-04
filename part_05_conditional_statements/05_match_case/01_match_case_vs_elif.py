language_2 = input("Which language do you want to learn: ")

if language_2 == "JavaScript":
    print("You can be a frontend developer.")
elif language_2 == "Python":
    print("You can be a backend developer.")
elif language_2 == "Flutter":
    print("You can be a mobile developer.")
elif language_2 == "Java":
    print("You can be an automation developer.")
else:
    print("Sorry, I don't know that language. Please try again.")

language = input("Which language do you want to learn: ")

match language:
    case "JavaScript":
        print("You can be a frontend developer.")
    case "Python":
        print("You can be a backend developer.")
    case "Flutter":
        print("You can be a mobile developer.")
    case "Java":
        print("You can be an automation developer.")
    case _:
        print("Sorry, I don't know that language. Please try again.")
