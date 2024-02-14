#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let shape = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shape += 'X';
      }

      if (i < this.height - 1) {
        shape += '\n';
      }
    }
    console.log(shape);
  }
}

module.exports = Rectangle;
