#!/usr/bin/node
const value = parseInt(process.argv[2]);
let sum = 1;

function factorial (n) {
  if (n !== 1 && n !== 0) {
    sum *= n;
    factorial(n - 1);
  }
  return sum;
}

if (value) {
  console.log(factorial(value));
} else if (isNaN(value)) {
  console.log(1);
}
