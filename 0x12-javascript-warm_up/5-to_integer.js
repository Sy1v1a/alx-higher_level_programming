#!/usr/bin/node

const args = process.argv.slice(2);
const firstArg = args[0];

const intValue = parseInt(firstArg);

if (!isNaN(intValue)) {
  console.log(`My number: ${intValue}`);
} else {
  console.log("Not a number");
}
