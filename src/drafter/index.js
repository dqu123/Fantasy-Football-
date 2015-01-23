var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var login = require('./login.js');

connection.connect();

var players;

connection.query('SELECT name FROM players', function(err, rows, fields) {
    if (err) throw err;
    players = rows;
    console.log('Players ', players);
});

connection.end();

app.get('/', function(req, res) { 
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
    socket.on('pick', function(current_pick){
        io.emit('pick', current_pick + ' drafted!');
        for (var i = 0; i < players.length; i++) { 
            if (players[i].name == current_pick) {
                players.splice(i, i + 1);
            }
        }
        io.emit('players updated', players);
        console.log(players[1]);
    });
    io.emit('players updated', players);
});

http.listen(3000, function() { 
    console.log('listening on *:3000'); 
});
