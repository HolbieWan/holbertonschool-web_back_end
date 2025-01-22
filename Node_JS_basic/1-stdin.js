const readline = require('readline');

function wellcome() {
  const readinput = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  readinput.question( "Welcome to Holberton School, what is your name? ",
    (name) => {
      console.log("Your name is: " + name);
      readinput.close();
    });
  readinput.on('close', () => {
    console.log("This important software is now closing");
    process.exit(0);
  });
}
    
wellcome();
module.exports = wellcome;
