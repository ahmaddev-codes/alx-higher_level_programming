#!/usr/bin/node

if (process.argv[2]) {
  const inputNumber = parseInt(process.argv[2]);

  if (!isNaN(inputNumber) && Number.isInteger(inputNumber)) {
    console.log(`My number: ${Math.floor(inputNumber)}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
