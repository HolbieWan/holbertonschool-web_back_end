# Type Annotations in Python 3

+ **What:**
    + Type annotations allow developers to specify the expected data types of variables, function arguments, and return values in Python. This helps improve code readability and maintainability.
+ **Why:**
    + Helps catch type-related errors early during development.
	+ Improves IDE support with better autocomplete and type hints.
	+ Makes the codebase easier to understand and maintain.
+ **How:**
    + Use type hints for variables, function parameters, and return values.

+ **Example:**
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

age: int = 25
```
---

## How You Can Use Type Annotations to Specify Function Signatures and Variable Types

+ **What:**
    + Type annotations in function signatures specify the types of inputs and outputs. For variables, annotations indicate their expected type.
+ **Why:**
    + Defines clear expectations for functions and variables.
    + Reduces runtime errors caused by unexpected types.
+ **How:**
    + Use : to annotate parameters and -> for return values. Variable annotations use :.

+ **Example:**
```python
def add_numbers(a: int, b: int) -> int:
    return a + b

x: float = 3.14
```
---

## Duck Typing

+ **What:**
    + Duck typing focuses on the behavior of objects rather than their type. If an object implements the expected methods or attributes, it can be used, regardless of its type.
+ **Why:****
    + Promotes flexibility in code.
    + Enables writing functions that work with different object types, as long as they provide the expected behavior.
+ **How:**
    + Avoid strict type checks, and instead rely on the object’s methods and attributes.
   
+ **Example:**
```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(duck: "Any"):
    duck.quack()

make_it_quack(Duck())
make_it_quack(Person())
```
---

## How to Validate Your Code with Mypy

+ **What:**
    + MyPy is a static type checker for Python. It verifies that your type annotations are consistent and valid.
+ **Why:**
    + Identifies potential type errors before runtime.
    + Enforces type safety in your codebase.
+ **How:**
    + Install MyPy using pip install mypy, then run mypy on your code.

+ **Example:**
```python
# sample.py
def multiply(a: int, b: int) -> int:
    return a * b

x: str = multiply(2, 3)  # This is a type error

# Validate with MyPy
# Command: mypy sample.py
# Output: error: Incompatible types in assignment (expected "str", got "int")
```