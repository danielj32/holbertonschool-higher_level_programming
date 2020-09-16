#!/usr/bin/node
const myVar = process.argv[2];

if (myVar === undefined || isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  let ct = 0;
  while (ct < myVar) {
    console.log('C is fun');
    ct++;
  }
}
