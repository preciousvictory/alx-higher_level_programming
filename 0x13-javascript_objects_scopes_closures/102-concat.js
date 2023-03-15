#!/usr/bin/node
let args = process.argv
const fs = require('fs');

if (args.length != 5) {
  console.log('Missing Argument');
  return;
}
fileA = process.argv[2];
fileB = process.argv[3];
fileC = process.argv[4];

const data1 = fs.readFileSync(fileA, {encoding:'utf8', flag:'r'});
const data2 = fs.readFileSync(fileB, {encoding:'utf8', flag:'r'});

data = '' + data1 + data2;
fs.writeFile(fileC, data, (err) => {
  if (err) throw err;
})
