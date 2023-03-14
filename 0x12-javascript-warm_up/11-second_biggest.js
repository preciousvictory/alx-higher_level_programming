#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  args.splice(0, 2);
  args.sort((x, y) => x - y).reverse();
  console.log(args[1]);
}
