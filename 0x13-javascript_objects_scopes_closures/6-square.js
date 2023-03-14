#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super();
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    let char_ = 'X';
    if (c) {
      char_ = c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(char_.repeat(this.width));
    }
  }
}

module.exports = Square;
