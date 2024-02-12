#!/usr/bin/node
const size = process.argv[2];
if (size) {
    if (!isNaN(size) && size > 0) {
        for (let i = 1; i <= size; i++) {
            let row = "";
            for (let j = 1; j <= size; j++) {
                row += "X";
            }
            console.log(row);
        }
    } else if (isNaN(size)) {
        console.log("Missing size");
    }
} else {
    console.log("Missing size");
}