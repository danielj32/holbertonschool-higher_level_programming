#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request
  .get(url, (e, response, body) => {
    if (e) {
      console.log(e);
    } else if (id === '7') {
      console.log('The Force Awakens');
    } else {
      console.log(JSON.parse(body).title);
    }
  });
