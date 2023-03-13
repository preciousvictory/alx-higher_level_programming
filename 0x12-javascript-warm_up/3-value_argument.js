#!/usr/bin/node
let arguments = process.argv;

if (arguments.length >= 3)
{
	console.log(arguments[2]);
}
else
{
	console.log('No arguments');
}
