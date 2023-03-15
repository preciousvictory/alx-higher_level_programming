#!/usr/bin/node
const dict = require('./101-data').dict;
let occur = Object.values(dict);
occur = occur.filter((item, index) => occur.indexOf(item) === index);

function getvalue (k) {
  const val = [];
  for (const [key, value] of Object.entries(dict)) {
    if (value === k) {
      val.push(key);
    }
  }
  return val;
}

const newDict = {};
for (let i = 0; i < occur.length; i++) {
  newDict[occur[i]] = getvalue(i + 1);
}
console.log(newDict);
