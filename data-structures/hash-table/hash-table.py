dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# accessing an entry - O(1)
name = dict['Name']
print(name)

# update existing entry - O(1)
dict['Age'] = 8

# Add new entry - O(1)
dict['School'] = "DPS School"

# remove entry - O(1)
del dict['Name']
print(dict)