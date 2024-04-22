#!/usr/bin/node

let array = process.argv;

if (array.length == 3) {
  console.log('Argument found');
} else if (array.length > 3) {
  console.log('Arguments found')
} else {
  console.log('No argument');
}
