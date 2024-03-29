#!/usr/bin/node
// A Script that prints msgs based on the number of argument passed to it
function checkArg(arg) {
    if (process.argv.length <= 2) {
        console.log("No argument");
    } else if (process.argv.length === 3) {
        console.log("Argument found");
    } else {
        console.log("Arguments found");
    }
}
//  Call the function
checkArg()