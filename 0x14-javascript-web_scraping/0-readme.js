#!/usr/bin/node

let fs = require('fs');
let file = process.argv[2];
fs.readFile(file, 'utf8', (err, data = err) => {
    if (err) {
        throw err;
    } else {
        console.log(data);
    }
});
