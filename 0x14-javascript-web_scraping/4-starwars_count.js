#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      for (const char of results[i].characters) {
        if (char.search('/18/') > 0) { count += 1; }
      }
    }
    console.log(count);
  }
});
