#!/usr/bin/node
/* a script that reads and prints the content of a file. */

const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
