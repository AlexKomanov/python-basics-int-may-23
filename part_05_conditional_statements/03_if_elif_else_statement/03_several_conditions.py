experience = int(input("Enter your experience: "))
language = input("Enter your language: ")

# if experience >= 3 and language == "Python":
#     print("You're matching a Python job!")
# elif experience >= 2 and language == "Java":
#     print("You're matching a Java job!")
# elif experience >= 5 and language == "JavaScript":
#     print("You're matching a JavaScript job!")
# else:
#     print("You need to improve your skills!")


if experience >= 2:
    if language == "Java" or language == "JavaScript":
        print("You're matching a job!")
    elif language == "Python":
        print("You're matching a job!")
    else:
        print("Not required languages")
else:
    print("You need to improve your skills!")
