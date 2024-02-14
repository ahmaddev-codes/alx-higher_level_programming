#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.shape = 'C';
    this.print();
  }
}

module.exports = Square;
