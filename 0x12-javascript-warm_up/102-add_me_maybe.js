#!/usr/bin/bash

function addMeMaybe (number, theFunction) {
  number ++;
  theFunction(number);
}

module.exports = { addMeMaybe };
