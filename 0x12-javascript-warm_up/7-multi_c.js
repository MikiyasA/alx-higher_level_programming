#!/usr/bin/node
const c = 'C is fun';
const len = process.argv[2];
let cnt = 0;
if (len) {
  while (cnt < len) {
    console.log(c);
    cnt++;
  }
} else {
  console.log('Missing number of occurrences');
}
