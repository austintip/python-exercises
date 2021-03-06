# Write a method called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

# def multiply_by(list, num):
# # multiply by num for each number in the list.
#     for i in list:
#         list = [i] * num
#     print(list)
def multiply_by(list, num):
    my_new_list = [i * num for i in list]
    print(my_new_list)


multiply_by([1, 2, 3], 12)