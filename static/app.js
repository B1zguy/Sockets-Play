$(document).ready(function () {
    var socket = io();

    socket.on('connect', function () {
        socket.emit('others', {data: 'I\'m connected!'});
    });

    socket.on('pressed button', function (msg) {
        $('#updates').append('<li class="list-group-item">' + msg.data + '</li>');
    });

    socket.on('other-cons', function (msg) {
        console.log('checking')
        $('#updates').append('<li class="list-group-item list-group-item-primary">' + msg.data + '</li>');
    });

    $('#bPressed').on('click', function (event) {
        socket.emit('button press', {data: 'beep boop!'});
        event.preventDefault();
    });
})