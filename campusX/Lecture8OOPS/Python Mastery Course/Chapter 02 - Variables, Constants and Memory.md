# Chapter 02 - Variables, Constants and Memory

**Level:** Beginner  
**Suggested study time:** 4-6 hours  
**Prerequisites:** Chapter 1 - running a Python file and reading simple expressions

In this chapter, a variable is treated as a name that refers to an object, not as a permanent box with a type. That model makes assignment, dynamic typing, identity, and shared mutable values easier to understand.

## Learning outcomes

- Create and update variables using assignment.
- Choose valid, readable names and recognize Python keywords.
- Explain dynamic typing and compare it with static typing.
- Use multiple assignment and unpacking safely.
- Explain the difference between equality and identity.
- Use `type()` and `id()` for basic inspection without making incorrect assumptions about memory.
- Describe introductory Python memory management and name scope.

## 1. What is a variable?

### Definition

A variable is a name in a program that refers to a value or object. For example, after `score = 85`, the name `score` can be used to access the integer value `85`.

### Easy explanation

Imagine writing a label on a card and pointing the label at an object. The label is the variable name; the object is the value. The label does not permanently own a particular kind of value. It can later be made to refer to another object.

```python
score = 85
print(score)
```

`score` is the name. `85` is the integer object. The assignment statement binds the name to that object.

[[diagram:variable_reference]]

### Important distinction

The `=` sign in an assignment means "bind the name on the left to the result on the right." It does not mean mathematical equality.

```python
score = 85
score = score + 5
print(score)
```

The second statement first calculates `score + 5`, which is `90`, and then rebinds `score` to the result.

### Dry run

| Step | Statement | Name binding after the step |
|---|---|---|
| 1 | `score = 85` | `score` refers to `85` |
| 2 | `score = score + 5` | Python reads `85`, calculates `90`, then binds `score` to `90` |
| 3 | `print(score)` | Displays `90` |

## 2. Variable declaration and assignment

### Definition

An assignment statement evaluates an expression and binds its result to one or more names. In ordinary Python code, you do not declare a variable's type before assigning to its name.

```python
student_name = "Nila"
student_score = 92
passed = True
```

Python creates the bindings when these statements run. The names are not available before their assignment in the current scope.

### Assignment order

For `total = price * quantity`, Python:

1. Evaluates the expression `price * quantity`.
2. Gets the resulting value.
3. Binds `total` to that value.

If a name on the right has not been assigned, Python raises `NameError`.

```python
price = 4
quantity = 3
total = price * quantity
print(total)
```

**Dry run**

| Step | Expression | Value |
|---|---|---|
| 1 | `price = 4` | `price` refers to `4` |
| 2 | `quantity = 3` | `quantity` refers to `3` |
| 3 | `price * quantity` | `4 * 3 = 12` |
| 4 | `total = ...` | `total` refers to `12` |

### Assignment versus comparison

- `=` assigns a value: `count = 3`
- `==` compares values: `count == 3`

They have different purposes and cannot be swapped.

## 3. Variable naming rules

Python names are case-sensitive identifiers. Use names that tell a reader what the value represents.

### Rules

- A name can contain letters, digits, and underscores.
- A name cannot start with a digit.
- Spaces and punctuation such as `-` are not allowed in a variable name.
- Uppercase and lowercase are different: `score`, `Score`, and `SCORE` are three different names.
- A Python keyword cannot be used as a name.
- Python permits many Unicode letters, but English letters and underscores are the most portable choice for shared code.

### Naming style

```python
student_name = "Nila"     # descriptive
quiz_score = 92           # descriptive
x = 92                    # valid, but unclear outside a small calculation
```

For ordinary variables and functions, Python's common style uses `snake_case`: lowercase words separated by underscores.

| Name | Valid? | Reason |
|---|---|---|
| `user_name` | Yes | Letters and underscore |
| `score2` | Yes | A digit is allowed after the first character |
| `_total` | Yes | An underscore may begin a name |
| `2score` | No | A name cannot start with a digit |
| `user-name` | No | A hyphen is interpreted as subtraction |
| `first name` | No | Spaces are not allowed |

### Practical naming test

Before creating a name, ask: "Could someone who did not write this code guess what value it holds?" Prefer `monthly_income` to `m` when the purpose is not obvious.

## 4. Identifiers and keywords

An **identifier** is a name used for a variable, function, class, module, or other program object. A **keyword** is a reserved word with a special meaning in Python's grammar.

Examples of keywords include `if`, `else`, `for`, `while`, `def`, `class`, `return`, `True`, `False`, and `None`.

Do not memorize a list from a random webpage; the language can add keywords. Ask Python for the list when needed:

```python
import keyword

print(keyword.kwlist)
```

You can also check one name:

```python
import keyword

print(keyword.iskeyword("class"))
print(keyword.iskeyword("student_name"))
```

The first call displays `True`; the second displays `False`. A built-in name such as `list` is not necessarily a keyword, but replacing it with your own variable name is still a bad idea because it hides the built-in function.

## 5. Dynamic typing

### Definition

Python is dynamically typed: values have types at runtime, and a name can be rebound to values of different types during execution.

```python
item = 25
item = "twenty-five"
```

This is valid. In the first assignment, `item` refers to an integer. In the second, it refers to a string.

Dynamic typing does **not** mean that Python values have no types. It means you do not normally write a type declaration for every variable before using it.

### Dry run

| Statement | Value referred to by `item` | Type |
|---|---|---|
| `item = 25` | `25` | `int` |
| `item = "twenty-five"` | `"twenty-five"` | `str` |

If a later operation is not supported by the current value, Python reports an error:

```python
item = "twenty-five"
print(item + 5)
```

This raises `TypeError` because Python does not know whether the programmer intended text concatenation, numeric conversion, or something else.

## 6. Static vs dynamic typing

### Definition

- In a **statically typed** language, type checking is commonly performed before the program runs, and variables or expressions have declared or inferred types that constrain valid operations.
- In a **dynamically typed** language, types are associated with runtime values and many type checks happen while the program runs.

The exact rules vary among languages; these terms describe broad approaches, not a complete comparison.

| Question | Dynamic typing (Python) | Static typing (for example, Java) |
|---|---|---|
| When are many type mistakes detected? | Often while the relevant code runs | Often during compilation or static analysis |
| Must a beginner declare every variable type? | Usually no | Often yes, depending on the language |
| Can names refer to different types of values? | Yes | Usually restricted by the declared or inferred type |
| Does either approach prevent every bug? | No | No |

Python also supports optional type annotations and external static type checkers. These tools are covered in Chapter 23. Python's runtime behavior remains dynamically typed.

## 7. Multiple variable assignments

Python lets one assignment statement bind several names.

### Chained assignment

```python
first = second = 0
```

Both names refer to the same integer object. This is safe for integers because integers are immutable. Do not assume the same pattern creates independent mutable lists:

```python
first = second = []
first.append("new")
print(second)
```

The output is `['new']` because both names refer to the same list. Use separate list literals when independent lists are intended:

```python
first = []
second = []
```

### Assigning different values

```python
minimum, maximum = 0, 100
```

The right-hand expressions are evaluated, then assigned to the left-hand names from left to right.

## 8. Multiple-value unpacking

Unpacking assigns items from an iterable to several names.

```python
first, second = 10, 20
print(first)
print(second)
```

The number of targets must match the number of values unless a starred target collects the remainder.

### Swap two names

Python can swap names without a temporary variable:

```python
left = "A"
right = "B"
left, right = right, left
print(left, right)
```

### Algorithm

1. Evaluate the right-hand values using the current bindings: `right` is `"B"` and `left` is `"A"`.
2. Keep those two results for the assignment.
3. Bind `left` to `"B"`.
4. Bind `right` to `"A"`.

### Dry run

| Moment | `left` | `right` |
|---|---|---|
| Before swap | `"A"` | `"B"` |
| Values evaluated on right | `"A"` | `"B"` |
| After unpacking assignment | `"B"` | `"A"` |

### Starred unpacking

```python
first, *middle, last = [10, 20, 30, 40]
print(first)
print(middle)
print(last)
```

The result is `first == 10`, `middle == [20, 30]`, and `last == 40`. The starred target receives a list. A starred target can collect zero or more values.

If the number of values does not fit the targets, Python raises `ValueError`:

```python
first, second = [10, 20, 30]  # too many values
```

## 9. Constants and naming conventions

Python does not have a general syntax that makes a variable permanently constant. By convention, a name written in uppercase with underscores signals that a value is intended to remain unchanged.

```python
SECONDS_PER_MINUTE = 60
MAX_RETRIES = 3
```

This convention helps readers. It does not stop reassignment:

```python
SECONDS_PER_MINUTE = 60
SECONDS_PER_MINUTE = 30  # Python allows this; avoid it by convention.
```

For type-checking tools, `typing.Final` can communicate that a name should not be reassigned:

```python
from typing import Final

SECONDS_PER_MINUTE: Final = 60
```

`Final` is a static-analysis hint; it does not make the value immutable at runtime.

### Three different ideas

- **Constant name:** A naming convention that tells people not to reassign a name.
- **Immutable object:** An object whose value cannot be changed in place, such as an `int` or `str`.
- **Mutable object:** An object that can be changed in place, such as a `list` or `dict`.

A constant name may refer to a mutable object. The name convention alone does not freeze that object.

## 10. Object references

### Definition

An object reference is the relationship between a name and the object it currently refers to. Assignment usually creates or updates a binding; it does not automatically make a copy of the object.

```python
original = [1, 2]
alias = original
alias.append(3)
print(original)
```

Both names refer to the same list, so changing the list through `alias` is visible through `original`.

**Dry run**

| Step | Operation | `original` and `alias` |
|---|---|---|
| 1 | Create `[1, 2]` and bind `original` | `original -> list [1, 2]` |
| 2 | `alias = original` | Both names refer to that list |
| 3 | `alias.append(3)` | The shared list becomes `[1, 2, 3]` |
| 4 | `print(original)` | Displays `[1, 2, 3]` |

To create a shallow copy of a list, use a copy operation:

```python
original = [1, 2]
copy_of_original = original.copy()
copy_of_original.append(3)
print(original)  # [1, 2]
```

Shallow and deep copying are studied further with collections in later chapters.

## 11. Object identity and `id()`

### Equality and identity preview

Every object has an identity during its lifetime. `id(value)` returns an integer that identifies that object for the lifetime of the object. The exact representation is implementation-dependent.

```python
value = [1, 2]
print(id(value))
```

Do not treat the number from `id()` as a portable memory address. Do not assume a particular number, pattern, or ordering. An identity may be reused after an object is no longer alive.

Use `id()` mainly as a learning or debugging tool when investigating whether two references point to the same object. In ordinary programs, `is` is the direct identity test:

```python
first = []
second = first
third = []

print(first is second)  # True
print(first is third)   # False
```

`first` and `second` share one object; `third` is a separate list with the same initial contents.

## 12. The `type()` function

`type(value)` returns the type object of a value. It is useful for learning and basic inspection.

```python
print(type(42))
print(type(3.5))
print(type("hello"))
print(type([1, 2]))
```

Typical output names are `int`, `float`, `str`, and `list`.

For a yes/no question such as "is this an integer or a subclass of integer?", `isinstance(value, int)` is usually more flexible than comparing `type(value)` exactly. The distinction matters because Python has type inheritance; for example, `bool` is a subclass of `int`.

```python
print(isinstance(True, int))  # True
```

This behavior is explained more fully in the data-types chapter.

## 13. `is` vs `==`

These operators answer different questions:

- `a == b` asks whether the values compare equal.
- `a is b` asks whether both names refer to the same object.

```python
first = [1, 2]
second = [1, 2]
third = first

print(first == second)  # True: same contents
print(first is second)  # False: separate list objects
print(first is third)   # True: same object
```

### Correct use of `is`

Use `is` when identity is what matters, especially when testing for `None`:

```python
result = None

if result is None:
    print("No result yet")
```

Do not use `is` to compare strings or numbers for their value. Some implementations reuse certain objects as an optimization, so identity results for equal small values should not be used as a substitute for `==`.

### Dry run

| Expression | Question | Result |
|---|---|---|
| `first == second` | Do their list values compare equal? | `True` |
| `first is second` | Are they the same list object? | `False` |
| `first is third` | Are they the same list object? | `True` |

## 14. Memory management basics

Python's runtime manages memory for objects. As a beginner, create values and let Python manage their ordinary lifetime; do not try to manually free memory.

### Useful ideas

- Names are bindings in a namespace.
- Objects occupy memory while they are needed by the running program.
- Multiple names can refer to one object.
- Removing one name does not necessarily remove the object if another name still refers to it.
- When an object is no longer reachable and is no longer needed, the implementation can reclaim its memory.

In CPython, reference counting is an important memory-management mechanism, and a cyclic garbage collector handles certain reference cycles. These are implementation details, not a guarantee that every Python implementation uses exactly the same internal mechanism.

### `del` removes a binding

```python
numbers = [1, 2]
another_name = numbers
del numbers
print(another_name)
```

`del numbers` removes the name `numbers`. The list remains reachable through `another_name`, so it is still usable.

### Practical memory habits

- Avoid keeping large objects reachable after they are no longer useful.
- Do not create unnecessary copies of very large data.
- Use a context manager for resources such as files; file handling is covered in Chapter 16.
- Profile memory when a real program has a measured memory problem instead of guessing.

## 15. Variable scope introduction

### Definition

Scope describes where a name can be accessed. A **local variable** is created inside a function and is normally available only within that function. A name defined at the top level of a module is a **global name** for that module.

```python
course_name = "Python"  # module-level name

def show_course():
    message = "Learning " + course_name  # local name: message
    print(message)

show_course()
```

`message` is local to `show_course`. `course_name` is found at module scope.

### LEGB lookup rule

When Python looks up a name inside a function, the common search order is:

1. **L - Local:** The current function.
2. **E - Enclosing:** Any enclosing function, from inner to outer.
3. **G - Global:** The current module.
4. **B - Built-in:** Names provided by Python, such as `print` and `len`.

[[diagram:scope_lookup]]

### Local variables and parameters

```python
def add_tax(price, tax_rate):
    tax = price * tax_rate
    return price + tax

total = add_tax(100, 0.1)
print(total)
```

`price`, `tax_rate`, and `tax` are local to the function call. The `return` statement sends a result back, where it is bound to the outer name `total`.

### Scope mistakes

Do not use a global variable when a function parameter or return value communicates the data more clearly. The `global` and `nonlocal` keywords exist, but using them casually can make programs harder to reason about. Functions and scope are covered in depth in Chapter 12.

## Worked program: swap two values and report the types

### Problem

Start with two values, swap their references using unpacking, then display the values and their types.

### Algorithm

1. Bind `left` to `"red"` and `right` to `"blue"`.
2. Evaluate the right-hand side `right, left` using the current values.
3. Assign those two values to `left` and `right`.
4. Display the new values.
5. Display the type of each value.

```python
left = "red"
right = "blue"

left, right = right, left

print(left, right)
print(type(left).__name__, type(right).__name__)
```

### Dry run

| Step | `left` | `right` | Notes |
|---|---|---|---|
| 1 | `"red"` | - | First assignment |
| 2 | `"red"` | `"blue"` | Second assignment |
| 3 | `"blue"` | `"red"` | Unpacking swap |
| 4 | - | - | Prints `blue red` |
| 5 | - | - | Prints `str str` |

### Why the swap works

Python evaluates the values on the right before binding the targets on the left. The original values are therefore available while the new bindings are made.

## Common mistakes and debugging

### `NameError`

```python
print(total)
```

If `total` has not been assigned in the current scope, Python raises `NameError`. Check spelling, capitalization, and whether the assignment ran before the use.

### Accidental reuse of a built-in name

```python
list = [1, 2, 3]
```

This hides the built-in `list` name in the current scope. Choose a descriptive name such as `scores`.

### Unexpected shared list

```python
first = second = []
first.append(1)
```

Both names refer to one list. Create two separate lists if that is what the problem requires.

### Comparing identity instead of value

```python
name = input("Name: ")
if name is "Aisha":  # do not use identity for string value comparison
    print("Hello")
```

Use `==` to compare string contents:

```python
if name == "Aisha":
    print("Hello")
```

## Practice problems with solutions

### Problem 1: calculate a rectangle's area

Use `width = 8` and `height = 5`. Store the area in a well-named variable and print it.

**Solution**

```python
width = 8
height = 5
rectangle_area = width * height
print(rectangle_area)
```

The multiplication gives `40`. `rectangle_area` describes what the result represents.

### Problem 2: swap two numbers

Start with `first = 4` and `second = 9`. Swap them and print both.

**Solution**

```python
first = 4
second = 9
first, second = second, first
print(first, second)
```

Output: `9 4`.

### Problem 3: identify aliasing

What does this program print, and why?

```python
one = [5]
two = one
two.append(8)
print(one)
```

**Solution:** It prints `[5, 8]`. Both names refer to the same list object, and `append` changes that object.

### Problem 4: choose equality or identity

Two separately created lists contain the same values. Which operator checks that their contents compare equal?

**Solution:** Use `==`. Use `is` only when you need to know whether both names refer to the exact same object.

### Problem 5: fix a naming error

Why is `2nd_score = 90` invalid? Give a valid alternative.

**Solution:** A Python identifier cannot begin with a digit. Use `second_score = 90`.

## Key terms

| Term | Short definition |
|---|---|
| Variable / name | A name bound to a value or object |
| Assignment | Evaluation of a right-hand expression followed by a name binding |
| Identifier | A name used for a program object |
| Keyword | A reserved word in the Python language |
| Dynamic typing | Runtime values have types; names can be rebound to other types |
| Constant convention | Uppercase naming that signals a value should not be reassigned |
| Reference | A name-to-object relationship |
| Identity | The property that distinguishes one object from another during its lifetime |
| `id()` | A function returning an object's identity value |
| Scope | The region where a name can be accessed |
| LEGB | Local, Enclosing, Global, Built-in name lookup order |

## Chapter mastery checklist

- [ ] I can explain a variable as a name bound to an object.
- [ ] I can use `=` for assignment and `==` for value comparison.
- [ ] I can identify valid names and avoid Python keywords.
- [ ] I can explain dynamic typing without saying values have no types.
- [ ] I can unpack values and swap two names.
- [ ] I understand why `first = second = []` creates an alias.
- [ ] I know that `is` checks identity and `==` compares values.
- [ ] I can use `type()` and `isinstance()` to inspect values.
- [ ] I can explain local scope and the LEGB lookup order.
- [ ] I can dry-run the worked swap program.

## Next chapter

Chapter 3 introduces Python's built-in data types, including numbers, strings, lists, tuples, ranges, sets, dictionaries, and `None`.
