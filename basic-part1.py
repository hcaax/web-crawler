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

# def times(inputStr, n):
#     if len(inputStr) > 2:
#         return inputStr[:2]*n
#     else:
#         return inputStr*n


# print(times("hcaa", 5))

# 24 a passed letter is a vowel or not
# def is_vowel(char):
#     all_volwers = "aeiou"
#     return char in all_volwers

# print(is_vowel("c"))
# print(is_vowel("e"))

# 25
# def is_contained(n, group_data):
#     for value in group_data:
#         if n == value:
#             return True
#     return False

# print(is_contained(9, [1, 3, 5, 7]))

# 26 create a histogram from a given integers
# def histogram(items):
#     for n in items:
#         output = ""
#         while n > 0:
#             output += "*"
#             n -= 1
#         print(output)


# histogram([7, 9, 5, 3, 2])

# 27 concatenates all elements in a list  into a string and returns it.
# def intoString(ls):
#     string = ""
#     for n in ls:
#         string += str(n)
#     return string

# print(intoString(["a", "b", "c", "d", "e", "f","g"]))
# print(intoString([1, 3, 5, 7, 9]))

# 28 print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# def evenNumbers237(list):
#     for x in list:
#         if x == 237:
#             print(x)
#             break
#         elif x % 2 == 0:
#             print(x)


# evenNumbers237([3, 5, 17, 24, 237, 999, 834, 108, 100, 40, 20, 26])

# 29 prints out all colors from color_list_1 that are not present in color_list_2.
# color_list_1 = set(["black", "white", "red"])
# color_list_2 = set(["red", "green"])
# print(color_list_1)
# print(color_list_2)
# print(color_list_1.difference(color_list_2))
# print(color_list_2.difference(color_list_1))

# 30 accept the base and height of a triangle and compute its area.
# def triangleArea(base, height):
#     area = (base * height)/2
#     return area

# print(triangleArea(20, 10))

# 31 computes the greatest common divisor(GCD) of two positive integers.

# def gcd(x, y):
#     gcd = 1
#     if x % y == 0:
#         return y
#     elif y % x == 0:
#         return x
#     for k in range(int(x/2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd

# print(gcd(66, 99))

# 32 find the least common multiple (LCM) of two positive integers.
# def lcm(x, y):
#     if x > y:
#         z = x
#     else:
#         z = y

#     while(True):
#         if z % x == 0 and z % y == 0:
#             lcm = z
#             break
#         z += 1
#     return lcm
# print(lcm(33, 20))

# 33 sum three given integers. However, if two values are equal, the sum will be zero.
# def sum(x, y, z):
#     if x == y or y == z or x == z:
#         sum = 0
#     else:
#         sum = x + y + z
#     return sum

# print(sum(1, 2, 3))

# 34 sum two given integers. However, if the sum s between 15 and 20 it will return 20.
# def sum(x, y):
#     if x + y in range(15, 20):
#         return 20
#     return x + y

# print(sum(10, 13))

# 35 returns true if two given integer are equal or their sum or difference is 5.
# def equalOrFive(x, y):
#     if x == y or (x+y) == 5 or abs(x-y) == 5:
#         return True
#     else:
#         return False


# print(equalOrFive(-7, 3))

# 36 add two objects if both objects are integers.
# def addInt(x, y):
#     if type(x) == int and type(y) == int:
#         return x + y
#     else:
#         return "not both int"
# def addInt(x, y):
#     if not (isinstance(x, int) and isinstance(y, int)):
#         return "they should be integers"
#     else:
#         return x + y
# print(addInt(30.1, 7))

# 37 displays your name, age, and address on three different lines.
# def info(name, age, addr):
#     # print("name: {}\nage: {}\naddress: {}".format(name, age, addr))
#     print(f"name: {name}\nage: {age}\naddress: {addr}")

# info("arina", 25, "tokyo")

# 38 solve (x + y)*(x + y)
# x, y = 4, 3
# result = x*x + 2*x*y + y*y
# print("({} + {}) ^ 2 = {}".format(x, y, result))

# 39 compute the future value of a specified principal amount, rate of interest and number of years.
# amount, rate, years = 10000, 3.5, 7
# future_value = amount*((1 + (rate/100))**years)
# print(round(future_value, 2))

# 40 calculate the distance between the points(x1, y1) and (x2, y2)
# import math
# x1, y1 = 4, 0
# x2, y2 = 6, 6
# distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print(distance)

# 41 check whether a file exists
# import os
# print(os.path.isfile("practice.py"))
# print(os.path.isfile("app.py"))
# print(os.path.isfile("main.py"))
# print(os.path.exists("index.html"))
# # solution-3
# my_file = open("practice1.py")
# try:
#     my_file.close()
#     print("file found")
# except FileNotFoundError:
#     print("file not found")

# 42 determine if a python shell is executing in 32bit or 64bit mode on OS
# import platform, struct
# print(platform.architecture())
# print(struct.calcsize("P")*8)

# 43 get OS name, platform and release information
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

# 44 locate python site packages
# import site
# print(site.getusersitepackages())s

# 45 calls the external command
# import psutil
# print(psutil.cpu_count())

# 46 retrieve the path and name of the file currently being executed
# import os
# print(os.path.realpath())

# 48 parse a string to float or integer
# n = "268.133"
# print(int(float(n)))

# 49 list all files in a directory
# from os import listdir
# from os.path import isfile, join
# file_lists = [f for f in listdir("./") if isfile(join("./", f))]
# print(file_lists)

# 50 print without a new line or space
# for item in range(0, 10):
#     print("*", end="")

# 51 detemine the profiling of python programs.
# import cProfile
# def sum():
#     print(3 + 2)
# cProfile.run("sum()")

# 52 print to STDERR
# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)

# eprint("abc", "def", "xyz",123, sep="-", end="")

# 53 access environment variables.
# import os
# print(os.environ['path'])

# 54 get the current username
# import getpass
# print(getpass.getuser())

# 55 find local IP addresses using python's stdlib
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# 57 get the execution time of a Python method.
# import time

# def sumOfNumbers(n):
#     startTime = time.time()
#     s = 0
#     for i in range(0, n):
#         s += i
#     endTime = time.time()
#     return s, endTime-startTime

# print(sumOfNumbers(100000))

# 58 sum the first n positive integers.
# def sum(n):
#     s = 0
#     for i in range(0, n + 1):
#         s += i
#     return s
#     # return n*(n+1) / 2

# print(sum(8))

# 59 convert height (in feet and inches) to centimeters.
# def centimeters(foot, inch):
#     return foot*12*2.54*10 + inch*2.54*10

# print(centimeters(6, 0))

# 60 calculate the hypotenuse of a right angled triangle.
# import math
# def hypotenuse(ab, bc):
#     return round(math.sqrt(ab**2 + bc**2), 2)

# print(hypotenuse(3, 4))

# 61 convert the distance (in feet) to inches, yards, and miles.
# feet = int(input('input feet: '))
# inches = feet * 12
# yards = feet / 3
# miles = feet / 5280
# print(inches, yards, miles)

# 62 convert all units of time into seconds.

# def toSeconds(h, m, s):
#     m = m * 60
#     h = h * 60 * 60
#     s = m + h + s
#     return s

# print(toSeconds(0, 20, 0))

# 63 get an absloute file path
# import os
# print(os.path.abspath("google.py"))

# 64 retrieves the date and time of file creation and modification
# import os.path, time
# print(time.ctime(os.path.getmtime("practice.py")))
# print(time.ctime(os.path.getctime("practice.py")))

# 65 converts seconds into days, hours, minutes, and seconds
# time = 88888
# day = time / 24 / 60 /60
# time = time % (24*60*60)
# hour = time / 60 / 60
# time = time %(60*60)
# minute = time / 60
# time = time % 60
# second = time

# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minute, second))

# 66 calculate the Body Mass Index
# def BMI(height, weight):
#     return round(weight / (height/100)**2,2)

# print(BMI(174, 64))

# 67 convert pressure in kilopascals to pounds per square inch, a millmeter of mercury (mmHg) and atmosphere presure
# kpa = float(input("Input pressure in in kilopascals> "))
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
# print("Atmosphere pressure: %.2f atm." % (atm))

# 68 calculate sum of digits of a number
# def sum(num):
#     sum = 0
#     for i in str(num):
#        sum += int(i)
#     return sum

# print(sum(5245))

# 69 sort three integers without using conditional statements and loops
# x, y, z = 8, 3, 7
# a3 = max(x, y, z)
# a1 = min(x, y, z)
# a2 = x + y + z - a3 - a1
# print(a1, a2, a3)

# 70 sort files by date
# import glob
# import os

# files = glob.glob("*.py")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

# 71 jump over

# 72 get details of the math module
# import math
# print(dir(math))

# 73 caculate the midpoints of a line
# a = (3, 4)
# b = (5, 7)
# def mid(a, b):
#     return ((a[0] + b[0])/2, (a[1] + b[1])/2)
# print(mid(a, b))

# 74 hash a word
# soundex = [1, 3, 0, 7, 5, 9, 5, 0, 2, 5, 1]
# word = input("input the word be hashed: ")
# word = word.upper()
# coded = word[0]
# for a in word[1:len(word)]:
#     i = 65 - ord(a)
#     coded = coded + str(soundex[i])
# print(coded)

# 75 get the copyright information and write copyright information in python code
# import sys
# print(sys.copyright)

# 76 command-line arguments(name of the script, the number of arguments, arguments) passed to a script
# import sys
# print(sys.argv[0], len(sys.argv), str(sys.argv))

# 77 test whether the system is a big-endian platform or a little-endlian platform
# import sys
# if sys.byteorder == "little":
#     print("little-endian platform.")
# else:
#     print("big-endian platform")

# 78 find the available built-in modules
# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(textwrap.fill(module_name, width=100))

# 79 get the size of an object in bytes
# import sys
# print(sys.getsizeof("abcdefghijklmnopqrstuvwxyz"))
# print(sys.getsizeof("測試輸入中文的話，這個的容量大小會是多少個bytes"))

# 80 get the current value of the recursion limit
# import sys
# print(sys.getrecursionlimit())

# 81 concatnate N strings
# list_of_colors = ["red", "blue", "yellow"]
# colors = "-".join(list_of_colors)
# print(colors)

# print("Concatenating With the + Operator:")
# list_of_colors = ['Red', 'White', 'Black']
# colors = list_of_colors[0]+'-'+list_of_colors[1]+'-'+list_of_colors[2]
# print("All Colors: "+colors)

# 82 calculate the sum of all items of container(tuple, list, set, dictionary)
# def mySum(item):
#     sum = 0
#     for i in item:
#         sum += i
#     return sum


# list1 = [10, 20, 30]
# list1 = (10, 20, 30)
# print(mySum(list1))

# dict1 = {"a": 11, "b": 22, "c": 33}
# print(dict1["a"])


# def dict_sum(nums):
#     num_sum = 0
#     for i in nums:
#         print(i)
#         num_sum += nums[i]
#     return num_sum


# print(dict_sum(dict1))

# tuple1 = (10, 20, 30)
# print(sum(tuple1))
# set1 = {12, 13, 14}
# print(sum(set1))

# 83 test whether all numbers in a list are greater than a certain number
# def greater(nums, c):
#     for num in nums:
#         if num <= c:
#             return False
#     return True


# print(greater([10, 20, 30], 10))
# num = [2, 3, 4, 5]
# print(all(x > 3 for x in num))

# 84 count the number of occurrences of a specific character in a string
# def count(string, c):
#     count = 0
#     for s in string:
#         if s == c:
#             count += 1
#     return count

# print(count("this is a string", "h"))
# print("this is a text".count("t"))

# 85 check whether a file path is a file or diectory
# import os
# path = "google.py"
# if os.path.isdir(path):
#     print(path + " is a directory")
# elif os.path.isfile(path):
#     print(path + " is a file")

# def test(x, y, z):
#     return x if x <= y and x <= z else y if y <= x and y <= z else z
# print(test(1123, 254668, 3454))

# 86 get the ASCII value of a character
# print(ord("A"))

# 87 get the size of a file
# import os
# print(os.path.getsize("google.py"), "Bytes")

# file_size = os.stat("google.py")
# print(file_size.st_size)

# 88 given variables x = 30 and y = 20, to print "30 + 20 = 50"
# x, y = 30, 20
# print("%d + %d = %d" % (x, y, x + y))
# print(f"{x} + {y} = {x+y}")
# print("{0} + {1} = {2}".format(x, y, x + y))

# 89 given a varialbe name, if the values is 1 , display the string and do nothing if the value is not equal
# n = 1
# if n == 1:
#     print("first day of a month")

# 90 create of a copy of its own source code
# def file_copy(src, dest):
#     with open(src) as f, open(dest, "w") as d:
#         d.write(f.read())


# file_copy("y.py", "z.py")

# 91 swap two variables
# def swap(a, b):
#     temp = a
#     a = b
#     b = temp
#     print(a, b)


# a, b = 10, 20
# swap(10, 20)

# 92 define a string containing special character in various form
# print("\#{'}${\"}@/")

# 93 get the identity, type, and value of an object
# x = 35
# print("identity: ", x, "type: ", type(x), "id: ", id(x))

# 94 convert the bytes in a given string to a list of integers
# x = b"abcdefghijklmnopqrstuvwxyz"
# y = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(list(x))
# print(list(y))

# print(list(b"0123456789"))

# 95 check whether a string is numeric
# str = "123ddd3"
# try:
#     i = float(str)
#     print("numeric")
# except(ValueError, TypeError):
#     print("not numeric")

# 96 print the current call stack
# import traceback
# def f1(): return abc()
# def abc(): traceback.print_stack()
# f1()

# 97 list the special variables used in the language
# s_var_names = sorted((set(globals().keys()) | set(
#     __builtins__.__dict__.keys())) - set('_ names i'.split()))
# print()
# print('\n'.join(' '.join(s_var_names[i:i+8])
#       for i in range(0, len(s_var_names), 8)))
# print()

# 98 get the system time
# import datetime
# import time
# print(time.ctime())
# print(datetime.datetime.now())

# 99 clear the screen or terminal
# import os
# import time
# os.system("cls")
# time.sleep(1)

# 100 get the name of the host on which the routine is running
# import os
# import platform
# import socket
# print(socket.gethostname())

# print(platform.uname()[1])

# print(34//6 % 3)
# print(34//4/2)
# print(9*((5*12)-8))

# 101 access and print a url's content to the console
# from http.client import HTTPConnection
# import requests
# data = requests.get("https://www.example.com/")
# print(data.text)

# conn = HTTPConnection("example.com/")
# conn.request("GET", "/")
# result = conn.getresponse()
# content = result.read()
# print(content)

# 102 get system command output
# import subprocess
# return_text = subprocess.check_output(
#     "dir", shell=True, universal_newlines=True)
# print(return_text)

# 103 extract the filename from a given path
# import os
# path = os.path.abspath("./google.py")
# print(os.path.basename(path))

# 104 get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current porcess
# import os
# print("\nEffective group id: ", os.getegid())
# print("Effective user id: ", os.geteuid())
# print("Real group id: ", os.getgid())
# print("List of supplemental group ids: ", os.getgroups())

# 105 get the users environment
# import os
# import pprint
# u_env_var = os.environ
# print(u_env_var)
# pprint.pprint(dict(u_env_var), width=1)

# 106 divide a path by the extension separator
# import os.path
# print(os.path.splitext("abc.txt"))
# for path in ['test.txt', 'filename', '/user/system/test.txt']:
#     print('"%s" :' % path, os.path.splitext(path))

# 107 retrieve file properties
# import os.path
# import time
# print(__file__)
# print(time.ctime(os.path.getatime(__file__)))
# print(time.ctime(os.path.getmtime(__file__)))
# print(time.ctime(os.path.getctime(__file__)))
# print(os.path.getsize(__file__))

# 108 find the path to a file or directory when you encounter a path name
# import os.path
# for file in [__file__, os.path.dirname(__file__), '/', "./broken_link"]:
#     print(file)
#     print(os.path.isabs(file))
#     print(os.path.isdir(file))
#     print(os.path.islink(file))
#     print(os.path.exists(file))
#     print(os.path.lexists(file))

# 109 check if a number is positive, negative or zero
# num = 5
# print("num is positive" if num >
#       0 else "num is negative" if num < 0 else "num is zero")

# 110 get numbers divisible by fitteen from a list using an anonymous funtion
# num_list = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda x : (x%15 == 0), num_list)))

# 111 make file lists from the current directory using a wildcard
# import glob
# file_list = glob.glob("*[a-z]*.py")
# print(file_list)

# from pathlib import Path
# for path in Path("./").glob("[a-z].*"):
#     print(path)

# 112 remove the first item from a specified list
# item_list = ['x', 'y', 'z', 'j', 'k', 'l']
# del item_list[0]
# print(item_list)

# new_item_list = item_list[1:]
# print(new_item_list)
# new_item_list.remove("z")
# print(new_item_list)

# def tail(lst):
#     return lst[1:]

# print(tail(new_item_list))

# 113 inputs a number and generates an error is it is not a number
# solution1
# while True:
#     try:
#         a = int(input("input a number: "))
#         break
#     except ValueError:
#         print("not a number")

# solution2
# x = 1
# x_int = x.is_integer()
# print(x_int)

# solution3
# x = 1.0
# x_int = isinstance(x, int)
# print(x_int)

# 114 filter positive numbers from a list
# solution1
# num_list = [6, -3, 9, 4, -7, 5, -3]
# new_nums = list(filter(lambda x: x > 0, num_list))
# print(new_nums)

# new_list = []
# for num in num_list:
#     if num > 0:
#         print(num, end=" ")

# print([n for n in num_list if n > 0])

# 115 compute the product of a list of integers(without using a for loop)
# from functools import reduce
# nums = [10, 20, 30, 40, 50, 60, 70]
# nums_add = reduce(lambda x,y: x + y, nums)
# print(nums_add)

# 116 print unicode characters
# str = '\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
# print(str)
# print('\u0050\u0060')
# x = ['ab', 'cd']
# new_x = []
# for i in x:
#     new_x.append(i.upper())
#     print(new_x, end='')

# 117 prove that two string variables of the same value point to the same memory location
# a = 10
# b = 10
# print(hex(id(a)))
# print(hex(id(b)))

# 118 create a bytearray from a list
# nums = [10, 20, 30, 40, 50]
# values = bytearray(nums)
# for x in values:print(x)

# 119 round a floating-point number to a specified number of decimal places
# num = 14.365
# print('the origin num is %f'% num)
# print('the new num is %.2f' % num)
# print("{:0.3f}".format(num))

# 120 format a specified string and limit the length of a string
# str_num = "1234567890"
# print('%.6s'% str_num)
# print('%.3s' % str_num)

# 121 determine if a variable is defined or not
# try:
#     x = 1
#     print("x = 1")
# except NameError:
#     print("not defined")
# else:
#     print("is defined")

# 122 empty a variable without destorying it
# n = 20
# d = {"x":20}
# l = [1, 3, 5]
# t = (3, 5, 7)
# print(type(n)())
# print(type(d)())
# print(type(l)())
# print(type(t)())

# def empty_var(lst):
#     return [type(i)() for i in lst]

# lst = ["apple", {"x":20}, [1, 3, 5], (3, 5, 7), 100]
# print(empty_var(lst))

# 123 detemine the largest and smallest integers, lones, and floats
# import sys
# print(sys.int_info)
# print(sys.maxsize)

# 124 check whether multiple variables have the same value
# x, y, z = 10, 20, 30
# if x == y and y == z:
#     print("all variables have the same value")
# else:
#     print("they are not the same")

# 125 sum the counts in a collection
# import collections

# nums = [10, 20, 30]
# print(sum(collections.Counter(nums).values()))
# print(len(nums))

# 126 get the actual module object for a given object

# from inspect import getmodule
# print(getmodule(getmodule))
# def add(x, y):
#     return x + y
# print(getmodule(add))

# 127 check whether an integer fits in 64 bits
# int_val = 30
# if int_val.bit_length() <= 63:
#     print((-2**63).bit_length())
#     print((2**63).bit_length())

# 128 check whether lowercase letters exist in a string
# text = "ABCDEFiGHIJKL"
# print(any(c.islower() for c in text))
# def check(text):
#     flag = 0
#     for i in text:
#         if (ord(i) >= 97 and ord(i) <= 122):
#             flag += 1
#     if (flag > 0):
#         return True
#     else:
#         return False
# print(check(text))

# 129 add leading zeros to a string
# str1 = "abc"
# print(str1.ljust(10, "x"))
# print(str1.rjust(10, "x"))
# print('{:>8}'.format(str1))

# 130 uses double quotes to display strings
# import json
# print(json.dumps({'alex':1, 'suresh':2, 'agnessa':3}))

# 131 split a varialbe length string into varialbes
# var_list = ['a', 'b', 'c']
# x, y, z = (var_list + [None]*3)[0:3]
# print(x, y, z)

# 132 list the home directory without an absolute path
# import os.path
# print(os.path.expanduser('~'))

# 133 calculate the time runs(difference between start and current time)of a program
# from timeit import default_timer
# def timer(n):
#     start = default_timer()
#     # some code here
#     for row in range(0, n):
#         print(row)
#     print(default_timer() - start)

# timer(5)

# 134 input two integers on a single line
# x, y = map(int, input().split())
# print(x, y)

# a, b = [int(a) for a in input("Input the value of a & b: ").split()]
# print("The value of a & b are:",a,b)

# 135 print a variable without spaces between values
# x = 30
# print('Value of x is "{}"'.format(x))
# print('value is "%i"' %x)
# print("value is " + '\"' + str(x) + '\"')

# 136 find files and skip directories in a given directory
# import os
# print([f for f in os.listdir('./') if os.path.isfile(os.path.join("./", f))])

# user_path = 'd:/'
# for fname in os.listdir(user_path):
#    path = os.path.join(user_path, fname)
#    if os.path.isdir(path):
#        # skip directories
#        continue
#    print(fname)

# 137 extract a single key-value pair from a directory into variables
# d = {'Red': 'Green'}
# (c1, c2), = d.items()
# print(c1)
# print(c2)

# 138 convert True to 1 and False to zero
# x = 'true'
# x = int(x == 'true')
# print(x)
# x = 'abcd'
# x = int(x == "true")
# print(x)

# 139 validate an IP address
# import socket
# addr = '127.0.0.999'
# try:
#     socket.inet_aton(addr)
#     print("valid IP")
# except socket.error:
#     print('invalid IP')

# 140 convert an integer to binary that keeps leading zeros
# x = 12
# print(format(x, '010b'))

# 141 convert decimal to hexdecimal
# x = 30
# print(format(x, '02x'))

# 142 check if every consecutive sequence of zeros is followed by a consecutive sequence of ones of same length in a given string.Return True/False
# def test(str1):
#     while '01' in str1:
#         str1 = str1.replace('01', '')
#     return len(str1) == 0


# str1 = "01010000"
# print(test(str1))

# 143 detemine if the python shell is executing in 32-bit or 64-bit mode on the operating system
# import struct
# print(struct.calcsize("p")*8)

# 144 check whether a variable is an integer or a string
# print(isinstance((1, 2, 3), tuple))
# print(isinstance([1, 2, 3], list))
# print(0 or 2 or 3)

# 145 test if a variable is a list, tuple, or set
# v = {"a": 1}
# if isinstance(v, list):
#     print("v is a list")
# elif isinstance(v, tuple):
#     print("v is a tuple")
# elif isinstance(v, set):
#     print("v is a set")

# 146 find the location of python module sources
# import sys
# import os
# import imp
# print(imp.find_module("os"))
# print(imp.find_module("sys"))
# print(os.path)
# print(sys.path)

# 147 check whether a number is divisible by another number
# def divisible(a, b):
#     if a % b == 0:
#         return True
#     elif b % a == 0:
#         return True


# print(divisible(5, 10))

# 148 find the maximum and minimum numbers from a sequence of numbers
# max = 0
# min = 9999
# list = [12, 23, 35, 44, 57]
# for i in list:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max)
# print(min)


# def max_min(data):
#     max = data[1]
#     min = data[1]
#     for num in data:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
#     return max, min


# print(max_min([3, 16, 0.6, 39, 55]))

# 149 takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number
# def sum_of_cubes(n):
#     n -= 1
#     total = 0
#     while n > 0:
#         total += n**3
#         n -= 1
#     return total


# print(sum_of_cubes(6))


# def sum_of_cubes1(n):
#     if n < 0:
#         raise ValueError("n must be positive number")
#     return n*n(n*n-2*n+1)/4


# print(sum_of_cubes1(6))


# 150
def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
    return False


dt1 = [2, 4, 6, 8]
dt2 = [1, 6, 4, 7, 8]
dt3 = [1, 3, 5, 7, 9]
print(dt1, odd_product(dt1))
print(dt2, odd_product(dt2))
print(dt3, odd_product(dt3))
