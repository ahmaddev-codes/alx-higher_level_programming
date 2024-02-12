#!/usr/bin/node
const argArray = process.argv;
const newArray = argArray.slice(2);

if (process.argv[3]) {
    sorted_array = newArray.sort();
    sorted_array.pop();
    second_biggest = sorted_array.pop();
    console.log(second_biggest);
} else {
    console.log(0)
}