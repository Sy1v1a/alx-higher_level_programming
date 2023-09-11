#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const integers = process.argv.slice(2).map(arg => parseInt(arg));
  integers.sort((a, b) => b - a);
  const secondBiggest = integers[1];
  console.log(secondBiggest);
}
