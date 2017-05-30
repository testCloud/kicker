var ws = new WebSocket('ws://kicker.local:15674/ws');
var client = Stomp.over(ws);

var on_connect = function() {
    console.log('connected');
    //var sub = client.subscribe('/queue/amq.gen-vGxOrDvHFqEzY_D0cctNkw', function(message) {
    var sub = client.subscribe('/queue/simon', function(message) {
        console.log("WebWorker: " + message.body);
    });
};
var on_error =  function() {
    console.log('error');
};
client.connect('pi', 'raspberry', on_connect, on_error, '/');

