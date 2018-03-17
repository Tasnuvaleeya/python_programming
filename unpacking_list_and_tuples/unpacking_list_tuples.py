"""
first, second, third = ['December', "Tasnuva", 99]

print(first)
print(second)
print(third)
"""


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
drop_first_last([12, 33, 99, 37, 87, 56])
