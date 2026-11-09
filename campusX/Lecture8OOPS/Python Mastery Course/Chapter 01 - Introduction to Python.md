# Chapter 01 - Introduction to Python

**Level:** Beginner  
**Suggested study time:** 3-5 hours  
**Prerequisites:** None

This chapter introduces Python, its history, uses, tools, execution model, and basic input/output. Historical and comparison topics use examples rather than algorithms; step-by-step algorithms and dry runs are included wherever code performs a task.

## Learning outcomes

By the end of this chapter, you should be able to:

- Explain what Python is and name its main strengths and tradeoffs.
- Describe the difference between source code, bytecode, and a Python virtual machine.
- Distinguish an interpreter, an interactive shell, an editor, an IDE, and a notebook.
- Run a Python file from a terminal and recognize the steps Python takes to execute it.
- Write readable code with comments, docstrings, correct indentation, `print()`, and `input()`.
- Trace a small program by hand and explain each value as it changes.

## 1. What is Python?

### Definition

Python is a high-level, general-purpose programming language. A Python program is a set of instructions written in Python syntax. A Python implementation reads those instructions and performs the requested work.

- **High-level** means that most programs can be written without directly managing processor registers or memory addresses.
- **General-purpose** means Python can be used for many kinds of work, not only one specialized task.
- **Programming language** means it has rules for expressing instructions and combining them into programs.

### Easy explanation

Think of a program as a recipe and the computer as a very literal cook. The recipe must be written in a language the computer's Python implementation can process. Python lets the recipe be relatively close to the way people describe steps, while still being precise enough for the computer.

```python
print("Hello, Python!")
```

`print` asks Python to display the text in parentheses. The quotes mark the text as a string; they are not displayed.

### Dry run

| Step | Instruction or value | What happens |
|---|---|---|
| 1 | `print("Hello, Python!")` | Python evaluates the string value. |
| 2 | `print(...)` | The text is sent to standard output, usually the terminal. |

### When Python is a good fit

Python is often a good choice when readability, fast development, automation, data work, or a large library ecosystem matters. It may not be the best choice for every hard real-time system, tiny microcontroller, or performance-critical inner loop. Those cases may use a different language, a native library, or a combination of languages.

## 2. History and features of Python

### Short history

- Guido van Rossum began designing Python in the late 1980s.
- Python was first publicly released in 1991.
- Python 2.0 appeared in 2000.
- Python 3.0 appeared in 2008 and introduced changes that could not all remain compatible with Python 2.
- Python 2 reached end of life in 2020. New learning and projects should use a currently supported Python 3 release.

Python continues to evolve through community proposals, releases, and maintenance work. You do not need to memorize release dates to write programs; the important lesson is that the language and its tools change over time.

### Important features

| Feature | Meaning | Small example or consequence |
|---|---|---|
| Readable syntax | Many common operations use concise, familiar words and punctuation. | `total = price * count` |
| High-level | The language hides many low-level machine details. | You can work with a list without allocating each memory slot yourself. |
| Dynamically typed | The type belongs to a value; a variable name can later refer to a value of another type. | `item = 3`, then `item = "three"` |
| Multi-paradigm | The language supports procedural, object-oriented, and functional styles. | A script can use functions and classes together. |
| Automatic memory management | The implementation manages object memory for ordinary programs. | You normally do not manually free each string or list. |
| Standard library | Python ships with modules for common tasks. | `json`, `pathlib`, `datetime`, and `csv` |
| Broad ecosystem | Third-party packages add tools for many domains. | Data science, web development, testing, and automation |
| Portable | The same source can often run on different operating systems when dependencies and environment differences are handled. | A small script can usually run on Windows, macOS, and Linux. |

The details of execution depend on the Python implementation. CPython is the most commonly used implementation, but it is not the only one.

## 3. Why Python is popular

Python is popular because it combines a relatively gentle learning curve with tools used in professional work.

1. **Readable code:** Python often needs fewer punctuation marks and less boilerplate than some alternatives.
2. **Fast experimentation:** An interactive shell and notebooks make it convenient to test a small idea.
3. **Useful libraries:** A library can provide a tested solution for a task that would otherwise take substantial work.
4. **Large community:** Tutorials, examples, forums, and maintained packages are widely available.
5. **Many application areas:** Skills from basic Python transfer to automation, data analysis, web applications, and machine learning.
6. **Good teaching language:** Beginners can focus on the problem before learning many low-level details.

Popularity does not mean Python is always the fastest language or the best tool for every job. Choose a language based on the problem, constraints, team, and available libraries.

### Example: reuse a library

Python's standard library can parse JSON without writing a JSON parser yourself:

```python
import json

text = '{"course": "Python", "weeks": 8}'
course_info = json.loads(text)
print(course_info["course"])
```

The `json` module handles the format rules; the program focuses on using the data.

## 4. Applications of Python

Python is used in many fields:

- **Automation:** Rename files, generate reports, or perform repeated checks.
- **Data science:** Clean data, calculate summaries, and create visualizations.
- **Machine learning and AI:** Prepare data, train models, and connect models to applications.
- **Web development:** Build server-side applications and APIs.
- **Testing and developer tools:** Test software and automate development tasks.
- **Education and research:** Express experiments and calculations clearly.
- **Networking and system administration:** Communicate with services and automate supported operations.

[[diagram:applications]]

### Example: a simple data workflow

A common data-science process can be described without committing to a particular library:

1. Read a dataset.
2. Inspect its columns and values.
3. Handle missing or invalid values.
4. Calculate summaries or train a model.
5. Check the result.
6. Save or present the result.

```python
scores = [72, 81, 90]
average = sum(scores) / len(scores)
print(f"Average score: {average}")
```

**Dry run**

| Step | `scores` | Calculation | Result |
|---|---|---|---|
| 1 | `[72, 81, 90]` | `sum(scores)` | `243` |
| 2 | `[72, 81, 90]` | `len(scores)` | `3` |
| 3 | `[72, 81, 90]` | `243 / 3` | `81.0` |
| 4 | - | formatted output | `Average score: 81.0` |

This tiny example illustrates the idea of transforming input data into a useful result. Real datasets require additional checks, which are covered in later chapters.

## 5. Python vs Java vs C++

These languages are all widely used, but they make different tradeoffs. The table describes common implementations and typical use, not an absolute rule.

| Topic | Python | Java | C++ |
|---|---|---|---|
| Common style | Concise, dynamically typed | Class-oriented, statically typed | Multi-paradigm, statically typed |
| Typical execution | Commonly compiled to bytecode and executed by a Python virtual machine | Compiled to JVM bytecode and executed by a Java virtual machine, often with JIT compilation | Commonly compiled to native machine code |
| Memory | Automatic memory management in common implementations | Automatic memory management through garbage collection | Manual control is possible; smart pointers and libraries can manage ownership |
| Common strengths | Scripting, automation, data science, fast development | Large services, enterprise software, Android-related ecosystems | Systems software, game engines, performance-sensitive components |
| Tradeoffs | Often slower for CPU-heavy pure-Python loops | More declarations and build setup than a tiny Python script | More complexity and responsibility for low-level details |

### Important comparison rules

- No language is automatically best for every project.
- Actual performance depends on the program, implementation, libraries, and workload.
- Python libraries may call optimized C, C++, or Fortran code, so a Python application can still use fast native components.
- Learn the concepts behind types, memory, algorithms, and testing; those concepts transfer between languages.

## 6. Compiled vs interpreted languages

### Definitions

- A **compiler** translates a program from one representation to another before or during execution.
- An **interpreter** executes program instructions by reading and processing them at runtime.
- A **runtime** is the system that supports a running program, such as loading code and providing built-in operations.

These words describe ways of implementing and running a language. They are not always mutually exclusive categories. A language implementation can compile some form of code and also use an interpreter or just-in-time compiler.

### Simple analogy

- **Ahead-of-time compilation:** Translate a whole instruction sheet before the task starts.
- **Interpretation:** Read an instruction, then perform it as you go.
- **Just-in-time compilation:** Observe frequently used work while running and compile selected parts for faster execution.

### Common paths

| Approach | Simplified flow |
|---|---|
| Native compiled program | Source code -> compiler -> machine code -> processor |
| Common CPython execution | Python source -> bytecode -> CPython virtual machine |
| JIT-enabled runtime | Source or bytecode -> runtime -> selected code compiled while running |

The diagram is simplified: real implementations may include parsing, optimization, module loading, caching, and other steps.

**Common misconception:** "Python is interpreted" is a useful beginner-level shorthand, but it hides the fact that CPython normally compiles source to bytecode before its virtual machine executes it.

## 7. How Python works internally

### The basic idea

When a Python program runs, the implementation must turn the text in the source file into actions. In CPython, a simplified path is:

1. Read the source file.
2. Check that its syntax is valid and build an internal representation.
3. Compile the representation to Python bytecode.
4. Have the CPython virtual machine execute the bytecode.
5. Call built-in or library operations as the program needs them.

[[diagram:execution_pipeline]]

For imported modules, CPython may cache bytecode in a `__pycache__` directory. A cache is an optimization, not the original source and not something you normally edit by hand.

### Example

```python
message = "Hello"
print(message)
```

Before the output appears, Python has to recognize a name assignment, a string literal, a function call, and the argument passed to that call. The virtual machine then performs the actions in order.

### Practical way to inspect execution

Python's `dis` module can display bytecode for learning:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

The exact bytecode and display can change between Python versions. Use this to understand that a translation step exists, not to memorize opcode names.

## 8. Python installation and setup

### Windows setup

1. Download a supported Python 3 installer from the official Python website.
2. Run the installer. If the installer offers an **Add Python to PATH** option, enable it when appropriate for your setup.
3. Complete the installation.
4. Open a new PowerShell or Command Prompt window.
5. Check that the Python launcher works:

```powershell
py --version
py -m pip --version
```

The version output should identify an installed Python 3 release. If `py` is not recognized, reopen the terminal first; if it still fails, review the installation and PATH options.

### Create and run a test file

Save this as `hello.py`:

```python
print("Python is ready")
```

In the terminal, change to the directory that contains the file and run:

```powershell
py hello.py
```

Expected output:

```text
Python is ready
```

### Setup habits

- Use a supported Python 3 version.
- Use a project-specific virtual environment when a project has package dependencies; environments are covered in Chapter 22.
- Use `py -m pip ...` on Windows so `pip` is associated with the selected Python launcher.
- Do not install packages just because a tutorial lists them. Install only the dependencies the project needs.
- Keep project files in a folder you can find, and use clear names such as `hello.py`.

## 9. Python interpreter and interactive shell

An **interpreter** is the program that runs Python code. An **interactive shell**, also called a REPL, lets you enter one statement at a time and see results immediately.

REPL means **Read, Evaluate, Print, Loop**:

1. Read the statement.
2. Evaluate it.
3. Print a result when appropriate.
4. Wait for the next statement.

Example session:

```text
>>> 2 + 3
5
>>> name = "Mina"
>>> print(name)
Mina
```

- `>>>` is the primary prompt in the standard Python shell.
- `...` is a continuation prompt, often shown while entering an indented block.
- The shell is useful for short experiments.
- A `.py` file is better for saved, repeatable programs.

[[diagram:repl]]

Start the Windows Python shell with:

```powershell
py
```

Leave it with `exit()` or the terminal's end-of-file shortcut. A program file and the interactive shell use the same Python language, but differ in how code is entered and saved.

## 10. IDEs: VS Code, PyCharm, and Jupyter Notebook

An editor is where you write text. An **IDE** adds development tools such as code completion, navigation, debugging, and project management. A **notebook** lets you organize executable code into cells alongside text and results.

| Tool | Best for | Useful first check |
|---|---|---|
| VS Code | General-purpose editing, projects, and extensions | Select the intended Python interpreter in the workspace. |
| PyCharm | Python-focused projects and integrated navigation/debugging | Confirm the project interpreter and environment. |
| Jupyter Notebook | Experiments, teaching, visualizations, and data analysis | Select the intended kernel; a kernel is the running Python process for the notebook. |

[[diagram:tools]]

### Choose the simplest tool that fits

- For the first few lessons, a terminal and a text editor are enough.
- Use an IDE when you want integrated help, debugging, or project navigation.
- Use a notebook when the work benefits from running cells and seeing output next to explanations.

An IDE is not Python itself. If a file runs in one terminal but not another, compare the selected Python interpreter and installed dependencies.

## 11. Your first Python program

Create a file named `hello.py` with:

```python
name = "Aisha"
print(f"Hello, {name}!")
```

Run it:

```powershell
py hello.py
```

Output:

```text
Hello, Aisha!
```

### What each line means

1. `name = "Aisha"` creates a name that refers to the string `"Aisha"`.
2. `f"Hello, {name}!"` creates a formatted string and inserts the value of `name`.
3. `print(...)` displays the result.

### Algorithm

1. Store a person's name.
2. Build a greeting using that name.
3. Display the greeting.

### Dry run

| Step | `name` | Formatted text | Output |
|---|---|---|---|
| 1 | `"Aisha"` | - | - |
| 2 | `"Aisha"` | `"Hello, Aisha!"` | - |
| 3 | `"Aisha"` | `"Hello, Aisha!"` | `Hello, Aisha!` |

Try changing `"Aisha"` to your own name and run the file again.

## 12. Python execution process

### Running a file

When you run `py hello.py`, the operating system starts the Python launcher, the launcher selects an installed Python interpreter, and that interpreter executes the file.

### A useful mental model

```text
Saved .py file
    -> Python reads and checks the code
    -> code is compiled to bytecode by CPython
    -> the Python virtual machine executes it
    -> output or an error is shown
```

The exact internal steps depend on the Python implementation and version.

### Errors are part of execution

- A **syntax error** means Python cannot parse the code as valid syntax.
- A **runtime error** happens while a program is running, for example when it tries to divide by zero.
- A **traceback** shows where an error occurred and helps you find the relevant line.

Read the last line of a traceback first to identify the error type and message, then inspect the indicated line and the calls leading to it. Debugging is covered more fully in Chapter 21.

## 13. Source code, bytecode, and the Python virtual machine

| Term | Definition | Analogy |
|---|---|---|
| Source code | The human-readable instructions in a `.py` file | The written recipe |
| Bytecode | A lower-level instruction format produced by a Python implementation | A recipe translated into a standard set of kitchen steps |
| Python virtual machine (PVM) | The runtime component that executes Python bytecode in CPython | The worker carrying out those translated steps |

The PVM is not the same thing as a separate computer or a hardware processor. It is software in the Python runtime.

Different implementations can use different internal execution strategies. The terms "bytecode" and "PVM" are most useful here as a CPython learning model.

### Remember the direction

```text
source code -> bytecode -> virtual-machine execution
```

You normally edit source code, not bytecode. If a `__pycache__` folder appears, Python created a cache for imported modules; do not rely on it as the program's source.

## 14. Comments and docstrings

### Comments

A comment explains something to a human reader. A `#` starts a comment that continues to the end of the line.

```python
# Convert minutes to seconds.
minutes = 5
seconds = minutes * 60
print(seconds)
```

Comments do not make code run differently. Prefer comments that explain a reason or a non-obvious decision rather than restating the next line.

### Docstrings

A docstring is a string placed at the start of a module, function, or class to document its purpose. Triple-quoted strings are commonly used.

```python
def minutes_to_seconds(minutes):
    """Convert a number of minutes to seconds."""
    return minutes * 60

print(minutes_to_seconds(5))
```

The function's docstring can be inspected:

```python
print(minutes_to_seconds.__doc__)
```

**Difference:** A comment is for readers of source code. A docstring is documentation attached to a module, class, or function and can be retrieved at runtime.

## 15. Python indentation and syntax

### Indentation defines blocks

Python uses indentation to show which statements belong together. Four spaces per indentation level is the standard convention.

```python
temperature = 24

if temperature > 20:
    print("It is warm.")
    print("Consider drinking water.")

print("This line is outside the if block.")
```

The colon introduces the block. The indented lines belong to the `if`. The final `print` is not indented, so it runs after the conditional block.

### Algorithm

1. Read the temperature.
2. Compare it with 20.
3. If it is greater than 20, display the two indented messages.
4. Display the final message in every case.

### Dry run for `temperature = 24`

| Step | Check or statement | Result |
|---|---|---|
| 1 | `24 > 20` | `True` |
| 2 | First indented `print` | `It is warm.` |
| 3 | Second indented `print` | `Consider drinking water.` |
| 4 | Unindented `print` | `This line is outside the if block.` |

### Common syntax mistakes

- Forgetting the colon after `if`, `for`, `while`, `def`, or `class`.
- Mixing tabs and spaces in a block.
- Using inconsistent indentation levels.
- Misspelling a name or using the wrong capitalization: `print` and `Print` are different names.
- Forgetting quotes around text: `print(hello)` looks for a variable named `hello`; `print("hello")` prints text.

Let your editor insert spaces consistently. If you see `IndentationError` or `SyntaxError`, read the line named in the error and also inspect the lines just before it.

## 16. `print()` and `input()`

### `print()`

`print()` displays values. It can display more than one value, choose a separator with `sep`, and choose what to end with using `end`.

```python
print("Python", "is", "ready", sep=" - ")
print("One", end=" ")
print("line")
```

Output:

```text
Python - is - ready
One line
```

### `input()`

`input()` displays an optional prompt, waits for the user to type text and press Enter, and returns that text as a string.

```python
name = input("What is your name? ")
print(f"Welcome, {name}!")
```

If a program needs a number, convert the returned string:

```python
age_text = input("How old are you? ")
age = int(age_text)
print(f"Next year you will be {age + 1}.")
```

`int()` works only when the text represents a valid integer. Invalid text causes a `ValueError`; robust error handling is taught in Chapter 15.

### Worked algorithm: add two numbers

**Problem:** Ask for two whole numbers and display their sum.

**Algorithm**

1. Ask for the first number as text.
2. Convert it to an integer.
3. Ask for the second number as text.
4. Convert it to an integer.
5. Add the two integers.
6. Display the sum.

[[diagram:add_numbers]]

**Code**

```python
first_text = input("First whole number: ")
first_number = int(first_text)

second_text = input("Second whole number: ")
second_number = int(second_text)

total = first_number + second_number
print(f"Sum: {total}")
```

**Dry run with inputs `12` and `8`**

| Step | Variable or operation | Value |
|---|---|---|
| 1 | User types first input | `"12"` (text) |
| 2 | `int(first_text)` | `12` (integer) |
| 3 | User types second input | `"8"` (text) |
| 4 | `int(second_text)` | `8` (integer) |
| 5 | `12 + 8` | `20` |
| 6 | `print(...)` | `Sum: 20` |

**Key lesson:** Input begins as text. Convert it before doing numeric arithmetic.

## Common misconceptions

1. **"Python is only interpreted."** CPython normally compiles source to bytecode, then executes it in its runtime.
2. **"A variable has a permanent type."** In Python, a name can refer to values of different types at different times. The values still have types.
3. **"`input()` gives me a number."** It returns a string; convert it with `int()` or `float()` when needed.
4. **"An IDE is Python."** An IDE is a tool for editing and running code. A Python interpreter runs the program.
5. **"Indentation is just decoration."** In Python, indentation is part of the syntax and determines code blocks.
6. **"A comment and a docstring are identical."** A docstring is attached to a module, class, or function and can be inspected at runtime.

## Practice problems with solutions

### Problem 1: personal introduction

Ask for a name and a favorite subject. Print one sentence containing both.

**Solution**

```python
name = input("Name: ")
subject = input("Favorite subject: ")
print(f"{name} enjoys {subject}.")
```

**Dry run:** If the inputs are `Ravi` and `math`, the output is `Ravi enjoys math.`

### Problem 2: minutes to seconds

Ask for a whole number of minutes and display the equivalent number of seconds.

**Algorithm:** Read minutes -> convert to integer -> multiply by 60 -> print.

```python
minutes = int(input("Minutes: "))
seconds = minutes * 60
print(f"Seconds: {seconds}")
```

**Dry run:** Input `3` gives `3 * 60 = 180`, so the output is `Seconds: 180`.

### Problem 3: predict the output

```python
course = "Python"
print("Learn", course, sep=": ")
```

**Solution:** `print` receives two values and joins them using `": "`. The output is:

```text
Learn: Python
```

### Problem 4: find and fix the syntax error

```python
if 5 > 2
    print("Five is greater")
```

**Solution:** The `if` statement needs a colon. Correct code:

```python
if 5 > 2:
    print("Five is greater")
```

### Problem 5: explain the input type

What is the type of `value` in this code before conversion?

```python
value = input("Enter a number: ")
```

**Solution:** `value` is a string (`str`), even if the user types digits. For example, typing `42` gives the text `"42"`. Use `int(value)` to convert it to the integer `42`.

## Key terms

| Term | Short definition |
|---|---|
| Python | A high-level, general-purpose programming language |
| Implementation | A program that provides the language's behavior, such as CPython |
| Interpreter | Software that runs Python code |
| Interactive shell / REPL | A prompt for entering and evaluating statements interactively |
| Source code | Human-readable program text |
| Bytecode | A lower-level instruction representation used by an implementation |
| PVM | The Python virtual machine that executes bytecode in the CPython model |
| IDE | An editor combined with development tools |
| Notebook | A document containing executable cells, text, and outputs |
| Comment | A source-code note beginning with `#` |
| Docstring | A documentation string attached to a module, class, or function |
| Traceback | A report showing the call path and location associated with an error |

## Chapter mastery checklist

- [ ] I can explain Python in one or two sentences.
- [ ] I can name three strengths and one tradeoff of Python.
- [ ] I can describe the simplified CPython source-to-bytecode-to-VM path.
- [ ] I know the difference between a shell, a `.py` file, an IDE, and a notebook.
- [ ] I can save and run a Python file from a terminal.
- [ ] I can use comments, docstrings, and consistent four-space indentation.
- [ ] I know that `input()` returns text and can convert valid numeric input.
- [ ] I can trace the two-number addition program without running it.
- [ ] I completed the practice problems and can explain why each solution works.

## Next chapter

Chapter 2 covers variables, assignment, naming rules, dynamic typing, object references, identity, and introductory memory concepts.
