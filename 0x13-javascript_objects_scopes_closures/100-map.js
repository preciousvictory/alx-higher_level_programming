#!/usr/bin/node
const list = require('./100-data').list;
let i = 0;
const new_list = list.map(x => x * (i++));

console.log(list);
console.log(new_list);
