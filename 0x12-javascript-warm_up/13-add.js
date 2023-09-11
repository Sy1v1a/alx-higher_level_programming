#!/usr/bin/node

global.add = function (a, b) {
  if (typeof a === 'number' && typeof b === 'number') {
    return a + b;
  } else {
    throw new Error('Both arguments must be integers.');
  }
};

module.exports = { add };
