#!/usr/bin/node
const list = require('./100-data.js').list;
const m = list.map(function (n, i) {
  return n * i;
});
console.log(list);
console.log(m);
