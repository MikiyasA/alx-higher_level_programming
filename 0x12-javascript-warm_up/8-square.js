#!/usr/bin/node
const s = process.argv[2];
let c = 0;
if (s) {
  while (c < s) {
    let x = '';
    for (let i = 0; i < s; i++) {
      x += 'X';
    }
    console.log(x);
    c++;
  }
} else {
  console.log('Missing size');
}
