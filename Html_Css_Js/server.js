//var http = require('http');
const fs = require('fs');
const content = fs.readFileSync('character/Megumin.jpg');
const express = require('express');
const server = express();

server.get('/', (req, res) => {
  res.send(`
  <!DOCTYPE html>
  <html lang="pt-br">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>jogo das cartas</title>
  </head>
  <body>
      <div>
        <img src="./character/Megumin.jpg" alt="Megumin">
        
      </div>
  </body>
  </html>
  
  `);
})

server.get('/card', (req,res) => {
  res.send(content);
})

server.listen(3001, () => {
  console.log('Servidor em pé em http://localhost:3001');
  console.log('Derruba com Ctrl + C');
})

/*http.createServer(function(req, res){
  res.end(content);
}).listen(3001);*/

