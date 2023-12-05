my_file = open("write_example.txt", "w")

list_of_students = ["Alex\n", "Komanov\n", "Python\n", "Java\n", "TS"]

my_file.writelines(list_of_students)
