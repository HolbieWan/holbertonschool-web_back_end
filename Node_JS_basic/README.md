# Node.js Project

Welcome to your Node.js project! This README contains essential learning objectives and foundational knowledge for junior developers. By the end of this project, you'll have a strong grasp of key Node.js concepts and the ability to build a basic HTTP server and work with Express.js.

---

## Learning Objectives

By completing this project, you will learn to:

1. **Run JavaScript using Node.js**
2. **Use Node.js modules**
3. **Utilize specific Node.js modules to read files**
4. **Use `process` to access command line arguments and the environment**
5. **Create a small HTTP server using Node.js**
6. **Create a small HTTP server using Express.js**
7. **Create advanced routes with Express.js**
8. **Use ES6 with Node.js via Babel-node**
9. **Leverage Nodemon for faster development**

---

## Table of Contents

- [Node.js Project](#nodejs-project)
  - [Learning Objectives](#learning-objectives)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Node.js](#introduction-to-nodejs)
  - [Running JavaScript Using Node.js](#running-javascript-using-nodejs)
  - [Using Node.js Modules](#using-nodejs-modules)
  - [Reading Files with Node.js Modules](#reading-files-with-nodejs-modules)
  - [Accessing Command Line Arguments and Environment Variables](#accessing-command-line-arguments-and-environment-variables)
  - [Creating an HTTP Server](#creating-an-http-server)
  - [Creating an HTTP Server with Express.js](#creating-an-http-server-with-expressjs)
  - [Advanced Routes with Express.js](#advanced-routes-with-expressjs)
  - [Using ES6 with Babel-node](#using-es6-with-babel-node)
  - [Using Nodemon for Faster Development](#using-nodemon-for-faster-development)
  - [Getting Started](#getting-started)
  - [Resources](#resources)

---

## Introduction to Node.js

Node.js is a runtime environment that lets you execute JavaScript outside the browser. It is built on Chrome's V8 JavaScript engine and allows developers to build scalable, server-side applications.

- **Key Features:**
  - Event-driven and non-blocking I/O model.
  - Ideal for data-intensive real-time applications.

---

## Running JavaScript Using Node.js

To execute JavaScript files using Node.js:

1. Install Node.js from the [official website](https://nodejs.org/).
2. Write a JavaScript file (e.g., `app.js`).
3. Run the file using the command:
   ```bash
   node app.js
   ```

Example:
```javascript
console.log('Hello, Node.js!');
```

---

## Using Node.js Modules

Node.js modules are reusable pieces of code. They can be built-in (e.g., `fs`, `http`) or custom.

- **Importing Modules:**
  ```javascript
  const fs = require('fs');
  ```
- **Exporting Custom Modules:**
  ```javascript
  module.exports = function greet() {
    console.log('Hello from a custom module!');
  };
  ```

---

## Reading Files with Node.js Modules

Use the `fs` module to read files:

```javascript
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

---

## Accessing Command Line Arguments and Environment Variables

- **Command Line Arguments:** Use `process.argv`.
  ```javascript
  console.log(process.argv);
  ```
- **Environment Variables:** Access with `process.env`.
  ```javascript
  console.log(process.env.NODE_ENV);
  ```

---

## Creating an HTTP Server

Use the `http` module to create a server:

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, world!');
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

---

## Creating an HTTP Server with Express.js

Express.js is a minimal web framework for Node.js. Install it with:
```bash
npm install express
```

Example:
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello, Express.js!');
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
```

---

## Advanced Routes with Express.js

Define dynamic and nested routes:

```javascript
app.get('/user/:id', (req, res) => {
  res.send(`User ID: ${req.params.id}`);
});

app.get('/products/:category/:id', (req, res) => {
  res.send(`Category: ${req.params.category}, Product ID: ${req.params.id}`);
});
```

---

## Using ES6 with Babel-node

Babel allows you to use modern JavaScript features. Install Babel:
```bash
npm install @babel/core @babel/node @babel/preset-env
```

Add a `.babelrc` file:
```json
{
  "presets": ["@babel/preset-env"]
}
```
Run your code with:
```bash
npx babel-node app.js
```

---

## Using Nodemon for Faster Development

Nodemon automatically restarts the server when you make changes. Install it globally:
```bash
npm install -g nodemon
```

Run your application with:
```bash
nodemon app.js
```

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the application:
   ```bash
   nodemon app.js
   ```

---

## Resources

- [Node.js Documentation](https://nodejs.org/en/docs/)
- [Express.js Documentation](https://expressjs.com/)
- [Babel Documentation](https://babeljs.io/)
- [Nodemon Documentation](https://nodemon.io/)

Happy coding!
