#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let results = {};
    for (const todo of JSON.parse(body)) {
      if (todo.completed) {
        if (results[todo.userid] === undefined) {
          results[todo.userid] = 0;
        }
        results[todo.userid] += 1;
      }
    }
    console.log(results);
  }
});
