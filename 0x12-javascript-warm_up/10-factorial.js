#!/usr/bin/node
const firstVar = process.argv[2];

function myFactorial (ct) {
  if (ct < 0) {
    return (-1);
  } else if (ct === 0 || isNaN(ct)) {
    return (1);
  } else {
    return (ct * myFactorial(ct - 1));
  }
}
console.log(myFactorial(parseInt(firstVar)));
