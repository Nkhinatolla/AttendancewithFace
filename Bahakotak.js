const cors = require('cors');
const express = require('express');
const JSONStream = require('JSONStream');
const bodyParser = require('body-parser');
const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.get('/kotak', function(req, res) {
  res.body('text')
})
