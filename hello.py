
if __name__ == "__main__":
    print("hello")

"""
Just goofing around with the map function
"""

x = [1, 2, 3, 4, 5]  # iteratable
y = [2, 2, 2]  # another iterable of different length
print(type(x))


z = list(map(lambda x, y: (x % 2)*y, x, y))


print(z)


# lambda executes on minimum boundary list length. in this example, the output is [2, 0, 2], since the second parameter Y only has
# 3 iterable elements, while x has 5 iterable elements.
# the map function builds an interable with 3 elements.
