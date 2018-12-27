const cors = require('cors');
const express = require('express');
const JSONStream = require('JSONStream');
const bodyParser = require('body-parser');
const app = express();
const axios = require ('axios');
app.use(cors());
app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.post('/v1', function(req, res) {
  var spawn = require("child_process").spawn;
  console.log(req.body)
  var process = spawn('python',["./test.py", req.body.name] );
  console.log("Running test.py... ")
  process.stdout.on('data', function(data) {
      console.log(data.toString())
      res.send(data.toString());
  })
  // axios.get("https://post.kz/mail-app/info/calculate.json")
  // .then(response => {
  // })
  // .catch(error => {
  //   console.log(error);
  // })
})

app.listen(process.env.PORT || 3000);
console.log('Server is running on Port 3000')
