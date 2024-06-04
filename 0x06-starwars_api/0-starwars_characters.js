#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } else {
    console.error(error);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) return;
  
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    } else {
      console.error(error);
    }
  });
}
