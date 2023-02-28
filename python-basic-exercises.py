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

