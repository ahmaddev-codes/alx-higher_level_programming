#!/usr/bin/node

const fs = require('fs');

// store files in variables
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

function readFile (file) {
  try {
    // Using fs.readFileSync for synchronous reading
    const content = fs.readFileSync(file, 'utf8');
    console.log(`File '${file}' read successfully`);
    return content;
  } catch (error) {
    console.error(`Error reading file '${file}':`, error.message);
    process.exit(1); // Exit with an error code
  }
}

function writeFile (fileA, fileB, fileC) {
  const fileAContent = readFile(fileA);
  const fileBContent = readFile(fileB);
  const content = `${fileAContent}\n${fileBContent}`;

  try {
    // Using fs.writeFileSync for synchronous writing
    fs.writeFileSync(fileC, content);
    console.log(`Content written to '${fileC}' successfully`);
  } catch (error) {
    console.error(`Error writing to file '${fileC}':`, error.message);
    process.exit(1); // Exit with an error code
  }
}

writeFile(fileA, fileB, fileC);
