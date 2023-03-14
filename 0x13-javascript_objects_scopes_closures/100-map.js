#!/usr/bin/node
const list = require('./100-data').list;
const new_list = [];
for (let i = 0; i < list.length; i++) {
  new_list.push(list[i] * i);
}
console.log(list);
console.log(new_list);
