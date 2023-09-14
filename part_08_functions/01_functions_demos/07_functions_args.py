# *args
def my_function(*languages):
    if len(languages) >= 3:
        print("My favorite language is " + languages[2])
    else:
        print("Not enough arguments")


def iterate_languages(*languages):
    print(languages)
    print(type(languages))
    for elem in enumerate(languages):
        print(elem, end=" ")


my_function("Python", "TypeScript", "Java")
iterate_languages("Python", "TypeScript", "Java", "GO", "PHP")
