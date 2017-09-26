$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        socket.emit('connect');
    });

    $('#sendMsg').click(function(){
        var msg = $('#comment').val();
        console.log(msg);
    });

});











