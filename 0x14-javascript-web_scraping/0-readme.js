#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', bar);

function bar (err, data) {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data);
  }
}
