def my_function(food):
    print(food)
    print(type(food))
    for element in food:
        print(element)


fruits = ["apple", "banana", "cherry"]
fruits_tuple = ("apple", "banana", "cherry")

text = 'alex'

my_function(fruits)
my_function(fruits_tuple)
my_function(text)


