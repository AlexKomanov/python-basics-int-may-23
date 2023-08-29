#Tuple definition

my_tuple=('Alex',5,35,False,'age',56)
print(my_tuple)

#converting tuple to list

my_list=list(my_tuple)
print(type(my_list))
print(my_list)

#Adding element by append()

my_list[2]=105
my_list.append(True)

#convert modified list to tuple again
my_tuple=tuple(my_list)
print(my_tuple)

#Converting a tuple to be alist by using * unpacking method

unpacked_list=[* my_tuple]
print(f"{unpacked_list= }")

