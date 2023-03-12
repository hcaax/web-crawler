# 1 find a list of integers with exactly two occurrences of nineteen and at least three occurences of five.Return True otherwise False
# def test(lst):
#     return lst.count(19) >= 2 and lst.count(5) >= 3


# print(test([18, 19, 17, 19, 5, 3, 7, 5, 2]))

# print('%s' % (4.65,))

# print('%.2f%s' % (4.2345, '98'))

# print('{0:f}, {1:2f}, {2:05.2f}'.format(1.2345, 1.2345, 1.2345))

# 2 accepts a list of integers and calculates the length and the fifth element.Return True if the length of the list is 8 and the fifth element occurs thrice in the said list
# lst = [19, 19, 15, 5, 5, 4, 1, 2]


# def test(lst):
#     return len(lst) == 8 and lst.count(lst[4]) == 3


# print(test(lst))

# 3 accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34
# num1 = 922
# def test(n):
#     return n > 4**4 and n % 34 == 4
# print(test(num1))

# 4 We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones in each pile.
# def test(n):
#     return [n + 2 * i for i in range(n)]
# print(test(10))

# 5 check the n th-1 string is a proper substring of the n th string in a given list of strings
# def check(strs):
#     return strs[len(strs) - 2] != strs[len(strs) - 1] and strs[len(strs)-2] in strs[len(strs)-1]


# print(check(['a', 'abb', 'sad', 'ooaaesdfe',
#       'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']))

# 6 test a list of one hundred integers

# 7 check a given list of integers where the sum of the first i integers is i
# print(sum([1, 2, 3, 4, 5][:1]) == 1)

# I = list("java")
# p = I[0], I[-1], I[1:3]
# print(type(p))

# print('{0:.2f}'.format(1/3.0))

# print('%x %d' %(255, 255))
# import re
# str1 = "yes i am the hero"
# str2 = str1.split(' ', 1)
# print(str2)
# print([1, 2, 3, 4, 5, 6][0::2])
# import re
# string= "臺中市南屯區埔興段35-12地號"
# regex = re.compile(r'段(\d+-*\d)')
# match = regex.search(string)
# print(match.group(1))

def test(string):
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]
s = "W3resource Python, Exercises."
print("Original string:",s)
print("Split the said string into 2 lists: words and separators:")
print(test(s))
# s = "The dance, held in the school gym, ended at midnight."
# print("\nOriginal string:",s)
# print("Split the said string into 2 lists: words and separators:")
# print(test(s))
# s = "The colors in my studyroom are blue, green, and yellow."
# print("\nOriginal string:",s)
# print("Split the said string into 2 lists: words and separators:")
# print(test(s))

# regex101.com regexone.com