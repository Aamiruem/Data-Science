In Python, a list is a built-in data structure used to store a collection of items. Lists are:

Ordered: The items in a list have a defined order, and the order is preserved.

Mutable: Lists can be modified after creation (you can add, remove, or change elements).

Heterogeneous: Lists can store elements of different data types (e.g., integers, strings, floats, other lists, etc.).

Indexed: Each element in a list has an index, starting from 0 for the first element.

Creating a List
You can create a list by enclosing elements in square brackets [], separated by commas.

Example:

python
Copy
my_list = [1, 2, 3, 4, 5]  # List of integers
mixed_list = [1, "Hello", 3.14, True]  # List with mixed data types
nested_list = [[1, 2], [3, 4], [5, 6]]  # List of lists
empty_list = []  # Empty list
Accessing List Elements
You can access elements in a list using their index. Python uses zero-based indexing, meaning the first element is at index 0.

Example:

python
Copy
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Output: 10 (first element)
print(my_list[2])  # Output: 30 (third element)
print(my_list[-1]) # Output: 50 (last element, using negative indexing)
Modifying a List
Lists are mutable, so you can change their elements after creation.

Example:

python
Copy
my_list = [1, 2, 3, 4, 5]
my_list[2] = 99  # Change the third element
print(my_list)   # Output: [1, 2, 99, 4, 5]
Common List Operations
Adding Elements:

append(): Adds an element to the end of the list.

insert(): Inserts an element at a specific index.

extend(): Adds multiple elements (from another list) to the end.

Example:

python
Copy
my_list = [1, 2, 3]
my_list.append(4)       # Adds 4 to the end
my_list.insert(1, 99)   # Inserts 99 at index 1
my_list.extend([5, 6])  # Adds 5 and 6 to the end
print(my_list)          # Output: [1, 99, 2, 3, 4, 5, 6]
Removing Elements:

remove(): Removes the first occurrence of a specific value.

pop(): Removes and returns the element at a specific index (default is the last element).

clear(): Removes all elements from the list.

Example:

python
Copy
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # Removes the first occurrence of 3
my_list.pop(1)     # Removes and returns the element at index 1 (2)
my_list.clear()    # Clears the list
print(my_list)     # Output: []
Slicing a List:

You can extract a portion of a list using slicing.

Example:

python
Copy
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])   # Output: [1, 2, 3] (elements from start to index 2)
print(my_list[2:])   # Output: [3, 4, 5] (elements from index 2 to end)
Finding Elements:

index(): Returns the index of the first occurrence of a value.

count(): Returns the number of occurrences of a value.

Example:

python
Copy
my_list = [1, 2, 3, 2, 4]
print(my_list.index(2))  # Output: 1 (index of the first occurrence of 2)
print(my_list.count(2))  # Output: 2 (number of times 2 appears)
Sorting and Reversing:

sort(): Sorts the list in ascending order (or descending with reverse=True).

reverse(): Reverses the order of elements in the list.

Example:

python
Copy
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()      # Sorts the list in ascending order
print(my_list)     # Output: [1, 1, 3, 4, 5, 9]
my_list.reverse()  # Reverses the list
print(my_list)     # Output: [9, 5, 4, 3, 1, 1]
List Comprehensions
List comprehensions provide a concise way to create lists.

Example:

python
Copy
squares = [x**2 for x in range(5)]  # Creates a list of squares
print(squares)  # Output: [0, 1, 4, 9, 16]
Key Features of Lists
Dynamic: Lists can grow or shrink in size as needed.

Versatile: Can store any type of data, including other lists (nested lists).

Iterable: You can loop through a list using a for loop.

Example Use Case
python
Copy
# Storing and processing student grades
grades = [85, 90, 78, 92, 88]
grades.append(95)  # Add a new grade
grades.sort()      # Sort grades in ascending order
average = sum(grades) / len(grades)  # Calculate average
print("Grades:", grades)
print("Average:", average)
