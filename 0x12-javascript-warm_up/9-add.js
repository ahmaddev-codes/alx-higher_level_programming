#!/usr/bin/node
const value1 = parseInt(process.argv[2]);
const value2 = parseInt(process.argv[3]);

function add(a, b) {
    const sum = a + b;
    return sum;
}

if (value1 && value2) {
    console.log(add(value1, value2));
} else {
    console.log("NaN")
}
