#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request(process.argv[2], bar);

function bar (err, resp, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
}
