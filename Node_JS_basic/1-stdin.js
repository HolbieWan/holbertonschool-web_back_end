// Program to read user input from stdin and display a message

// Display welcome message
console.log('Welcome to Holberton School, what is your name?');

// Event listener for input
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
  process.exit();
});

// Event listener for program exit
process.on('exit', () => {
  console.log('This important software is now closing');
});
