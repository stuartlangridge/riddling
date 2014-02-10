#!/usr/bin/node
var unhashed = require("./riddles-unhashed"),
    utils = require("../www/utils.js"),
    fs = require("fs");

var hashed = [];
unhashed.riddles.forEach(function(r) {
    if (r.clue) {
        hashed.push({
            clue: r.clue,
            answer: utils.checksum(r.answer),
            explanation: utils.encrypt(r.answer, r.explanation)
        });
    } else {
        hashed.push(r);
    }
});
fs.writeFile("../www/riddles.js",
    "var riddles = " + JSON.stringify(hashed, undefined, 2) +
    ";\nvar universal=" + utils.checksum(unhashed.universal) + ";", function(err) {
    console.log("Written as requested.");
});
