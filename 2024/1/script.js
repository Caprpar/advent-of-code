const fs = require("node:fs");
const path = "advent-of-code/2024/1/data.txt";

fs.readFile(path, "utf8", (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  let rows = [];
  for (let name of data.split("\n")) {
    name = parseInt(name) ? Number(name) : name;
    rows.push(name);
  }

  // Removes last index if content === "" (empty string)
  rows = rows[rows.length - 1] === "" ? rows.slice(0, -1) : rows;
  console.log(rows);
});
