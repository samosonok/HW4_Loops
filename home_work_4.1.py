# Write a program that moves all zeros to the end of the list.
# Your task is to modify the list so that all zeros end up at the end of the list.
# The order of non-zero numbers should be preserved!
#
# Example:
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
#
# To check the correctness of your code, use the examples above.
# There is no need to request input from the user.

list_of_numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for number in list_of_numbers:
    if number == 0:
        list_of_numbers.remove(number)
        list_of_numbers.append(number)

print(list_of_numbers)
