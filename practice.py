# https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 1
# print("Twinkle, Twinkle, little star, \n\tHow I wonder what your are!\n\t\tUp abouve the world so hight,\n\t\tLike a diamond in the ske.\ntwinkle, twinkle, little star,\n\tHow I wonder what your are")

# 2
# import sys
# print(sys.version_info)

# 3
# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))

# 4
# import math
# r = float(input("please input a radius: "))
# print(
#     f"the area of the circle with radius {r} is : " + str(round(r**2*math.pi, 4)))

# 5
# fname = input("input your first name:")
# lname = input("input your last name:")
# print("your name is " + lname + " " + fname)

# 6
# values = input("input some comma seprated numbers:")
# list = values.split(",")
# tuple = tuple(list)
# print("list ", list)
# print("tuple", tuple)

# 7
# filename = input("input the filename: ")
# f_extns = filename.split(".")
# print("the extension of the file is", repr(f_extns[-1]))

# 8
# color_list = ["red", "blue", "yellow", "purple", "green"]
# print("%s %s" % (color_list[0], color_list[-1]))

# 9
# exam_st_date = (11, 12, 2014)
# print("the exam will start from : %s/%s/%s" % (exam_st_date))

# 10
# n = int(input("input a number: "))
# n1 = int("%s" % n)
# n2 = int("%s%s" % (n, n))
# n3 = int("%s%s%s" % (n, n, n))
# print(n1 + n2 + n3)

# 11
# print(abs.__doc__)

# 12
# import calendar
# y = int(input("enter the year: "))
# m = int(input("enter the month: "))
# print(calendar.month(y, m))

# 13
# print("""
# a string that you "don't" have to escape
# This
# is a ...... multi-line
# heredoc string -------> example
# """)

# 14
# from datetime import date
# f_date = date(2019, 7, 1)
# l_date = date(2023, 2, 24)
# print(l_date - f_date)

# 15
# import math
# r = 6
# volume = round(4/3*math.pi*r**3, 2)
# print(volume)

# 16
# while True:
#     num = int(input("input a number: "))
#     if num > 17:
#         print((num - 17)*2)
#     elif num == 17:
#         break
#     else:
#         print(abs(num - 17))

# 17
# def near_thousand(n):
#     return abs(1000-n) <= 100 or abs(2000-n) <= 100
# print(near_thousand(2101))

# 18
# def sum(n1, n2, n3):
#     if n1 == n2 == n3:
#         return (n1+n2+n3)*3
#     else:
#         return n1+n2+n3

# print(sum(3, 3, 3))

# 19
# def add_is(text):
#     if len(text) > 2 and text[0:2] == "Is":
#         return text
#     return "Is" + text


# print(add_is("arina"))

# 20
# def string_3(text, n):
#     print(text*n)


# string_3("hello", 15)

# def three_string(text, n):
#     result = ""
#     for i in range(n):
#         result += text
#     return result


# print(three_string("hello", 3))

# 21 determines whether a given number(accepted from the user) is even or odd, and prints an appropriate message to the user
# def even_or_odd(n):
#     if n % 2 == 0:
#         print(n, "is even")
#     else:
#         print(n, "is odd")


# even_or_odd(9)

# 22 count the number 4 in a given list
# num = 4
# count = 0
# mylist = [1, 4, 3, 7, 4, 9, 4, 4, 4]
# for index in mylist:
#     if index == num:
#         count += 1
# print(count)

# 23 get n(non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

def times(inputStr, n):
    if len(inputStr) > 2:
        return inputStr[:2]*n
    else:
        return inputStr*n


print(times("hcaa", 5))
