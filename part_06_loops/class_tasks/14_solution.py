for i in range(1, 10):
    print(i, end=" ")
    for j in range(1, 10):
        # print("{:3d}".format(i * j), end=" ")  #  double-digit numbers
        print(i * j, end="\t")
    print()

# for i in range(1, 10):
#     for x in range(1, 10):
#         print("\t", i * x, end="\t")
#     print()
