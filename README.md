# Data Structures & Algorithms
<a href="https://jaggehn-portfolio.netlify.app/"><img alt="Website" src="https://img.shields.io/badge/Website-www.jaggehns.com-blue?style=flat-square&logo=google-chrome"></a>
<a href="https://www.linkedin.com/in/jaggehn-sivabalan/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Jaggehn%20Sivabalan-blue?style=flat-square&logo=linkedin"></a>
<a href="mailto:jaggehns@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-jaggehns@gmail.com-blue?style=flat-square&logo=gmail"></a>
<a href="https://www.instagram.com/jaggehn_/"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-jaggehn__-blue?style=flat-square&logo=instagram"></a>

> In this repository, I document my learning journey of data structures and algorithms in Python. This material can be used as a reference manual for developers, or you can refresh specific topics before an interview. Also, you can find ideas to solve problems more efficiently.


## Table of Contents

- [Data Structures](#data-structures)
  - [Array](#array)
  - [Linked List](#linked-list)
      - [Singly Linked List](#singly-linked-list)
      - [Doubly Linked List](#doubly-linked-list)
      - [Circular Linked List](#circular-linked-list)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Hash Table](#hash-table)
---

## Data Structures

### Array

- Arrays are also referred to as lists in Python
- They can be static (no extra memory allocated) or dynamic (extra memory allocated)

```python
array = [5, 6, 11, 0, 9, 8, 10, 15, 1, 2]
```
- Common array operations and their time complexities:

```python
# accessing a value - O(1)
array[0]

# insert/delete at the end - O(1)
array.append(12)
array.pop()

# insert/delete at the start/middle - O(n)
array.insert(7,0) # need to reassign indexes

# search (traverse) an array - O(n)
for idx, element in enumerate(array):
    if element == 10:
        print("index position: ", idx)
```
---

### Linked List

    - A linked list is a linear data structure that stores a collection of data elements dynamically.
    
    - Nodes represent data elements, and links or pointers connect each node.
    
    - Each node consists of two fields, 
      - the information stored in a linked list
      - a pointer that stores the address of its next node.

    - The first node is the Head, and the last node is the Tail
  
<br />
<img width="624" alt="Screenshot 2023-11-20 at 12 27 24 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/fa4b913d-0516-4095-94e6-5d032bf2597b">
<br /><br />

#### Singly Linked List

    - A singly linked list is the most common type of linked list. 
    
    - Each node has data and an address field that contains a reference to the next node.

    - The Tail node points to None

<br />
<img width="624" alt="Screenshot 2023-11-20 at 12 45 03 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/30d1fb8a-923c-4e07-92f7-e0af0e4c36b4">
<br /><br />

#### Doubly Linked List

    - Each node stores the data and the reference to the previous & next value. 
    
    - Thus, you can traverse in both directions.

<br />
<img width="624" alt="Screenshot 2023-11-20 at 12 48 34 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/d08ced6d-aeab-4dc3-a629-40208bc84c12">
<br /><br />

#### Circular Linked List

    - In a circular linked list, the last node is connected with the first node. 
    
    - This forms a circular loop in the circular linked list.

    - Circular linked lists can either be singly or doubly-linked lists.

<br />
<img width="624" alt="Screenshot 2023-11-20 at 12 51 46 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/b52cee79-a4f3-4135-be2d-8d8c4e06f8c0">
<br /><br />

- Linked list time complexities are shown below:

```
Accessing i-th node - O(n) - we need to traverse the list to find the node

Traverse all nodes - O(n)

Insert/Delete at known element - O(1)

Insert/Delete at unknown element - O(n) - need to traverse the list

```

---

### Stack

    - A stack is a linear data structure that follows the principle of Last In First Out (LIFO). 
    
    - This means the last element inserted inside the stack is removed first.
  
<br />
<img width="624" alt="Screenshot 2023-11-21 at 7 01 58 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/e1b5ebdb-204a-454f-82f5-0e9fc93d5423">
<br /><br />

- Stack time complexities are shown below

```
Push - O(1) - insert element into the stack

Pop - O(1) - Remove the last element in the stack

Peek (Top) - O(1) - View the last element in the stack

```

- A stack can be implemented using an array or a linked list

---

### Queue

    - Queue follows the First In First Out (FIFO) rule
    
    - The item that goes in first is the item that comes out first.
  
<br />
<img width="624" alt="Screenshot 2023-11-21 at 7 07 45 AM" src="https://github.com/jaggehns/dsa-python/assets/72048640/e8bec3c8-f24a-4000-abdc-83e693356813">
<br /><br />

- Queue time complexities are shown below

```
Dequeue - O(1) - Remove the first (front) element in the queue

Enqueue - O(1) - Add an element to the end of the queue

Peek (Top) - O(1) - View the first (front) element in the queue

```

- Queues are implemented using a linked list, as inserting an element at the start is O(1)

---

### Hash Table

    - The hash table data structure stores elements in key-value pairs
    
    - Key: unique integer that is used for indexing the values

    - Value: data that are associated with keys.
  
<br />
<img width="624" alt="Screenshot 2023-11-22 at 11 46 46 PM" src="https://github.com/jaggehns/dsa-python/assets/72048640/8273767e-6411-4aa9-b563-613f8b2e9814">
<br /><br />

```

- In a hash table, a new index is processed using the keys

- The element corresponding to that key is stored in the index

- This process is called hashing. Hashing collisions will not be covered here

```

- Hash table time complexities are shown below

```python
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# accessing an entry - O(1)
dict['Name']

# update existing entry - O(1)
dict['Age'] = 8

# Add new entry - O(1)
dict['School'] = "DPS School"

# remove entry - O(1)
del dict['Name']

```
