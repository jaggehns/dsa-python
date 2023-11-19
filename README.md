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

- Linked list complexities are shown below:

```
Accessing i-th node - O(n) - we need to traverse the list to find the node

Traverse all nodes - O(n)

Insert/Delete at known element - O(1)

Insert/Delete at unknown element - O(n) - need to traverse the list

```
