const express = require('express')
let {PythonShell} = require('python-shell')

const app = express()
const port = 3000



let pyshell = new PythonShell('chess.py');
let pyshell2 = new PythonShell('xiangqi.py');


//***this section of the code is responsible for running the python script ***
pyshell.on('message', function (message) {  
  
  console.log(message);
});
pyshell2.on('message', function (message) {  
  console.log(message);
});


// end the input stream and allow the process to exit
pyshell.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
  console.log('finished');
});
pyshell2.end(function (err,code,signal) {
  if (err) throw err;
  console.log('The exit code was: ' + code);
  console.log('The exit signal was: ' + signal);
  console.log('finished');
  console.log('finished');
});



app.get('/', (req,res) => {
  res.send("This app is running!")
});

app.listen(port, () => console.log(`App listening on port ${port}!`))

