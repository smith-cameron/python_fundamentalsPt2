## Python Syntax
### [PEP8](https://peps.python.org/pep-0008/)  Python Enhancement Proposals... version 8
### __Indentation__ 
in VSCODE: use either:
- indent rainbow 
- or render white space
to trigger the subconscious tracking of indentation

### Code blocks/Functions 
[Python Syntax](https://login.codingdojo.com/m/506/12457/87299)
COLON:

|----|COLON : 

|----|----|and indentation

Required For
- functions
- if, elif, else (conditional statements)
- for, while (loops)
- Class (classes)

## [Conditionals](https://login.codingdojo.com/m/506/12457/87307)
**if, elif, else (conditional statements)**
Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.  
These statements control the flow of how our code is executed by the interpreter

[DOCS - Comparisons](https://docs.python.org/3/library/stdtypes.html#typesseq-rcomparisons)

|Operator|Description|Example|
|---|---|---|
|`==`|Checks if the value of two operands are equal|1 `==` 2 `=>` False<br>1 `==` 1 `=>` True|
|!=|Checks if the value of two operands are not equal|1 != 2 => True<br>1 != 1 => False|
|>|Checks if the value of left operand is greater than the value of right operand|1 > 2 => False<br>2 > 1 => True|
|<|Checks if the value of left operand is less than the value of right operand|1 < 2 => True  <br>2 < 1 => False|
|>=|Checks if the value of left operand is greater than or equal to the value of right operand|1 >= 2 => False  <br>2 >= 2 => True|
|<=|Checks if the value of left operand is less than or equal to the value of right operand|1 <= 2 => True  <br>2 <= 2 => True|
|and|Checks that each expression on the left and right are both True|(1 <= 2) and (2 <= 3) => True  <br>(1 <= 2) and (2 >= 3) => False  <br>(1 >= 2) and (2 >= 3) => False|
|or|Checks if either the expression on the left or right is True|(1 <= 2) or (2 >= 3) => True  <br>(1 <= 2) or (2 <= 3) => True  <br>(1 >= 2) or (2 >= 3) => False|
|not|Reverses the true-false value of the operand|not True => False  <br>not False => True  <br>not 1 >= 2 => True  <br>not 1 <= 2 => False  <br>not (1 <= 2 and 2 >= 3)  => True  <br>not 1 <= 2 and 2 >= 3 => False|

## Functions
A **function** is a **named block of code that we can execute to perform a specific task**
list of instructions that we can run at any time and as many times as required
__IS__:
- has a name
- takes in parameters (parenthesis required, parameters optional)
- perform a series of instructions
- return something afterwards (will return None if there is no explicit return statement)
__WHY__:
- Reducing the duplication of code
- Breaking down complex problems into simpler pieces
- Improving clarity of code
__SYNTAX__
- `def` 
- Name
- Parameters
- Colon
- Indentation
- Body
- `return`
```python
def function_name(parameters):
	# Code block of 
	# stuff:
		#and things to do
	return "anything we want"
```
### Arguments/Parameters
**define parameters** - define the input of functions using parameters
- Define: `conditionals(boundary, input)`
**provide arguments** - pass in arguments into functions.
- Provide a value in function call: `conditionals(5,2)`

==Trigger==: TypeError: conditionals() takes 0 positional arguments but 1 was given 
==Trigger==: conditionals() missing 1 required positional argument: 'input'
### [Named arguments/parameters](https://login.codingdojo.com/m/506/12457/87313)
#### Default parameters
- Define: `conditionals(boundary = 10, input = 5)`
- Override in function call: `conditionals(5,2)`
#### Named Arguments
- conditionals(input = 5,boundary = 2)
#### How To Use Combinations of Named arguments/parameters
- __no arguments are provided__ -- the defaults are used
- __one unnamed argument provided__ -- provided value is used as the value for the first parameter, and the second parameter's default value is used
- __one named argument provided__ -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
- __both unnamed arguments provided__ -- values assigned to parameters in order (i.e. what we've been doing up to this point)
- __both named arguments provided__ -- values are assigned to associated parameters (and then order doesn't matter!)

## Composite Types 
### Lists (Arrays)
#### **Definition**:
- A list in Python is an ordered and mutable collection of items.
- Lists are defined by enclosing a comma-separated sequence of elements within square brackets `[]`.
- Element values can be anything - even more composite types

#### Syntax
```python
#Create: 
list_name = [value, value, value]
words = ["start","going","till","the","end"]
numbers= [1,2,3,4,5,6,7,8,9]
mix_up = ["start",6,[1,2,3,4,5],numbers,True, 22.45,"end"]
```
Because they are mutable we can perform operations on them
==Modularize and keep clean by using functions ==
- Concatenation: `list1 + list2` combines two lists.
- Repetition: `my_list * 3` repeats the list three times.
- Both yield a new list
__*Similarly to strings. In python a string is treated like a list of character substrings*__
##### **Accessing Elements**
Lists can shrink or grow or be updated
- List elements are indexed starting from 0 (zero).
- You can access elements using indexing.
    - Example: `first_element = my_list[0]` (returns 1)

**Iterating Over Lists**:
    - You can use loops (e.g., `for` loop) to iterate over the elements of a list.
__Example__:
```python
for item in my_list:
	print(item)
```
## Loops(lists & strings)
### Definition
In Python, loops are used to execute a block of code repeatedly as long as a certain condition is met. 
Python supports two main types of loops: `for` loops and `while` loops.
### Syntax
#### FOR
```python
for oneThing in manyThings:
	print(do some stuff)

for iteratorVariable in range(start, stop, step):
	print(do some stuff)
```
Defined __Horizontally__
- Iterator
- Start
- Stop(boundary)
- Step(rate of movement)
- Indented code block
#### Loops#For In
your typical loop in python
- The `for` loop iterates over a sequence (which can be a list, tuple, string, or any iterable) and executes a block of code for each item in the sequence.
- The `variable` takes on the value of each item in the sequence during each iteration.
- The loop continues until there are no more items in the sequence.
- prints the values only
```python
def for_in():
    for unicorn in mash_up:
        print(unicorn)
# for_in()

def nested_for_in():
    for unicorn in words:
        print(unicorn)
        for i in unicorn:
            print(i)
# nested_for_in()
```
#### Loops#For in range() 
The [`range()`](https://docs.python.org/3/library/stdtypes.html#range "range") Function
If you want to adjust the start stop step of the for loop you can use [`range()`](https://docs.python.org/3/library/stdtypes.html#range "range")
#### While
```python
iteratorVariable = start
while (conditional_boundary):
	# do some stuff
	iteratorVariable += step

# > WHILE
# < ITERATOR, START, STOP/BOUNDARY, STEP (DEFINED VERTICALLY)

#, iteratorVariable = start
#, while (conditional_boundary):
#, 	# do some stuff
#, 	iteratorVariable += step

def while_loops():
    i = 10
    while (i <= 20):
        print(f"i: {i}")
        i += 1
# while_loops()
```
Defined __Vertically__
- Iterator
- Start
- Stop(boundary)
- Step(rate of movement)
- Indented code block

### Loop Control Statements:
Python provides several loop control statements to modify the behavior of loops:

- `break`: Terminates the loop prematurely, even if the loop condition is still `True`.
- `continue`: Skips the rest of the current iteration and proceeds to the next iteration of the loop.
- `pass`: Acts as a placeholder, doing nothing. It is used when syntactically a statement is required but no action is desired.
- `return`: Terminates the function and return the return value to the function call regardless of looping.

Example using `break`:
```python
for num in range(10):     
	if num == 5:         
		break     
	print(num)
```

Example using `continue`:
```python
for num in range(10):     
	if num == 5:         
		continue     
	print(num)
```
### Looping with `else`:
Python allows you to use an `else` block with loops. The code in the `else` block will execute when the loop completes normally (i.e., without encountering a `break` statement).

__Example__ with `else`:
```python
for i in range(5):
    print(i)
else:
    print("Loop completed without a break")
```
[Sequence Operations - Docs](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)
[Built in Interpreter Functions - DOCS](https://docs.python.org/3.10/library/functions.html)

### Addtional List Content
#### [List Slicing](https://login.codingdojo.com/m/506/12457/87698)
[List Slicing/python-reference.readthedocs.io](https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html)
You can create a sublist (slice) from a list by specifying start and end indices.
__Example__: `sub_list = my_list[1:4]` (returns `[2, 3, 4]`)
```python
words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']
```

#### List Comprehension
##### Definition
List comprehensions in Python provide a concise and efficient way to 
- create lists by applying an expression to each item in an iterable (e.g., a list, tuple, or range) 
- optionally filtering the items based on a condition. 

They are a powerful and readable alternative to traditional for loops when you want to generate a new list from an existing iterable. 
##### Syntax
The basic syntax of a list comprehension is:
```python
new_list = [expression for item in iterable]
```
 - `expression` is the operation you want to perform on each item.
 - `item` is a variable that represents each element in the iterable.
 - `iterable` is the source of data (e.g., a list, tuple, or range).

**Example**:
Suppose you have a list of numbers and you want to create a new list that contains the squares of these numbers.
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
```
In this case, `squares` will be `[1, 4, 9, 16, 25]`.

##### More...
1. **Conditionals in List Comprehensions**:
   - You can include conditional statements to filter elements in the iterable before applying the expression.
   - The syntax for this is:
     ```
     new_list = [expression for item in iterable if condition]
     ```
   - Example: Create a list of even numbers from a given list.
     ```python
     numbers = [1, 2, 3, 4, 5]
     even_numbers = [x for x in numbers if x % 2 == 0]
     ```

   `even_numbers` will be `[2, 4]`.

2. **Multiple Conditions**:
   - You can use multiple conditions within a list comprehension.
   - Example: Create a list of numbers that are both even and greater than 2.
     ```python
     numbers = [1, 2, 3, 4, 5, 6]
     result = [x for x in numbers if x % 2 == 0 and x > 2]
     ```

   `result` will be `[4, 6]`.

3. **Nested List Comprehensions**:
   - You can also nest list comprehensions to create more complex structures.
   - Example: Create a 2D matrix (list of lists) using nested comprehensions.
     ```python
     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
     flattened = [x for row in matrix for x in row]
     ```

   `flattened` will be `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.

## **Benefits of List Comprehensions**:
   - They are concise and easy to read.
   - They often result in faster code execution compared to traditional for loops.
   - They are a Pythonic way to work with lists, emphasizing readability and simplicity.

## **When to Use List Comprehensions**:
   - List comprehensions are ideal when you want to transform, filter, or generate new lists from existing data.
   - For more complex logic or when you need to modify multiple variables, traditional loops may be more appropriate.
