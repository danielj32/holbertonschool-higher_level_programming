#!/usr/bin/node
const squareFive = require('./5-square.js');

class Square extends squareFive {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let ct;
    for (ct = 0; ct < this.height; ct++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
