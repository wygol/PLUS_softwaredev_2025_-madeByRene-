import urllib3
import fancyModule

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


response = urllib3.request("GET", "https://www.vum.co.at/")
print(response.status)


fib = fancyModule.generate_fibonacci(20)
print("fib: {0}".format(fib))

squared = fancyModule.square_iterable(fib)
print("squared: {0}".format(squared))

moduloList = fancyModule.modulo_iterable(fib, 7)
print("moduloList: {0}".format(moduloList))
