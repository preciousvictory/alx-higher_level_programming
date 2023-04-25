#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie: */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).characters;
    for (const c in results) {
      const url_ = results[c];

      request(url_, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const result = JSON.parse(body).name;
          console.log(result);
        }
      });
    }
  }
});
