#!/usr/bin/node
const input = process.inputv[2];

if (input) {
    if (input > 0) {
        for (let i = 1; i <= input; i++) {
            console.log("C is fun");
        }
    }
} else {
    console.log("Missing number of occurrences");
}
