matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print(matrix[0])
print(matrix[0:2])

print('-------*access elements in a matrix*-------')
# access elements in a array
print(matrix[0][1])

print('-------*length*-------')
# length
print(len(matrix))
print(len(matrix[0]))

print('-------*append*-------')
# append
newlist = [10, 11, 12]
matrix.append(newlist)
print(matrix)

newlist = [10, 11, 12, 13]
matrix.append(newlist)
print(matrix)

print('-------*insert*-------')
matrix[0].insert(0, 100)
print(matrix)

print('-------*extend*-------')
newlist = [10, 11, 12, 13]
newlist.extend([100])
print(newlist)

print('-------*remove*-------')
# remove
newlist = [10, 11, 12]
newlist.remove(10)  # use value here
print(newlist)

print('-------*pop*-------')
# pop
newlist = [10, 11, 12]
newlist.pop(2)  # use index here default index for pop is -1 (last element)
print(newlist)

print('-------*clear*-------')
# clear
newlist = [10, 11, 12]
newlist.clear()
print(newlist)
