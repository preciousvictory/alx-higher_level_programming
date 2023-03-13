#!/usr/bin/node
let arguments = process.argv;

if (arguments.length > 3)
{
	console.log('Arguments found');
}
else if (arguments.length === 3)
{
	console.log('Argument found');
}
else
{
	console.log('No argument');
}
