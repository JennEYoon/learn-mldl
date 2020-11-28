""" Practice Python enumerate function.
    enumerate(iter, start value)
    Jennifer Yoon 4/23/2018. """


print("Hello to me!")
print(3+5)
x= 10 + 2
print(x)
"""  testing doc string """
for i, item in enumerate(['a', 'b', 'c'], start=10):
    print(i, item)

seasons = ('spring', 'summer', 'autumn or fall', 'winter')
for i, item in enumerate(seasons, 1):
    print(i, item)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['me', 'you', 'us']]
print(matrix[:])

for i, item in enumerate(matrix, 0):
    print(i, item, item[0]+item[1]+item[2])

#   end of test.  #
