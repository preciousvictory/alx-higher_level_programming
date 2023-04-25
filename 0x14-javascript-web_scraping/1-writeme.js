#!/usr/bin/node
/* a script that writes a string to a file. */

const filename = process.argv[2];
const fs = require('fs');

fs.writeFile(filename, process.argv[3],
  {
    encoding: 'utf8',
    flag: 'w'
  }
  ,
  (err) => {
    if (err) { console.log(err); }
  }
);
