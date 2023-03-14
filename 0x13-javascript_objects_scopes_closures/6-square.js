#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

class Square extends Rectangle {
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

module.exports = Rectangle;
module.exports = Square;
