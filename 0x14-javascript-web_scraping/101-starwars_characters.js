#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).characters;
    const promises = [];
    for (const i of results) {
      promises.push(new Promise((resolve, reject) => {
        request(i, (e, r, b) => resolve(JSON.parse(b).name));
      }));
    }
    Promise.all(promises).then((p) => {
      for (const i of p) { console.log(i); }
    });
  }
});
