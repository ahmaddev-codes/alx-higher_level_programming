#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  const newList = [];

  for (let i = 0; i < list.length; i++) {
    newList[i] = list[len];
    console.log(newList);
    len--;
  }
  return newList;
};
