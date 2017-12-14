var socket = new WebSocket('ws://kicker.local:15674');

/*
socket.addEventListener('open', function (event) {
    console.log("opened!");
});
*/

// Listen for messages
socket.addEventListener('message', function (message) {
    window.rstate.states = JSON.parse(message.data);
});

/*
$(document).on('click', '#score_resetter_button', function(e) {
  socket.send('{ "event": "reset" }');
});
*/

