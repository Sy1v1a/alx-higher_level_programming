#!/usr/bin/node

function add (a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    console.log('Please provide valid integers as arguments.');
    return;
  }

  const sum = a + b;

  console.log(`The sum of ${a} and ${b} is: ${sum}`);
}

if (process.argv.length !== 4) {
  console.log('NaN');
} else {
  const integer1 = parseInt(process.argv[2]);
  const integer2 = parseInt(process.argv[3]);
  add(integer1, integer2);
}
