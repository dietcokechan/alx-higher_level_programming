#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let results = JSON.parse(body).results;
    let count = 0;
    for (let i in results) {
      for (let char in results[i].characters) {
        if (char.search('/18/') > 0) count += 1;
      }
    }
    console.log(count);
  }
});
