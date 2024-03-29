#!/usr/bin/node
// A Script that prints msgs based on the number of argument passed to it
function checkArg(arg) {
    if (process.argv.length > 2) {
        console.log("Arguments found");
    } else {
        console.log("No argument");
    }
}
//  Call the function
checkArg()