#!/usr/bin/node
const s = process.argv.slice(2).sort(function (a, b) {
  return b - a;
})[1];
if (s) {
  console.log(s);
} else {
  console.log(0);
}
