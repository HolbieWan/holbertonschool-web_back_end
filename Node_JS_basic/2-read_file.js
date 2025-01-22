// 2-read_file.js
// Function to count students in a CSV file

const fs = require('fs');

function countStudents(filePath) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(filePath, 'utf8');

    // Split file content into lines and filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length === 0) {
      throw new Error('File is empty');
    }

    // Extract header and data
    const headers = lines.shift(); // Remove and store the header line
    const students = lines.map((line) => line.split(','));

    console.log(`Number of students: ${students.length}`);

    // Count students by field
    const fieldGroups = {};
    students.forEach((student) => {
      const [firstname, lastname, age, field] = student;

      if (!field) return; // Skip invalid lines without a field

      if (!fieldGroups[field]) {
        fieldGroups[field] = [];
      }
      fieldGroups[field].push(firstname);
    });

    // Print the results
    for (const [field, names] of Object.entries(fieldGroups)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(
          ', ',
        )}`,
      );
    }
  } catch (error) {
    // Handle file read errors
    throw new Error('Cannot load the database');
  }
}

// Export the function
module.exports = countStudents;
