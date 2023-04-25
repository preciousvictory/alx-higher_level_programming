#!/usr/bin/node
/*  a script that computes the number of tasks completed by user id. */

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
