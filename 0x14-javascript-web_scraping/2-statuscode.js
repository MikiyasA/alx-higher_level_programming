#!/usr/bin/node
const request = require('request');

request(process.argv[2], bar);

function bar (err, data) {
  if (err == null) {
    console.log('code: ' + data.statusCode);
  }
}
