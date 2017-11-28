var socket = new WebSocket('ws://kicker.local:15674');

// Connection opened
socket.addEventListener('open', function (event) {
    //socket.send('Hello Server!');
    console.log("opened!");
});

// Listen for messages
socket.addEventListener('message', function (message) {
    window.rstate.states = JSON.parse(message.data);
});

$(document).on('click', '#score_resetter_button', function(e) {
  socket.send('{ "event": "reset" }');
});


/*
var client = Stomp.over(ws);

var on_connect = function() {
    console.log("HERE");
    var sub = client.subscribe('/exchange/kicker', function(message) {
        console.log("WebWorker: " + message.body);
        window.bstate.states = JSON.parse(message.body).payload;
    });
};
var on_error =  function() {
    console.log('error');
};
client.connect(null, null, on_connect, on_error, '/');
*/