const express = require('express');
const app = express();
const port = 3000;
const path = require('path');
const Handlebars = require("handlebars");
const fs = require("node:fs");

var index_string; 
try {
  index_string = fs.readFileSync(path.join(__dirname, '', 'index.html'), 'utf8');
} catch (err) {
  console.error(err);
}

app.get('/', (req, res) => {
  console.log("We got something for index");
  const template = Handlebars.compile(index_string);
  const data = {name: "Andrew"};
  res.send(template(data));
});

// Host blog
app.get('/blog', (req, res) => {
  console.log("We got something for blog");
  res.sendFile(path.join(__dirname, '', 'index.html'));
});

// Run website
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});

