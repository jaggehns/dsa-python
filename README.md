# Data Structures & Algorithms
<a href="https://jaggehn-portfolio.netlify.app/"><img alt="Website" src="https://img.shields.io/badge/Website-www.jaggehns.com-blue?style=flat-square&logo=google-chrome"></a>
<a href="https://www.linkedin.com/in/jaggehn-sivabalan/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Jaggehn%20Sivabalan-blue?style=flat-square&logo=linkedin"></a>
<a href="mailto:jaggehns@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-jaggehns@gmail.com-blue?style=flat-square&logo=gmail"></a>
<a href="https://www.instagram.com/jaggehn_/"><img alt="Instagram" src="https://img.shields.io/badge/Instagram-jaggehn__-blue?style=flat-square&logo=instagram"></a>

> In this repository, I document my learning journey of data structures and algorithms in Python. This material can be used as a reference manual for developers, or you can refresh specific topics before an interview. Also, you can find ideas to solve problems more efficiently.


## Table of Contents

- [Data Structures](#data-structures)
  - [Array](#array)
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
