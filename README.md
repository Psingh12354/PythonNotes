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
