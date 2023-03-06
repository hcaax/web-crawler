# 1 takes a sequence of numbers and detemines whether all the numbers are different from each other
def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False


print(test_distinct([1, 3, 5, 7, 9, 31]))
