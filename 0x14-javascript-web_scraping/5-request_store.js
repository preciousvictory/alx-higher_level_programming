#!/usr/bin/node
/* a script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const filename = process.argv[3];
    const fs = require('fs');

    fs.writeFile(filename, body,
      {
        encoding: 'utf8',
        flag: 'w'
      },
      (err) => {
        if (err) { console.log(err); }
      });
  }
});
