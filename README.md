# Piscine Python for Data-science
## _------------Starting------------_
### EX00
* by Default `Python` has different data types built-in.
* first what mean `built-in` ?
* `built-in` is anything that come pre-installed with a progrmming language, ready for use without the for additional coding.
all those next types are used to store collections of data :
- ### `list`
- List items are ordered, changeable, and allow duplicate values.
- Can contain different data types in same time.
- Since list items are indexed, we can access and change them by refferring to the index number.
- to create `List`:
```python
lst = ["one", "two", "tree"]
```
- ### `tuple` :
- Tuple (like `List`)items are ordered but unchangeable. Allows duplicate members.
- Tuple items also are indexed, we can access them by refferring to the index number. but we cannot change, add, or remove them once the tuple is created.
- But there are some workaounds, like (You can convert the tuple into a list, change the list, and convert the list back into a tuple).
- to create `Tuple`:
```python
tup = ("one", "two", "tree")
```
- ### `set` :
- Set items are unordered ,unchangeable, and unindexed. No duplicate members.
* `Note`: Set items are unchangeable, but you can remove items and add new items.
To add or remove item use the `add()` or `romove()` method.
- ### `dict` :
- Dictionary are used to store data values in `Key`:`Value` pairs.
- Dictionary items are ordered and changeable. No duplicate members.
- You can access or update or append by referring to its `key` name inside squre brackets '[]'.

---
### EX01
- 

---
### EX02
- `function` is a block of code which only runs when it is called.
you can create function by 'def':
```python
def my_function():
  print("Hello from a function")
```
- to make function return a value :
```python
  return value
```
---
### EX03
- `None` represents the absence of a value and is the only instance of the NoneType.
It's often used as a placeholder for variables that don't hold meaningful data yet.
Unlike 0, "", or [], which are actual values, `None` specifically means "`no value`" or "`nothing`."
---
### EX04
- `sys.argv` function lets you take argments from command line.
- `int()` for casting to intger.
- `try` : block lets you test a block of code for errors.
- `except` : block lets you handling error if occured.
- Since the try block raises an error, the except block will be executed.
Without the try block, the program will crash and raise an error
---
