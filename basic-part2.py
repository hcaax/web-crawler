# 1 takes a sequence of numbers and detemines whether all the numbers are different from each other
# def test_distinct(data):
#     if len(data) == len(set(data)):
#         return True
#     else:
#         return False


# print(test_distinct([1, 3, 5, 7, 9, 31]))

# 2 creates all possible strings using the letters 'a, 'e', 'i, 'o, and 'u'.Ensure that each character is used only once
# import random
# char_list = ['a', 'e', 'i', 'o', 'u']
# random.shuffle(char_list)
# print(''.join(char_list))

# 3 removes and prints every third number from a list of numbers unitil the list is empty
# lst = [1, 2, 3, 4, 5, 6, 7]
# position = 3 - 1
# idx = 0
# len_list = len(lst)
# while len(lst) > 0:
#     idx = (position+idx) % len_list
#     print(lst.pop(idx))
#     len_list -= 1

# 5 make combinations of 3 digits
# numbers = []
# for num in range(1000):
#     num = str(num).zfill(3)

# numbers.append(num)
# print(numbers)

# 6 prints long text, converts it to a list, and prints all the words and the frequency of each word
# string_words = """United States Declaration of Independence
# From Wikipedia, the free encyclopedia
# The United States Declaration of Independence is the statement
# adopted by the Second Continental Congress meeting at the Pennsylvania State
# House (Independence Hall) in Philadelphia on July 4, 1776, which announced
# that the thirteen American colonies, then at war with the Kingdom of Great
# Britain, regarded themselves as thirteen independent sovereign states, no longer
# under British rule. These states would found a new nation – the United States of
# America. John Adams was a leader in pushing for independence, which was passed
# on July 2 with no opposing vote cast. A committee of five had already drafted the
# formal declaration, to be ready when Congress voted on independence."""

# word_list = string_words.split()
# # print(word_list)
# word_freq = [word_list.count(n) for n in word_list]
# print(list(zip(word_list, word_freq)))


# a = ['a', 'b', 'c', 'd']
# b = [1, 2, 3, 4]
# zipped = zip(a, b)
# print(list(zipped))

# 7 count the number of each character in a text file
# import collections
# import pprint
# text_file = "These states would found a new nation – the United States of America. John Adams was a leader in pushing for independence"
# count = collections.Counter(text_file)
# value = pprint.pformat(count)
# print(value)

# 8 retrieves the top stories from google news
# import bs4
# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen

# new_url = "https://news.google.com/home?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
# Client = urlopen(new_url)
# xml_page = Client.read()
# Client.close()

# soup_page = soup(xml_page, "xml")
# news_list = soup_page.findAll("item")

# for news in news_list:
#     print(news.title.text)
#     print(news.link.text)
#     print(news.pubDate.text)
#     print("-"*60)

# 9 get a list of locally installed python modules
# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(
#     ["%s=%s" % (i.key, i.version) for i in installed_packages])
# for m in installed_packages_list:
#     print(m)

# 10 display some information about the OS where the script is running
# import platform as pf
# os_profile = ['architecture',
#               'linux_distribution',
#               'mac_ver',
#               'machine',
#               'node',
#               'platform',
#               'processor',
#               'python_build',
#               'python_compiler',
#               'python_version',
#               'release',
#               'system',
#               'uname',
#               'version', ]

# for key in os_profile:
#     if hasattr(pf, key):
#         print(key + ":" + str(getattr(pf, key)()))

# 11 check the sum of three elements (each from an array) from three arrays is equal to a target value.
# print all those three-element combinations
# import itertools
# from functools import partial
# x = [10, 20, 20, 20]
# y = [10, 20, 30, 40]
# z = [10, 30, 40, 20]
# t = 70


# def check_sum_array(N, *nums):
#     if sum(x for x in nums) == N:
#         return(True, nums)
#     else:
#         return(False, nums)


# pro = itertools.product(x, y, z)
# func = partial(check_sum_array, t)
# sums = list(itertools.starmap(func, pro))

# result = set()
# for s in sums:
#     if s[0] == True and s[1] not in result:
#         result.add(s[1])
#         print(result)

# 12

# result_perms = [[]]
# for n in [1, 2, 3]:
#     new_perms = []
#     for perm in result_perms:
#         for i in range(len(perm)+1):
#             new_perms.append(perm[:i] + [n] + perm[i:])
#             result_perms = new_perms

# 13 get all possible two-digit letter combinations from a 1-9 digit string
# def letter_combinations(digits):
#     if digits == "":
#         return []
#     string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#     result = [""]
#     for num in digits:
#         temp = []
#         for an in result:
#             for char in string_maps[num]:
#                 temp.append(an + char)
#         result = temp
#     return result


# digit_string = "47"
# print(letter_combinations(digit_string))
# digit_string = "29"
# print(letter_combinations(digit_string))

# 14 add two positive integers without using the '+' operator
# def add_without_plus_operator(a, b):
#     while b != 0:
#         data = a & b
#         a = a ^ b
#         b = data << 1
#     return a


# print(add_without_plus_operator(2, 10))

# 15 check the priority of the four operator(+, -, *, /)

# 16 get the third side of a right-angled trangle from two given side
