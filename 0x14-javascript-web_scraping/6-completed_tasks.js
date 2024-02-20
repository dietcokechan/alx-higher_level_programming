#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = {};
    for (const todo of JSON.parse(body)) {
      if (todo.completed) {
        if (results[todo.userId] === undefined) {
          results[todo.userId] = 0;
        }
        results[todo.userId] += 1;
      }
    }
    console.log(results);
  }
});
