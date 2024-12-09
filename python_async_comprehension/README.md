# Python - Async Comprehension

## How to write an asynchronous generator
An asynchronous generator is a generator function that uses async def and yields values using yield inside an async function. It allows producing values asynchronously, often waiting between yields.

**Example: Async Generator to Yield Numbers with Delays**
```python
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate asynchronous work
        yield i  # Yield a value asynchronously

# Usage:
async def main():
    async for value in async_generator():
        print(value)

# Run main() in an asyncio event loop
# Output: Prints numbers 0 to 4, one per second
```

## How to use async comprehensions
An async comprehension is similar to a list comprehension, but it works with asynchronous iterators (like an async generator). It allows collecting values from an async generator in a concise way.

**Example: Collect Values Using an Async Comprehension**
```python
import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

# Usage of async comprehension
async def main():
    results = [value async for value in async_generator()]
    print(results)

# Run main() in an asyncio event loop
# Output: [0, 1, 2, 3, 4]
```

**Exemple 2:**
```python
result = []
async for i in aiter():
    if i % 2:
        result.append(i)
```

With the proposed asynchronous comprehensions syntax, the above code becomes as short as:
```python
result = [i async for i in aiter() if i % 2]
```

The PEP also makes it possible to use the await expressions in all kinds of comprehensions:
```python
result = [await fun() for fun in funcs]
```


## How to type-annotate generators
When type-annotating generators, you specify the types of the values it yields and the return value. For asynchronous generators, you use AsyncGenerator from typing.

**Example: Type-Annotated Async Generator**
```python
from typing import AsyncGenerator
import asyncio

async def async_generator() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i

# Explanation:
# - `AsyncGenerator[int, None]` means:
#   - It yields `int` values.
#   - It does not accept any input after a `yield` (hence `None`).
```

## Other Types Asynch comprehension:
```python
+ set comprehension: {i async for i in agen()}
+ list comprehension: [i async for i in agen()]
+ dict comprehension: {i: i ** 2 async for i in agen()}
+ generator expression: (i ** 2 async for i in agen())
```

It is allowed to use async for along with if and for clauses in asynchronous comprehensions and generator expressions:
```python
dataset = {data for line in aiter()
                async for data in line
                if check(data)}

```

## await in Comprehensions:
```python
result = [await fun() for fun in funcs]
result = {await fun() for fun in funcs}
result = {fun: await fun() for fun in funcs}

result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth}
result = {fun: await fun() for fun in funcs if await smth}

result = [await fun() async for fun in funcs]
result = {await fun() async for fun in funcs}
result = {fun: await fun() async for fun in funcs}

result = [await fun() async for fun in funcs if await smth]
result = {await fun() async for fun in funcs if await smth}
result = {fun: await fun() async for fun in funcs if await smth}
```

## Some more exemples: 

```python
import asyncio
async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)
async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
```

**Note that what you really want to do is call another async def function instead of calling range directly!**
