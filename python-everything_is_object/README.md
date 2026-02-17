# Python: Everything is Object

## Description

This project explores Python's object model, focusing on the fundamental concept that **everything in Python is an object**. Through a series of quizzes and coding exercises, you'll gain a deep understanding of how Python handles objects, mutability, and references.

## Learning Objectives

By completing this project, you will be able to explain:

- What is an object in Python
- The difference between `type()` and `id()` built-in functions
- The distinction between mutable and immutable objects
- How Python handles variable assignment and references
- What aliases are and how they work
- How to determine if two variables are identical or equal
- How function arguments are passed in Python (pass by object reference)

## Project Structure

### Answer Files (Quiz Questions)

These files contain answers to questions about Python object behavior:

| File | Topic |
|------|-------|
| `0-answer.txt` | Function to get object type |
| `1-answer.txt` | Function to get variable's unique identifier |
| `2-answer.txt` - `9-answer.txt` | Questions about object identity and equality |
| `10-answer.txt` - `13-answer.txt` | List and string reference questions |
| `14-answer.txt` - `18-answer.txt` | List modification and reference behavior |
| `19-copy_list.py` | Function implementation: copy a list |
| `20-answer.txt` - `28-answer.txt` | Advanced reference and mutation questions |

### Python Scripts

| File | Description |
|------|-------------|
| `19-copy_list.py` | Returns a copy of a list |
| `100-magic_string.py` | Returns string "BestSchool" repeated n times using function attributes |
| `101-locked_class.py` | Class with `__slots__` to restrict attribute creation |

### Quiz Answer Files (Code Analysis)

| File Series | Description |
|-------------|-------------|
| `103-line1.txt` - `103-line2.txt` | Memory reference count analysis |
| `104-line1.txt` - `104-line5.txt` | Object identity and reference counting |
| `105-line1.txt` | Memory address calculation |
| `106-line1.txt` - `106-line5.txt` | Object lifecycle and reference analysis |

## Key Concepts

### Mutable vs Immutable Objects

**Immutable Types:**
- `int`, `float`, `complex`
- `str`
- `tuple`
- `frozenset`
- `bool`
- `bytes`

**Mutable Types:**
- `list`
- `dict`
- `set`
- `bytearray`
- User-defined classes (by default)

### `is` vs `==`

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True - same values (equality)
a is b  # False - different objects (identity)
```

### Aliasing

```python
# Aliasing - both variables point to the same object
list1 = [1, 2, 3]
list2 = list1  # list2 is an alias of list1

# Modifying list1 affects list2
list1.append(4)
print(list2)  # [1, 2, 3, 4]
```

## Requirements

- Python 3.8+
- All scripts are executable (`#!/usr/bin/python3`)
- Code follows PEP 8 style guidelines

## Resources

- [Blog Post: Mutable, Immutable... Everything is an Object!](./blog_post.md)
- [Python Documentation: Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python Documentation: Built-in Functions](https://docs.python.org/3/library/functions.html)

## Author

**Holberton School Student**

## License

This project is part of the Holberton School curriculum.