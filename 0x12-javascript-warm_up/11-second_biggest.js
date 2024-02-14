#!/usr/bin/node
const argArray = process.argv;
const newArray = argArray.slice(2);

if (process.argv[3]) {
  const sortedAray = newArray.sort();
  sortedAray.pop();
  const secondBiggest = sortedAray.pop();
  console.log(secondBiggest);
} else {
  console.log(0);
}
