#!/usr/bin/node
var index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`)
  index++;
}