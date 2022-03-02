#!/usr/bin/node

const arg1 = Number(process.argv[2]);
function fact (a) {
  if (!arg1) {
    return 1;
  } else if (a < 0) {
    return -1;
  } else if (a === 0) {
    return 1;
  } else {
    return (a * fact(a - 1));
  }
}
console.log(fact(arg1));
