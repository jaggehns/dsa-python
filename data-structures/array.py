array = [5, 6, 11, 0, 9, 8, 10, 15, 1, 2]

# access - O(1)
a = array[0]
print("accesed index postiton ", a)

# insert & delete
# end of array - O(1)
array.append(16)
print("inserted index postiton ", array[10])

# start/middle of array - O(n) - need to reassign indexes
array.insert(7, 0)
print(array)

# search (traverse) - O(n)
for idx, element in enumerate(array):
    if element == 10:
        print("index position: ", idx)