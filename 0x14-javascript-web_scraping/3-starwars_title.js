#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', bar);

function bar (err, data, body) {
  if (err == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
}
