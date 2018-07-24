const cors = require('cors');
const express = require('express');
const JSONStream = require('JSONStream');
const bodyParser = require('body-parser');
const app = express();
app.use(cors());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.get('/kotak', function(req, res) {
   return res.json({data: "huy"})
  console.log('lol');
})

app.listen(process.env.PORT || 3000);
console.log('Server is running on Port 3000')
