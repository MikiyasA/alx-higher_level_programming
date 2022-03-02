#!/usr/bin/node
const fs = require('fs');
const fl1 = fs.readFileSync(process.argv[2]).toString();
const fl2 = fs.readFileSync(process.argv[3]).toString()
fs.writeFileSync(process.argv[4], fl1 + fl2)
