#!/usr/bin/node

const fs = require('fs');

// store files in variables
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

function readFile (file) {
  // Using fs.readFileSync for synchronous reading
  const content = fs.readFileSync(file, 'utf8');
  return content;
}

function writeFile (fileA, fileB, fileC) {
  const fileAContent = readFile(fileA);
  const fileBContent = readFile(fileB);
  const content = `${fileAContent}\n${fileBContent}`;

  // Using fs.writeFileSync for synchronous writing
  fs.writeFileSync(fileC, content);
}

writeFile(fileA, fileB, fileC);
