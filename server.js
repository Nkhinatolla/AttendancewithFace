const cors = require('cors');
const express = require('express');
const JSONStream = require('JSONStream');
const bodyParser = require('body-parser');
const app = express();
const axios = require ('axios');
app.use(cors());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.post('/kotak', function(req, res) {
  var parent = "A1"
  var from = 0
  axios.get("http://post.city.kz/objects/{parent}?from={from}")
  .then(response => {
    console.log(response.data)
  })
  .catch(error => {
    console.log(error);
  });
   return res.json(response.data)
  console.log('lol');
})

app.listen(process.env.PORT || 3000);
console.log('Server is running on Port 3000')
