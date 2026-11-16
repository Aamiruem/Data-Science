# Chapter 03 - Python Data Types

**Level:** Beginner  
**Suggested study time:** 5-7 hours  
**Prerequisites:** Chapters 1 and 2

A data type describes the kind of value an object represents and the operations available for it. Choosing the right type helps a program store, validate, and process information correctly.

## Learning outcomes

- Recognize Python's common built-in types.
- Use numeric, Boolean, and string values.
- Choose between lists, tuples, ranges, sets, and dictionaries.
- Explain mutability, ordering, and hashability.
- Check types and convert values safely.
- Diagnose common type errors by examining the values and operations involved.

## 1. What are data types?

### Definition

A data type describes the kind of value an object represents and the operations that make sense for that value.

Examples:

- `42` is an integer; it can be added to another integer.
- `"42"` is text; it can be joined to other text.
- `[4, 2]` is a list; it can store multiple values and can be changed.
- `{"name": "Mina"}` is a dictionary; it maps keys to values.

### Easy explanation

Think of a type as a set of rules for how a value behaves. The characters `42` can mean a number or text depending on how they are written:

```python
number = 42
text = "42"

print(number + 1)  # 43
print(text + "1")  # 421
```

The visible digits look similar, but their types support different operations.

### Dry run

| Expression | Type of values | Operation | Result |
|---|---|---|---|
| `42 + 1` | `int` and `int` | Numeric addition | `43` |
| `"42" + "1"` | `str` and `str` | Text concatenation | `"421"` |

## 2. Built-in data types

Python provides common types as part of the language. This table groups important examples by purpose.

| Group | Common built-in types | Typical use |
|---|---|---|
| Numbers | `int`, `float`, `complex` | Counts, measurements, and mathematical values |
| Truth values | `bool` | Conditions that are true or false |
| Text | `str` | Names, messages, and other Unicode text |
| Sequences | `list`, `tuple`, `range` | Ordered values that can be visited by position |
| Mapping | `dict` | Key-to-value associations |
| Sets | `set`, `frozenset` | Collections of unique hashable values |
| Binary data | `bytes`, `bytearray`, `memoryview` | Data represented as bytes |
| Absence | `NoneType` | The single value `None`, often meaning "no value" |

Python also has types in libraries, such as `Decimal`, `date`, and `DataFrame`. Those are not all built-in types.

[[diagram:built_in_types]]

### Inspect an example

```python
values = [42, 3.5, True, "hello", [1, 2], (1, 2), {1, 2}, {"x": 1}, None]

for value in values:
    print(value, type(value).__name__)
```

This program loops over several values and prints each value with its type name. Loops are taught in detail in Chapter 6; here, focus on the different types in the list.

## 3. Numeric types: `int`, `float`, and `complex`

### Integers: `int`

An integer represents a whole number without a fractional part.

```python
students = 28
temperature_change = -3
```

Python integers can grow beyond the fixed-width range used by many processors, limited in practice by available memory. Very large integer calculations may take more time and memory.

### Floating-point numbers: `float`

A float represents an approximate real number using binary floating-point arithmetic.

```python
price = 19.99
ratio = 3.0
```

Some decimal fractions cannot be represented exactly in binary floating point:

```python
print(0.1 + 0.2)
```

The result may display as `0.30000000000000004`. For many measurements this approximation is acceptable. For exact decimal currency rules, Python's `decimal.Decimal` may be a better tool.

### Complex numbers: `complex`

A complex number has real and imaginary parts. Python uses `j` for the imaginary unit:

```python
signal = 2 + 3j
print(signal.real)
print(signal.imag)
```

The output is `2.0` and `3.0`. Complex numbers are useful in some engineering, scientific, and mathematical applications.

### Arithmetic example

```python
whole = 7
measurement = 2.5
combined = whole + measurement
print(combined)
print(type(combined).__name__)
```

The result is `9.5`, and its type is `float`. When an integer and a float are combined with addition, Python converts the integer for that operation.

## 4. Boolean: `True` and `False`

A Boolean (`bool`) represents one of two truth values: `True` or `False`. Booleans are often produced by comparisons and used by conditions.

```python
age = 20
is_adult = age >= 18
print(is_adult)
```

The comparison `20 >= 18` is true, so `is_adult` refers to `True`.

### Truthiness

Some values behave as false in a condition, such as `False`, `None`, numeric zero, and empty collections. Many other values behave as true. The conversion can be inspected with `bool()`:

```python
print(bool(0))       # False
print(bool(5))       # True
print(bool(""))      # False
print(bool("False")) # True: this is non-empty text
```

**Important:** `bool("False")` is `True` because the string is not empty. It does not interpret the word as a Boolean setting. Text-to-Boolean parsing needs an explicit rule, covered in the conversion section.

In Python, `bool` is a subclass of `int`, so `True` behaves like `1` and `False` like `0` in some numeric operations. In beginner programs, use Boolean values for logic rather than as a replacement for numeric values.

## 5. String: `str`

A string is an immutable sequence of Unicode text.

```python
name = "Mina"
message = 'Welcome!'
multiline = """This text
uses more than one line."""
```

Single and double quotes both create strings. Triple quotes are commonly used for multiline strings and docstrings.

### Useful operations

```python
first = "data"
second = "science"

print(first + " " + second)
print(first.upper())
print(len(second))
print(first[0])
```

Results:

- Concatenation creates `"data science"`.
- `.upper()` returns `"DATA"`.
- `len(second)` returns `7`.
- `first[0]` returns `"d"`.

Indexing starts at zero. Since strings are immutable, an item cannot be changed in place:

```python
word = "cat"
# word[0] = "b"  # TypeError: strings do not support item assignment
word = "b" + word[1:]
print(word)  # bat
```

The last line creates a new string and rebinds `word`.

### Unicode and encoding

Python strings represent Unicode text. Encoding is the process of converting text to bytes for storage or communication. UTF-8 is a common encoding:

```python
message = "cafe"
encoded = message.encode("utf-8")
decoded = encoded.decode("utf-8")
print(decoded)
```

Text and bytes are different types. File and network programs must use an agreed encoding when converting between them.

## 6. Sequence types

A sequence is an ordered collection whose items can be accessed by position. Common built-in sequences include `str`, `list`, `tuple`, and `range`.

Sequences commonly support:

- Indexing: `items[0]`
- Slicing: `items[1:3]`
- Length: `len(items)`
- Membership: `value in items`
- Iteration: visiting items one at a time

```python
letters = ["a", "b", "c", "d"]
print(letters[0])       # a
print(letters[1:3])     # ['b', 'c']
print("c" in letters)   # True
```

Slicing includes the starting index and excludes the ending index. `letters[1:3]` therefore contains indexes 1 and 2.

Not every sequence is mutable. Lists can be changed in place; strings and tuples cannot.

## 7. List

A list is an ordered, mutable collection. It can hold values of different types, although lists with one clear purpose are often easier to use.

```python
scores = [72, 81, 90]
scores.append(95)
scores[0] = 75
print(scores)
```

The final list is `[75, 81, 90, 95]`.

### Common list operations

| Operation | Example | Effect |
|---|---|---|
| Create | `items = [1, 2]` | Creates a list |
| Add to end | `items.append(3)` | Adds one item |
| Read by index | `items[0]` | Returns the first item |
| Replace by index | `items[0] = 9` | Changes an item |
| Remove by value | `items.remove(2)` | Removes the first matching value |
| Get length | `len(items)` | Counts the items |

### Mutability and references

```python
first = [1, 2]
second = first
second.append(3)
print(first)
```

This prints `[1, 2, 3]` because `first` and `second` refer to the same mutable list.

Create a shallow copy when a separate outer list is needed:

```python
first = [1, 2]
second = first.copy()
second.append(3)
print(first)   # [1, 2]
print(second)  # [1, 2, 3]
```

The copy is shallow: nested mutable objects inside the list may still be shared.

## 8. Tuple

A tuple is an ordered, immutable collection. Use it when the group of values should not be changed as a collection.

```python
point = (4, 7)
print(point[0])
```

The result is `4`. This would fail because a tuple does not support item assignment:

```python
point = (4, 7)
# point[0] = 9  # TypeError
```

### One-item tuple

A comma creates a one-item tuple:

```python
one_item = ("Python",)
not_a_tuple = ("Python")
print(type(one_item).__name__)     # tuple
print(type(not_a_tuple).__name__) # str
```

The parentheses alone do not make a tuple; the comma does.

### Immutability is shallow

A tuple cannot replace its own element, but an element inside it may refer to a mutable object:

```python
record = ("scores", [70, 80])
record[1].append(90)
print(record)
```

This is allowed because the list changes; the tuple's reference to that list remains the same. Immutable tuple does not mean every nested value is immutable.

## 9. `range`

`range` represents an arithmetic sequence of integers. It is often used to repeat an operation a known number of times.

```python
for number in range(1, 5):
    print(number)
```

This displays `1`, `2`, `3`, and `4`. The stop value `5` is excluded.

### Forms

- `range(stop)` starts at 0 and steps by 1.
- `range(start, stop)` starts at `start` and stops before `stop`.
- `range(start, stop, step)` also sets the increment.

```python
print(list(range(2, 11, 2)))
```

The result is `[2, 4, 6, 8, 10]`. Converting to `list` is useful for seeing the values; a range itself stores the parameters and generates values as needed.

### Dry run for `range(2, 8, 2)`

| Attempted value | Is it less than stop `8`? | Included? |
|---:|---|---|
| 2 | Yes | Yes |
| 4 | Yes | Yes |
| 6 | Yes | Yes |
| 8 | No | No |

## 10. Set and `frozenset`

A set is a collection of unique, hashable values. A set is mutable; a `frozenset` is its immutable counterpart.

```python
tags = {"python", "data", "python"}
print(tags)
```

The set contains only `"python"` and `"data"`; repeated values are collapsed. Do not rely on set display or iteration order.

### Common set operations

```python
left = {"a", "b", "c"}
right = {"b", "c", "d"}

print(left | right)  # union
print(left & right)  # intersection
print(left - right)  # values only in left
```

The output order may vary because sets are not an indexed sequence.

### Empty set

```python
empty_set = set()
empty_dictionary = {}
```

`{}` creates a dictionary, not a set. Use `set()` for an empty set.

### Immutable set

```python
fixed_tags = frozenset({"python", "data"})
```

A `frozenset` cannot be changed after creation and can be used as a dictionary key or as a member of another set if its contents are hashable.

## 11. Dictionary

A dictionary (`dict`) maps keys to values. Keys are unique and must be hashable. Values can be of any type.

```python
student = {
    "name": "Mina",
    "score": 92,
}

print(student["name"])
student["score"] = 95
student["passed"] = True
```

`student["name"]` looks up the value for the `"name"` key. Assignment updates an existing key or adds a new one.

### Safer lookup with `get`

Indexing a missing key raises `KeyError`. `get` returns a default when a key is absent:

```python
student = {"name": "Mina"}
score = student.get("score", 0)
print(score)
```

The output is `0`. `get` does not add the missing key.

### Iterating over dictionary data

```python
for key, value in student.items():
    print(key, value)
```

Dictionary insertion order is guaranteed by the language specification in modern Python versions (Python 3.7 and later). This does not make a dictionary a sequence: it is accessed by keys, not integer positions.

## 12. `None`

`None` is Python's single value meaning "no value" or "not available here." Its type is `NoneType`.

```python
result = None

if result is None:
    print("No result has been calculated.")
```

Use `is None` and `is not None` for this check. Do not use `== None` as the normal style.

Functions that finish without an explicit `return` return `None`. A function may also return `None` intentionally to indicate that no result was found.

`None` is not the same as `0`, `False`, or an empty string. Those values have different meanings and types.

## 13. Mutable vs immutable

- A **mutable** object can be changed after it is created. Examples include lists, dictionaries, and sets.
- An **immutable** object cannot be changed in place. Examples include integers, floats, Booleans, strings, and tuples as containers.

[[diagram:mutability]]

### Rebinding is not mutation

```python
count = 4
count = count + 1
```

The integer `4` was not changed. The expression produces an integer value `5`, and the name `count` is rebound.

```python
names = ["Mina"]
names.append("Ravi")
```

Here, the existing list object is mutated by adding an item.

### Why the difference matters

When two names refer to one mutable object, a mutation through either name is visible through both. With an immutable value, an operation produces a result and a name can be rebound to it.

## 14. Ordered vs unordered

An ordered collection has a defined order that can be observed consistently according to its type's rules. A sequence such as a list preserves its item positions.

- `list`, `tuple`, `str`, and `range` have sequence order.
- Dictionaries preserve insertion order in modern Python.
- Sets do not promise a useful iteration order; do not write code that depends on one.

**Important:** "Unordered" does not mean the display must be random every time. It means the type does not promise the positional ordering that your program should rely on.

If a stable sorted result is needed, sort the values explicitly:

```python
numbers = {8, 2, 5}
print(sorted(numbers))
```

`sorted` returns a list in ascending order.

## 15. Hashable vs unhashable

An object is **hashable** when it has a hash value that remains stable during its lifetime and it can be compared for equality consistently. Hashable values can be used as dictionary keys and set members.

Common hashable values include integers, strings, and tuples whose elements are all hashable. Lists, dictionaries, and sets are unhashable because they are mutable.

```python
student_scores = {
    "Mina": 92,
    "Ravi": 88,
}
```

Strings work as keys. This does not:

```python
# invalid = {[1, 2]: "value"}  # TypeError: list is unhashable
```

A tuple is hashable only when all of its contents are hashable:

```python
valid_key = (1, "room")
invalid_key = (1, [2, 3])
```

The first tuple can be used as a key; the second cannot because it contains a list.

## 16. Type checking

Use `type(value)` to inspect the exact type during learning:

```python
value = 12.5
print(type(value))
```

Use `isinstance(value, expected_type)` for a general type check that also recognizes subclasses:

```python
value = True
print(isinstance(value, bool))  # True
print(isinstance(value, int))   # True: bool is a subclass of int
```

Do not scatter checks through a program when the operations themselves can clearly express the requirement. Validate input at boundaries, then keep the main logic straightforward.

### Exact type vs compatible type

- `type(value) is int` asks whether the exact type is `int`.
- `isinstance(value, int)` asks whether it is an `int` or an instance of a subclass.

For most ordinary type validation, prefer `isinstance`.

## 17. Type conversion

Type conversion creates or requests a value of another type. Common constructors include `int`, `float`, `str`, `bool`, `list`, `tuple`, and `set`.

```python
age_text = "21"
age = int(age_text)

price_text = "12.5"
price = float(price_text)

print(age + 1)
print(price * 2)
```

Not every conversion is possible:

```python
# int("twenty")  # ValueError
```

### Converting collections

```python
letters = list("cat")
unique_letters = set("cacao")
pair = tuple([1, 2])
```

Results:

- `list("cat")` creates `["c", "a", "t"]`.
- `set("cacao")` contains unique letters, with no promised order.
- `tuple([1, 2])` creates `(1, 2)`.

### Boolean conversion warning

`bool(value)` checks truthiness; it does not parse words such as `"true"` or `"false"`:

```python
print(bool("false"))  # True, because the string is non-empty
```

For text settings, define accepted spellings and compare normalized text:

```python
answer = input("Enable feature? ").strip().lower()
enabled = answer in {"yes", "y", "true"}
print(enabled)
```

The braces above create a set of accepted strings; membership is used to check whether the normalized answer matches one of them.

## 18. Implicit vs explicit conversion

### Implicit conversion

An implicit conversion is performed by Python as part of an operation when the language defines a safe rule for it.

```python
result = 3 + 2.5
print(result)
print(type(result).__name__)
```

Python converts the integer to a floating-point value for the addition. The result is `5.5` and has type `float`.

### Explicit conversion

An explicit conversion is requested by the programmer:

```python
age_text = "21"
age = int(age_text)
```

Explicit conversion makes an important decision visible. It can also fail, so untrusted input may need validation and exception handling.

**Do not assume** Python will convert arbitrary text to a number or automatically treat a numeric-looking string as numeric.

## 19. Type errors and debugging

A `TypeError` often means an operation is not defined for the types or values used.

```python
age_text = "21"
next_age = age_text + 1
```

The program tries to combine a string and an integer. Python raises `TypeError`.

### Debugging method

1. Read the exception type and message at the end of the traceback.
2. Locate the line where the operation failed.
3. Inspect the values immediately before the operation.
4. Use `type(value)` or `isinstance(value, Type)` if you are unsure.
5. Decide the intended meaning: text concatenation, numeric arithmetic, or another operation.
6. Convert or validate at the point where external data enters the program.

Corrected example:

```python
age_text = "21"
age = int(age_text)
next_age = age + 1
print(next_age)
```

Output: `22`.

### Practical checklist

- Is the input a string because it came from `input()`?
- Is a list being changed through another name that refers to the same object?
- Is a dictionary key missing?
- Is a set being treated like an indexed list?
- Is a conversion invalid for the actual input text?
- Does the traceback identify a different line than the one you first suspected?

## Worked algorithm: remove duplicates but preserve first-seen order

### Problem

Given a list of words, create a new list with each word appearing once, preserving the order of its first appearance.

### Algorithm

1. Start with an empty set called `seen` and an empty list called `unique_words`.
2. Visit each word in the input list from left to right.
3. If the word is not in `seen`, add it to `seen` and append it to `unique_words`.
4. Return or display `unique_words`.

The list preserves order. The set makes membership checks convenient. A set's own order is not used for the result.

```python
words = ["red", "blue", "red", "green", "blue"]
seen = set()
unique_words = []

for word in words:
    if word not in seen:
        seen.add(word)
        unique_words.append(word)

print(unique_words)
```

### Dry run

| Input word | Already in `seen`? | `seen` after step | `unique_words` after step |
|---|---|---|---|
| `"red"` | No | `{"red"}` | `["red"]` |
| `"blue"` | No | `{"red", "blue"}` | `["red", "blue"]` |
| `"red"` | Yes | unchanged | unchanged |
| `"green"` | No | includes `"green"` | `["red", "blue", "green"]` |
| `"blue"` | Yes | unchanged | unchanged |

Output:

```text
['red', 'blue', 'green']
```

This example uses both a mutable list and a mutable set, and demonstrates why the set's ordering is irrelevant to the required result.

## Common misconceptions

1. **"A number written with digits is always numeric."** Quotes make `"42"` a string.
2. **"A tuple makes everything inside it immutable."** A tuple's references cannot be replaced, but a referenced list can still be changed.
3. **"Sets always print in the same useful order."** Set order is not guaranteed for program logic.
4. **"A dictionary is unordered."** Modern Python guarantees dictionary insertion order, but dictionaries are still mappings, not sequences.
5. **"`bool('False')` is false."** It is true because the string is non-empty.
6. **"`None`, `0`, and `False` all mean the same thing."** They are distinct values with distinct types and meanings.
7. **"A tuple is always hashable."** Every tuple element must be hashable for the tuple itself to be hashable.

## Practice problems with solutions

### Problem 1: classify values

Write a list containing an integer, a float, a string, a Boolean, a list, and `None`. Print each value's type name.

**Solution**

```python
values = [7, 2.5, "seven", False, [7], None]

for value in values:
    print(type(value).__name__)
```

The type names are `int`, `float`, `str`, `bool`, `list`, and `NoneType`.

### Problem 2: explain the result

```python
text = "5"
number = 5
print(text == number)
```

**Solution:** It prints `False`. The values have different types and do not compare equal. Convert `text` with `int(text)` if the program should compare numeric values.

### Problem 3: build a dictionary

Create a dictionary with a person's name and city. Use `.get()` to display a missing `"country"` key with a default of `"Unknown"`.

**Solution**

```python
person = {"name": "Mina", "city": "Pune"}
country = person.get("country", "Unknown")
print(country)
```

Output: `Unknown`. The lookup does not add `"country"` to the dictionary.

### Problem 4: fix Boolean parsing

Why is `bool("no")` true? Write an expression that treats `"yes"` and `"y"` as true after ignoring letter case and surrounding spaces.

**Solution**

```python
answer = input("Continue? ").strip().lower()
continue_program = answer in {"yes", "y"}
```

`"no"` is a non-empty string, so `bool("no")` is true. The solution checks explicit accepted answers instead.

### Problem 5: preserve order while removing duplicates

Use the worked algorithm with `["a", "b", "a", "c"]`. What is the result?

**Solution:** `["a", "b", "c"]`. The second `"a"` is already in `seen`, so it is not appended again.

## Key terms

| Term | Short definition |
|---|---|
| Data type | A category describing a value and its supported operations |
| `int` | Whole-number type |
| `float` | Approximate floating-point numeric type |
| `complex` | Number with real and imaginary parts |
| `bool` | Type for `True` and `False` |
| `str` | Immutable Unicode text sequence |
| Sequence | Ordered collection accessed by position |
| Mutable | Able to change in place |
| Immutable | Not able to change in place |
| Mapping | Key-to-value collection such as `dict` |
| Hashable | Suitable for set membership and dictionary keys |
| `None` | Python's value for absence or no result |

## Chapter mastery checklist

- [ ] I can distinguish numeric values from numeric-looking strings.
- [ ] I can describe the main built-in Python types.
- [ ] I can choose a list, tuple, set, or dictionary for a simple problem.
- [ ] I understand `range` starts at its first value and stops before its stop value.
- [ ] I can explain list aliasing and shallow copying.
- [ ] I know that dictionary keys and set members must be hashable.
- [ ] I can explain the difference between mutable and immutable objects.
- [ ] I use `is None` for a `None` check.
- [ ] I can convert valid input and explain why invalid conversion can fail.
- [ ] I can debug a basic `TypeError` by checking the value types.
- [ ] I can dry-run the duplicate-removal algorithm.

## Next chapter

Chapter 4 introduces arithmetic, comparison, assignment, logical, bitwise, membership, and identity operators.
