# ES6_Promises
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

+ Promises (how, why, and what)
+ How to use the then, resolve, catch methods
+ How to use every method of the Promise object
+ Throw / Try
+ The await operator
+ How to use an async function

Here’s a brief explanation of each concept:

### 1. Promises

+ What: 
	+ Promises are objects in JavaScript that represent the eventual result (or failure) of an asynchronous operation.
+ Why: 
	+ They help avoid “callback hell” and make asynchronous code easier to read.
+ How: 
	+ Create a promise with new Promise((resolve, reject) => { ... }). Use resolve for success and reject for failure.
```javascript
function getResponseFromAPI() {
return new Promise((resolve, reject) => {});
}
```
___
### 2. Resolve and Reject

+ What: 
	+ resolve and reject are functions provided when creating a promise.
+ Why: 
	+ They define the outcome of the promise.
+ How: 
	+ Use resolve(value) for successful operations and reject(error) for failures.

```javascript
function getFullResponseFromAPI(success) {
    return new Promise((resolve, reject) => {
        if (success) resolve({ status: 200, body: 'Success' });
        else reject(new Error('The fake API is not working currently'));
    });
}
```
___
### 3. .then, .catch, .finally

+ What: 
	+ Methods to handle promise outcomes.
	+ then:Runs when the promise is resolved.
	+ catch: Runs when the promise is rejected.
	+ finally: Always runs after resolution/rejection, regardless of success.
+ Why: 
	+ To separate success, error, and cleanup logic for better readability.
+ How:
	+  Chain them after a promise: promise.then().catch().finally().

```javascript
function handleResponseFromAPI(promise) {
    return promise
        .then(() => ({ status: 200, body: 'success' }))
        .catch(() => new Error())
        .finally(() => console.log('Got a response from the API'));
}
```
___
### 4. Promise.all

+ What: 
	+ Combines multiple promises and resolves when all promises are resolved or rejects if any promise fails.
+ Why: 
	+ To wait for multiple asynchronous operations to finish together.
+ How: 
	+ Use Promise.all([promise1, promise2]) to combine.

```javascript
import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
        .then(([photo, user]) => console.log(`${photo.body} ${user.firstName} ${user.lastName}`))
        .catch(() => console.log('Signup system offline'));
}
```
___
### 5. Promise.resolve

+ What: 
	+ Quickly creates a promise that resolves immediately.
+ Why: 
	+ For simple, predefined asynchronous operations.
+ How: 
	+ Use Promise.resolve(value) to create it.

```javascript
function signUpUser(firstName, lastName) {
    return Promise.resolve({ firstName, lastName });
}
```
___
### 6. Promise.reject

+ What: 
	+ Quickly creates a promise that rejects immediately with an error.
+ Why: 
	+ For predefined error scenarios.
+ How: 
	+ Use Promise.reject(new Error(message)).

```javascript
function uploadPhoto(fileName) {
    return Promise.reject(new Error(`${fileName} cannot be processed`));
}
```
___
### 7. Promise.allSettled

+ What: 
	+ Resolves when all promises finish, regardless of whether they succeed or fail. Provides an array of results with their status (fulfilled or rejected).
+ Why: 
	+ To gather outcomes of multiple promises without stopping for failures.
+ How: 
	+ Use Promise.allSettled([promise1, promise2]).

```javascript
function handleProfileSignup(firstName, lastName, fileName) {
    const signUp = signUpUser(firstName, lastName);
    const upload = uploadPhoto(fileName);

    return Promise.allSettled([signUp, upload]).then(results => results.map(r => ({
        status: r.status,
        value: r.reason || r.value,
    })));
}
```
___
### 8. Promise.race

+ What: 
	+ Resolves or rejects with the first promise to settle.
+ Why: 
	+ To determine the fastest promise to complete.
+ How: 
	+ Use Promise.race([promise1, promise2]).

```javascript
function loadBalancer(chinaDownload, USDownload) {
    return Promise.race([chinaDownload, USDownload]);
}
```
___
### 9. Throwing Errors

+ What: 
	+ Manually create an error in your code.
+ Why: 
	+ To signal that something went wrong during execution.
+ How: 
	+ Use throw new Error('message').

```javascript
function divideFunction(numerator, denominator) {
    if (denominator === 0) throw new Error('cannot divide by 0');
    return numerator / denominator;
}
```
___
### 10. try / catch

+ What: 
	+ A block of code to handle exceptions (errors).
+ Why: 
	+ Prevent your program from crashing when an error occurs.
+ How: 
	+ Wrap code in try { ... } catch (error) { ... } to catch errors.

```javascript
function guardrail(mathFunction) {
    const queue = [];
    try {
        queue.push(mathFunction());
    } catch (error) {
        queue.push(error.toString());
    } finally {
        queue.push('Guardrail was processed');
    }
    return queue;
}
```