var ws = new WebSocket('ws://kicker.local:15674/ws');
var client = Stomp.over(ws);

var on_connect = function() {
    var sub = client.subscribe('/exchange/kicker', function(message) {
        console.log("WebWorker: " + message.body);
        window.bstate.states = JSON.parse(message.body).payload;
    });
};
var on_error =  function() {
    console.log('error');
};
client.connect('pi', 'raspberry', on_connect, on_error, '/');

