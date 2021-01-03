# PythonNotes

When a program is run, data objects in the program are stored in the computer’s memory for processing. While some of these objects can be modified at that memory location, other data objects can’t be modified once they are stored in the memory. The property of whether or not data objects can be modified in the same memory location where they are stored is called **mutability**.

We can check the mutability of an object by checking its memory location before and after it is modified. If the memory location remains the same when the data object is modified, it means it is mutable.

To check the memory location of where a data object is stored, we use the function, id(). Consider the following example (you can try this yourself in IDLE):

Assigning values to the list a.
```
>>> a=[5, 10, 15]
```
Using the function id() to get the memory location of a.
```
>>> id(a)
```
**Output**
The ID of the memory location where a is stored.
```
1906292064
```
Replacing the second item in the list,10 with a new item, 20.
```
>>> a[1]=20
```
Using the print() function to verify the new value of a.
```
>>> print(a)
```
**Output**
Verified that the value of a has changed.
```
[5, 20, 15]
```
Using the function id() to get the memory location of a.
```
>>> id(a)
```
**Output**
The ID of the memory location where a is stored.
```
1906292064
 ```

Notice that the memory location has not changed as the ID remains (1906292064) remains the same before and after the variable is modified. This indicates that the list is **mutable**, i.e., it can be modified at the same memory location where it is stored. Now, let us check if a tuple is mutable in Python:

Assigning values to the tuple b.
```
>>> b=(5, 10, 15)
```
Replacing the second item in the list, 10 with a new item, 20.
```
>>> b[1]=20
```
**Output**
Error explaining that a tuple does not support modification in the items – i.e, it is immutable.
```
Traceback (most recent call last):

  File "<pyshell#1>", line 1, in <module>

    b[1]=20

TypeError: 'tuple' object does not support item assignment
 ```

You can verify the mutability of each of the data types in IDLE.

Immutable: numeric, string, and tuple
Mutable: list, dictionary

### Escape Sequence

You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An **escape sequence** in Python starts with a backslash (\). For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning - a new line.

Displayed here are a few common escape sequences available in Python. You can try these out in IDLE or the Python prompt from the windows command prompt.

![](https://github.com/Psingh12354/PythonNotes/blob/main/img1.PNG)

### Formated String

With Python 3.0, the format() method has been introduced for handling complex string formatting more efficiently. This method of the built-in string class provides functionality for complex variable substitutions and value formatting. This new formatting technique is regarded as more elegant.

The general syntax of the format() method is: **string.format(var1, var2,...)**

The string itself contains placeholders {} in which values of variables are successively inserted.
```
>>> name="Malhar"
>>> age=23
>>> percentage=55.5
>>> "my name is {} and my age is {} years".format(name, age)
'my name is Malhar and my age is 23 years'
>>>
```
You can also specify formatting symbols. Only change is using colon (:) instead of %. For example, instead of %s use {:s} and instead of %d use (:d}
```
>>> "my name is {:s} and my age is {:d} years".format(name, age)
'my name is Malhar and my age is 23 years'
>>>
```
Precision formatting of numbers can be accordingly done.
```
>>> "my name is {:s}, age {:d} and I have scored {:6.3f} percent
 marks".format(name, age, percentage)
'my name is Malhar, age 23 and I have scored 55.500 percent marks'
>>> 
```

### Set Data type

Set is also a collection data type in Python. However, it is **not an ordered collection of objects**, like a list or tuple. Hence, indexing and slicing operations cannot be done on a set object. A set also doesn’t allow duplicate objects to be stored, whereas, in list and tuple, the same object can appear more than once. Even if an object is put more than once in a set, only one copy is held. Set is a Python implementation of a set as defined in Mathematics. The set object has suitable methods to perform mathematical set operations like union, intersection, difference, etc. A set object contains one or more items, not necessarily of the same type which are separated by a comma and enclosed in curly brackets {}.

```
>>> S1={1, "Ravi", 75.50}
>>> S1
{1, 75.5, 'Ravi'}
>>> type(S1)
<class 'set'>
>>> S2={10,23,40,23,50,10}
>>> S2
{40, 10, 50, 23}
>>> 
```

**set() function**

Python has an in-built function set() using which set object can be constructed out of any sequence like string, list or tuple object.
```
>>> S1=set("Internshala")
>>> S1
{'t', 'n', 's', 'h', 'e', 'a', 'l', 'I', 'r'}
>>> S2=set([45,67,87,36,55])
>>> S2
{55, 67, 36, 45, 87}
>>> S3=set((10,25,15))
>>> S3
{25, 10, 15}
>>> 
```
The order of elements in the set is not necessarily the same that is given at the time of assignment. Python optimizes the structure for performing operations over the set as defined in mathematics. Only immutable (and hashable) objects can be a part of a set object. Numbers (integer, float as well as complex), strings, and tuple objects are accepted but list and dictionary objects are not.
>>> S1={(10,10), 10,20}
>>> S1
{10, 20, (10, 10)}
>>> S2={[10,10], 10,20}
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    S2={[10,10], 10,20}
TypeError: unhashable type: 'list'
>>> 

In the first case, (10,10) is a tuple, hence it becomes part of a set. In the second example though, since [10,10] is a list, an error message is displayed saying the list is unhashable. (Hashing is a mechanism in computer science that enables quicker searching of objects in the computer’s memory. https://en.wikipedia.org/wiki/Hash_function) Even though mutable objects are not stored in a set, set itself is a mutable object. A set object can be modified by add(), update(), remove() and discard() methods.

Operations Perform is-: 

- add()
- update()
- clear()
- copy()
- discard()
- remove()

### Set Operations

As mentioned earlier, set data type in Python implements set as defined in mathematics. Various Set operations can be performed using Python’s set object. The operators |, &, - and ^ perform union, intersection, difference, and symmetric difference operations respectively. Each of these operators have a corresponding method associated with a built-in set class.

Operation Perform is-: 

- Union 
- Intersection
- Difference
- Symmetric difference


- **Concatentaion(+)**

**Appends the second list or tuple to the first.**

The data types being concatenated should be of the same type. For example, you cannot concatenate a list and a tuple.

**List**
```
>>> founders=["Iron Man", "Thor", "Ant-Man", "Hulk", "Wasp"]
>>> recruits=["Captain America", "Hawkeye"]
>>> founders + recruits
['Iron Man', 'Thor', 'Ant-Man', 'Hulk', 'Wasp', 'Captain America', 'Hawkeye']
>>> 
```
**Tuple**
```
>>> stark=("Ned", "Catelyn", "Brandon", "Sansa", "Arya", "Robb")
>>> mormont=("Jeor", "Maege", "Jorah", "Lyanna")
>>> stark + mormont
('Ned', 'Catelyn', 'Brandon', 'Sansa', 'Arya', 'Robb', 'Jeor', 'Maege', 'Jorah', 'Lyanna')
>>> 
```

- **Repetition(*)**

**List**
```
>>> dna=["A", "G","T","C"]
>>> dna * 3
['A', 'G', 'T', 'C', 'A', 'G', 'T', 'C', 'A', 'G', 'T', 'C']
>>> 
```

**Tuple**
```
>>> glucose=("C6", "H12", "O6")
>>> glucose*6
('C6', 'H12', 'O6', 'C6', 'H12', 'O6', 'C6', 'H12', 'O6', 'C6', 'H12', 'O6', 'C6', 'H12', 'O6', 'C6', 'H12', 'O6')
>>> 
```

- **Slice[]**

**Returns the item at given index in a list or tuple.**
A negative index counts the position from right with the count starting at -1.

Note: Recall that the index starts at 0.

**List**
```
>>> founders=["Iron Man", "Thor", "Ant-Man", "Hulk", "Wasp"]
>>> founders[3]
'Hulk'
>>> 
>>> founders[-3]
'Ant-Man'
>>> 
```
**Tuple**
```
>>> stark=("Ned", "Catelyn", "Brandon", "Sansa", "Arya", "Robb")
>>> stark[2]
'Brandon'
>>> 
>>> stark[-1]
'Robb'
>>> 
```
- **Range Slice[:]**

**List**
```
>>> avengers=["Iron Man", "Thor", "Ant-Man", "Hulk", "Wasp", "Captain America", "Hawkeye"]
>>> avengers[2:5]
['Ant-Man', 'Hulk', 'Wasp']
>>> 
>>> avengers[3:]
['Hulk', 'Wasp', 'Captain America', 'Hawkeye']
>>> 
>>> avengers[:3]
['Iron Man', 'Thor', 'Ant-Man']
>>> 
```

**Tuple**
```
>>> got=("Ned", "Catelyn", "Brandon", "Sansa", "Arya", "Robb", "Jeor", "Maege", "Jorah", "Lyanna")
>>> got[1:4]
('Catelyn', 'Brandon', 'Sansa')
>>> 
>>> got[3:]
('Sansa', 'Arya', 'Robb', 'Jeor', 'Maege', 'Jorah', 'Lyanna')
>>> got[4:]
('Arya', 'Robb', 'Jeor', 'Maege', 'Jorah', 'Lyanna')
>>> 
```
- **In Membership**

**List**
```
>>> avengers=["Iron Man", "Thor", "Ant-Man", "Hulk", "Wasp", "Captain America", "Hawkeye"]
>>> "Wasp" in avengers
True
>>> 
>>> "Black Widow" in avengers
False
>>> 
```

**Tuple**
```
>>> got=("Ned", "Catelyn", "Brandon", "Sansa", "Arya", "Robb", "Jeor", "Maege", "Jorah", "Lyanna")
>>> "Arya" in got
True
>>> 
>>> "Jon" in got
False
>>> 
```

- **not in membership**

**List**
```
>>> avengers=["Iron Man", "Thor", "Ant-Man", "Hulk", "Wasp", "Captain America", "Hawkeye"]
>>> "Wasp" not in avengers
False
>>> 
>>> "Black Widow" not in avengers
True
>>> 
```

**Tuple**
```
>>> got=("Ned", "Catelyn", "Brandon", "Sansa", "Arya", "Robb", "Jeor", "Maege", "Jorah", "Lyanna")
>>> "Arya" not in got
False
>>> 
>>> "Jon" not in got
True
>>> 
```

Manipulating Lists

You can modify the items within a list. Modifying a list means tochange an item, or add a new item, or remove an existing item. Here are some methods of the built-in List class that help in modifying lists. Read through each function and then try it out in IDLE.

- append()
- insert()
- remove()
- pop()
- reverse()
- sort()

- **Tuple to List**
```
>>> t2=('python', 'java', 'c++')
>>> list(t2)
['python', 'java', 'c++']
>>> s1="Internshala"
>>> list(s1)
['I', 'n', 't', 'e', 'r', 'n', 's', 'h', 'a', 'l', 'a']
>>> 
```

- **List to Tuple**
```
>>> L2=['C++', 'Java', 'Python', 'Ruby']
>>> tuple(L2)
('C++', 'Java', 'Python', 'Ruby')
>>> s1="Internshala"
>>> tuple(s1)
('I', 'n', 't', 'e', 'r', 'n', 's', 'h', 'a', 'l', 'a')
>>> 
```

![](https://github.com/Psingh12354/PythonNotes/blob/main/img2.PNG)

- Items()
```
>>> captains={'England': 'Root', 'Australia': 'Smith', 'India': 'Virat', 'Pakistan': 'Sarfraz'}
>>> captains.items()
dict_items([('England', 'Root'), ('Australia', 'Smith'), ('India', 'Virat'), ('Pakistan', 'Sarfraz')])
>>> 
```

- Keys()
```
>>> captains={'England': 'Root', 'Australia': 'Smith', 'India': 'Virat', 'Pakistan': 'Sarfraz'}
>>> captains.keys()
dict_items(['England', 'Australia', 'India', 'Pakistan'])
>>> 
```

- Values()
```
>>> captains={'England': 'Root', 'Australia': 'Smith', 'India': 'Virat', 'Pakistan': 'Sarfraz'}
>>> captains.values()
dict_items([Root', 'Smith', 'Virat', 'Sarfraz'])
>>> 
```


![](https://github.com/Psingh12354/PythonNotes/blob/main/img3.PNG)
