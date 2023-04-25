#!/usr/bin/node
/* a script that prints the number of movies where the character “Wedge Antilles” is present. */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const result = JSON.parse(body).results;
    let count = 0;

    for (const c in result) {
      const chars = result[c].characters;

      for (const x in chars) {
        if (chars[x].includes('18') === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
