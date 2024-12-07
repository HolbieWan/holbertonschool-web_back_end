# ES6 - Data Manipulations: 

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

+ How to use map, filter and reduce on arrays
+ Typed arrays
+ The Set, Map, and Weak link data structures
___

### 0. Arrays of Objects

+ What: 
    + Arrays of objects are used to store related data in a structured way, where each object contains key-value pairs.
+ Why: 
    + They make it easy to organize and access complex data, such as lists of students or products.
+ How:
    + Create an array with objects inside.
    + Access specific properties using dot notation or destructuring.
+ Example:
```javascript
const students = [
    { id: 1, name: 'Alice', city: 'Paris' },
    { id: 2, name: 'Bob', city: 'London' },
];
console.log(students[0].name); // 'Alice'
```
___
### 1. Mapping Data

+ What: 
    + The map() method creates a new array by applying a function to every element of an existing array.
+ Why: 
    + It’s useful for transforming data, like extracting specific fields or modifying the values.
+ How:
    + Call map() on an array and pass a callback function that defines how each element should be transformed.
+ Example:
```javascript
const numbers = [1, 2, 3];
const squares = numbers.map(num => num * num); // [1, 4, 9]
console.log(squares);
```
___
### 2. Filtering Data

+ What: 
    +The filter() method creates a new array containing only elements that meet a certain condition.
+ Why: 
    + It helps narrow down data to only what’s relevant, like filtering students by city or products by price range.
+ How: 
    + Call filter() on an array and pass a callback function that returns true for elements to keep.
+ Example:
```javascript
const people = [
    { name: 'Alice', age: 25 },
    { name: 'Bob', age: 17 },
];
const adults = people.filter(person => person.age >= 18); // [{ name: 'Alice', age: 25 }]
console.log(adults);
```
___
### 3. Reducing Data

+ What: 
    + The reduce() method processes an array and returns a single accumulated result, such as a sum, product, or concatenated string.
+ Why: 
    + It’s used to compute values like totals or aggregated data.
+ How: 
    + Call reduce() with a callback that takes an accumulator and the current element.
	+ Optionally provide an initial value for the accumulator.
+ Example:
```javascript
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, num) => total + num, 0); // 10
console.log(sum);
```
___
### 4. Combining Map and Filter

+ What: 
    + You can combine filter() and map() to first narrow down data and then transform it.
+ Why: 
    + This is powerful for workflows where you need to select specific items and apply changes.
+ How: 
    + Use filter() to get only the desired elements.
	+ Chain map() to process the filtered data.
+ Example:
```javascript
const products = [
    { name: 'Shirt', price: 20 },
    { name: 'Hat', price: 15 },
    { name: 'Shoes', price: 50 },
];
const discounted = products
    .filter(product => product.price > 20)
    .map(product => ({ ...product, price: product.price * 0.9 }));
console.log(discounted); // [{ name: 'Shoes', price: 45 }]
```
___
### 5. Typed Arrays

+ What: 
    + Typed arrays (Int8Array, Uint8Array, etc.) provide a way to handle raw binary data efficiently.
+ Why: 
    + They’re used in applications like image processing, video editing, or WebGL for handling structured data buffers.
+ How:
	+ Create a buffer using ArrayBuffer.
	+ Use a DataView or specific typed array (like Int8Array) to manipulate the data.
+ Example:
```javascript
const buffer = new ArrayBuffer(8); // 8 bytes
const int8View = new Int8Array(buffer);
int8View[0] = 42; // Assign value at index 0
console.log(int8View[0]); // 42
```
___
### 6. Set Data Structure

+ What: 
    + A Set is a collection of unique values.
+ Why: 
    + It’s ideal for removing duplicates or checking membership efficiently.
+ How: 
    * Use the Set constructor to create a set. 
    * Use methods like add(), has(), and delete() to manipulate it.
	+ Example:
```javascript
const numbers = new Set([1, 2, 2, 3]);
console.log(numbers); // Set { 1, 2, 3 }
console.log(numbers.has(2)); // true
```
___
### 7. Checking Membership with Sets

+ What: 
    + The every() method checks if all elements in an array satisfy a condition, like existing in a Set.
+ Why: 
    + Useful for validating if a group of items are all allowed or present.
+ How: 
    + Combine Set.has() with Array.every().
+ Example:
```javascript
const set = new Set([1, 2, 3]);
const array = [1, 3];
const allPresent = array.every(value => set.has(value)); // true
console.log(allPresent);
```
___
### 8. Extracting from Sets

+ What: 
    + You can extract and manipulate values in a Set based on conditions.
+ Why: 
    + Useful for formatting data stored in a Set.
+ How:
    + Use forEach() or the spread operator to iterate over a Set.
    + Use string manipulation methods to transform values.
+ Example:
```javascript
const set = new Set(['apple', 'apricot', 'banana']);
const result = [...set].filter(word => word.startsWith('a')).join('-');
console.log(result); // 'apple-apricot'
```
___
### 9. Map Data Structure

+ What: 
    + A Map stores key-value pairs and remembers the insertion order.
+ Why: 
    + It’s more flexible than objects because keys can be of any type.
+ How:
    + Use the Map constructor and methods like set(), get(), and delete().
+ Example:
```javascript
const groceries = new Map();
groceries.set('Apples', 10);
groceries.set('Bananas', 5);
console.log(groceries.get('Apples')); // 10
```
___
### 10. Updating Map Values

+ What: 
    + You can iterate over a Map to update values based on conditions.
+ Why: 
    + This allows for dynamic updates while preserving the structure.
+ How:
    + Use forEach() or a for...of loop to check and modify values.
+ Example:
```javascript
const items = new Map([
    ['Shirt', 1],
    ['Hat', 10],
    ['Shoes', 1],
]);
items.forEach((value, key) => {
    if (value === 1) items.set(key, 100);
});
console.log(items);
```