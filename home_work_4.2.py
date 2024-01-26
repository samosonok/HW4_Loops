# For a list of integers, you need to find the sum of elements with even indices [0th, 2nd, 4th, etc.],
# and then multiply this sum by the last element of the input array.
# Don't forget that the first element of the array has index 0.
# For an empty array, the result is always 0.
#
# Explanation:
# [0, 1, 7, 2, 4, 8] -> (0 + 7 + 4) * 8 = 88
# [1, 3, 5] -> 30
# [6] -> 36
# [] -> 0
#
# To check the correctness of your code, use the examples above.
# There is no need to request input from the user.

list_of_num = [0, 1, 7, 2, 4, 8]

sum_of_numbers = 0
if not list_of_num:
    print(0)
else:
    for number in list_of_num:
        if list_of_num.index(number) % 2 == 0:
            sum_of_numbers += number
    print(sum_of_numbers * list_of_num[-1])
