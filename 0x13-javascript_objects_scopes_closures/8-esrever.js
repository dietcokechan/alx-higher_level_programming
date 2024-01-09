#!/usr/bin/node
exports.esrever = function (list) {
    return list.map((item, i) => list[list.length - 1 - i]);
};
