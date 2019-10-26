/*
Design the PostNatural
Author: Morgan Mueller
Date: October 20th, 2019
*/
//four line server example created by Tom Igoe
var express = require('express');
var server = express();
server.use('/',express.static('public'));

server.get('/23047-077', inmateOne);
server.get('/24463-001', inmateTwo)

server.listen(8080);


function inmateOne(request, response) {
  response.status(200).sendFile(__dirname + '/index2.html');
  response.setHeader("Set-Cookie", "HttpOnly;Secure;SameSite=Strict");
  response.end;

}

function inmateTwo(request, response) {
  response.status(200).sendFile(__dirname + '/index.html');
  response.setHeader("Set-Cookie", "HttpOnly;Secure;SameSite=Strict");
  response.end;

}


}
