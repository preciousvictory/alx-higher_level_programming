#!/usr/bin/node
const args = process.argv;
if (args.length === 3) {
  console.log('0');
} else if (args.length > 3) {
  args.splice(0, 2);
  args.sort().reverse();
  console.log(args[1]);
} else {
  console.log('0');
}
