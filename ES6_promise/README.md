# ES6 - Promises

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

+ Promises (how, why, and what)
+ How to use the then, resolve, catch methods
+ How to use every method of the Promise object
+ Throw / Try
+ The await operator
+ How to use an async function

Promises in JavaScript are a way to manage asynchronous code and make it more readable and maintainable. However, with ES6 and beyond, async/await provides an alternative to handle asynchronous tasks more cleanly. Let me explain Promises in detail and their advantages, and then compare them to async/await.
___
### What Are Promises?

A Promise is an object representing the eventual completion (or failure) of an asynchronous operation. It has three states:
+ Pending: The initial state; the operation is not yet completed.
+ Resolved/Fulfilled: The operation completed successfully.
+ Rejected: The operation failed.

**Syntax:**
```javascript
const myPromise = new Promise((resolve, reject) => {
  // Simulate an asynchronous operation
  setTimeout(() => {
    const success = true;
    if (success) {
      resolve("Operation succeeded!");
    } else {
      reject("Operation failed.");
    }
  }, 1000);
});
```
### How to Use Promises

+ **Handling the Result**

Promises are consumed using .then() for success and .catch() for errors.

```javascript
myPromise
  .then((result) => {
    console.log(result); // "Operation succeeded!"
  })
  .catch((error) => {
    console.error(error); // "Operation failed."
  });
```
+ **Chaining Promises**

You can chain multiple .then() calls to perform sequential operations:

```javascript
myPromise
  .then((result) => {
    console.log(result);
    return "Next operation";
  })
  .then((nextResult) => {
    console.log(nextResult);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

### Advantages of Promises

**1. Better Readability Compared to Callbacks**

Without Promises, asynchronous tasks would be handled using callbacks, leading to “callback hell”:

```javascript
doTask1(() => {
  doTask2(() => {
    doTask3(() => {
      console.log("All tasks completed!");
    });
  });
});
```
**With Promises, the same code looks cleaner:**

```javascript
doTask1()
  .then(doTask2)
  .then(doTask3)
  .then(() => {
    console.log("All tasks completed!");
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```
**2. Error Handling**

Promises centralize error handling using .catch() instead of writing multiple error callbacks:

```javascript
myPromise
  .then(doTask1)
  .then(doTask2)
  .then(doTask3)
  .catch((error) => {
    console.error("Error occurred:", error);
  });
```

**3. Chaining for Sequential Execution**

Promises make it easier to chain asynchronous operations. Each .then() runs after the previous one resolves.

**4. Composing Multiple Promises**

Promises allow concurrent execution of asynchronous tasks with Promise.all() or Promise.race():

```javascript
Promise.all([promise1, promise2, promise3])
  .then((results) => {
    console.log("All tasks completed:", results);
  })
  .catch((error) => {
    console.error("Error in one of the tasks:", error);
  });
```
___
### **Why Use async/await Instead of Promises Directly?**

async/await was introduced in ES2017 (ES8) to make asynchronous code look and behave like synchronous code, improving readability and maintainability.

**How async/await Works**

+ async declares a function that returns a Promise.
+ await pauses execution of the function until the Promise is resolved or rejected.

Example:

```javascript
async function fetchData() {
  try {
    const result = await fetch("https://api.example.com/data");
    const data = await result.json();
    console.log(data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}
```

This code behaves sequentially, which is easier to read and debug compared to .then() chaining.
___
### **Comparison: Promises vs async/await**

**Key Advantages of Promises**

+ **Versatile**: You can compose and chain promises, making them suitable for both sequential and parallel asynchronous tasks.
+ **Universal**: Promises work natively in JavaScript without the need for extra syntax or keywords.
+ **Error Propagatio**n: Errors automatically propagate through .catch().

**Key Advantages of async/await**

+ ****Readability**: The code looks synchronous and is easier to read and debug.
+ **Simplicity**: No need for chaining; everything happens within a try/catch block.
+ **Better Error Handling**: You can use try/catch to handle errors more naturally.
___
### When to Use Each

**Use Promises:**

+ When you need to manage multiple asynchronous operations (e.g., Promise.all() or Promise.race()).
+ When working with older codebases or libraries that return Promises.

**Use async/await:**

+ For sequential asynchronous tasks.
+ When you want your code to be cleaner and easier to understand.
