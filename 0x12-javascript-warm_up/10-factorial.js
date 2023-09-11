#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

if (process.argv.length !== 3) {
  console.log(1);
} else {
  const inputNumber = parseInt(process.argv[2]);
  const result = factorial(inputNumber);
  console.log(result);
}
