// 3-read_file_async.js
// Function to count students in a CSV file asynchronously

const fs = require('fs');
const path = require('path');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    // Ensure the provided path is absolute for consistency
    const absolutePath = path.resolve(filePath);

    fs.readFile(absolutePath, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        // Split file content into lines, skipping empty lines
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        if (lines.length === 0) {
          console.log('File is empty');
          resolve();
          return;
        }

        // Extract and discard the header line
        const headers = lines.shift();

        // Parse student data
        const students = lines.map((line) => line.split(','));
        console.log(`Number of students: ${students.length}`);

        // Process each student and print their details
        students.forEach((student) => {
          const [firstname, , , field] = student;
          console.log(`Student: ${firstname}, Field: ${field}`);
        });

        resolve(); // Successfully completed
      } catch (parseError) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
