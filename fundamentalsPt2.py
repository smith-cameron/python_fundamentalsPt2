
# _ Functions
# < a named block of code that we can execute to perform a specific task
# < we can run at any time and as many times as required

def function_name(input):
    # code body
    # do work here
    print(input)
    print("hello_world from inside the function code block")
    return f"return anything from inside the function we like: {input}"
# return_value = function_name(11)
# print(return_value)

# _ Conditionals
# < if, elif, else (conditional statements)
# < Conditional statements allow us to run certain lines of code
    # < depending on whether certain conditions are met.
# < These statements control the flow of how our code is executed
def conditionals():
    x = 12
    if x > 50:
        print("bigger than 50")
    else:
        print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute

    x = 55
    if x > 10:
        print("bigger than 10")
    elif x > 50:
        print("bigger than 50")
    else:
        print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

    if x < 10:
        print("smaller than 10")
    # nothing happens, because the statement is false   

def conditionals_with_params(input1 = 12, input2 = 7):
    if input1 > input2:
        # If statements are ALWAYS CHECKED
        # This block will only run if condition is truthy
        print("if")
        print(f"{input1} is bigger than {input2}")
    elif input1 < input2:
        # elif statements are checked IF ABOVE IS falsy
        # This block will only run if condition is truthy
        print("elif")
        print(f"{input2} is bigger than {input1}")
    else:
        # Will run ONLY if all conditions above are falsy
        print("else")
        print("they are equal")
# conditionals_with_params(input2 = 5,input1 = 6)

# < Named Arguments & Default Parameters
#* no arguments are provided -- the defaults are used
#* one unnamed argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used
#* one named argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
#* both unnamed arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)
#* both named arguments provided -- values are assigned to associated parameters (and then order doesn't matter!)


# _ Lists
# < an ordered and mutable collection of items.
# < a comma-separated sequence of elements within square brackets
# < Element values can be anything - even more composite types
# < 0 base index

# > SYNTAX => list_name = [value, value, value]
words = ["start","going","till","the","end"]
numbers= [1,2,3,4,5,6,7,8,9]
mix_up = ["start",6,[1,2,3,4,5],numbers,True, 22.45,"end"]
        #   0     1     2        3      4      5     6
# print(len(mix_up))

# > Accessing Values:
def accessing_list_values():
    # print(mix_up[3])
    # * print(list_name[index])
    
    # > Replacing values
    # * list_name[index] = new_value
    mix_up[6] = "finished"
    # print(mix_up)

    # > Store value temporarily
    # * temp = list_name[index]
    temp = mix_up[5]
    print(temp)
    mix_up[5] = mix_up[1]
    mix_up[1] = temp
    
    # > Replace a value with another value
    # * list_name[index] = list_name[other_index]
    mix_up[5] = mix_up[1]
    
    # > Adding values to a list
    # * list_name.append(new_value)
    words.append("just kiddingggg")
    
    # > Removing values of a list
    # * list_name.pop()
    # * list_name.pop(0)
    words.pop()
    words.pop(0)
    
    # > Number of Elements
    print(len(mix_up))
# accessing_list_values()

# ? List vs. Tuple
# < Lists are mutable, while tuples are immutable (cannot be changed once created).
# < Lists are defined with square brackets, and tuples use parentheses.

def tuple_stuff():
    my_tuple = ('this is a tuple', True, [1, 2, 3, 4, 5])
    my_list = ['this is a tuple', False, [1, 2, 3, 4, 5]]
    import sys
    print("Byte size of tuple", sys.getsizeof(my_tuple))
    print("Byte size of list", sys.getsizeof(my_list))
# tuple_stuff()

# _ Loops
# < used to execute a block of code repeatedly as long as a certain condition is met.
# < Python supports two main types of loops: `for` loops and `while` loops

# > FOR IN
#,  for oneThing in manyThings:
#,      print(do some stuff)
def for_in_loop():
    for unicorn in numbers:
        print(unicorn)
# for_in_loop()
def for_in_string_loop():
    for unicorn in "all the beautiful unicorns":
        print(unicorn)
# for_in_string_loop()
def nested_for_in():
    for unicorn in words:
        print(unicorn)
        for horn in unicorn:
            print(horn)
# nested_for_in()

# > FOR IN RANGE
# < ITERATOR, START, STOP/BOUNDARY, STEP (DEFINED HORIZONTALY)

#,  for iteratorVariable in range(start, stop, step):
#, 	    print(do some stuff)
def for_in_range():
    print(len(mix_up)+1)
    for i in range(0, len(mix_up),1):
        print(f"i: {i}")
        print(f"value: {mix_up[i]}")
# for_in_range()

# > WHILE
# < ITERATOR, START, STOP/BOUNDARY, STEP (DEFINED VERTICALLY)

#,  iteratorVariable = start
#,  while (conditional_boundary):
#, 	    # do some stuff
#, 	    iteratorVariable += step
def while_loop():
    i = 10
    while (i <= 20):
        print(i)
        i += 1
# while_loop()