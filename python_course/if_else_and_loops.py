#--------------------- if-else ---------------------#

# a = 4
# b = 5
# if b > a:
#     print("b is greater than a")
# elif a > b:
#     print("a is greater than b")
# else: 
#     print(" a is equal to b")

# # all of the above is in a single line
# print("b is greater than a") if b > a else print("a is greater than b") if a > b else print("a equals to b")

# #if inside if condition
# if a >= b:
#     if a == b:
#         print("a equals to b")
#     else:
#         print("a > b")
# else:
#     print("a is less than b")

# # if conditions one by one
# if a > b:
#     print("a is greater than b")
# if a < b:
#     print("a is less than b")
# if a == b:
#     print("a is equal to b")

# # -------------------- loops --------------------#
# # for loop
# # while

# # Example 1: for loop to check if number is present in the list

# numbers = [1,2,3,4,5,6,7,8,9]
# flag = False
# for i in numbers:
#     if i == 8:
#         flag = True
# print("Number 8 present in list", flag)

# # Example 2:
# for i in range(0,10):
#     print(i)

# numbers = [1,255,3,543, 5, 6, 7, 8, 9]
# length_num_list = len(numbers)
# print(length_num_list)

# for i in range(0, length_num_list + 1):
#     print(i)

# for i in range(0,9):
#     print(i)

# for i in range(0, length_num_list):
#     print(i)
#     print(numbers[i])
#     print("------------")

# lst = [i for i in range(0,9)]
# print(lst)

# numbers = [103, 255, 56, 43, 53, 64, 72, 99]

# for idx, value in enumerate(numbers):
#     print(idx, value)
#     if idx==3:
#         print(value)


# #-----------------------while-loop-----------------------#

# count = 0
# while True:
#     print(count)
#     if count == 10:
#         break
#     count +=1

# a = 5
# b = 5
# while a == b:
#     for i in range(0,5):
#         a = 6
#         print(i, a)

# """
# *****
# ****
# ***
# **
# *
# """

# for i in range(0,5):
#     for j in range(0, 5-i):
#         if j == 4-i:
#             print("*")
#             continue
#         print("*", end='')

"""
*
**
***
****
*****
"""

"""
**********
 ********
  ******
   ****
    **
     *
"""
counter = 0
for i in range(0, 10, 2):
    for number in range(0, counter):
        print(" ", end='')
    for j in range(0, 10-i):
        if j == 9-i:
            print("*")
            continue
        print("*", end='')
    counter += 1
    if counter == 5:
        for number in range(0, counter):
            print(" ", end='')
            # print(counter)
        print("*")

    # print("", end='')




