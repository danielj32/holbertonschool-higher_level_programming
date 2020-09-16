#!/usr/bin/node
const first_var = parseInt(process.argv[2]);
const second_var = parseInt(process.argv[3]);
function add(a, b) {
  const result = first_var + second_var;
  console.log(result);
}
add(first_var, second_var);
