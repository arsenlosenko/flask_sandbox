$(document).ready(function(){
    // TODO: remove audio from cache, so it could load new file

    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        socket.emit('connect_event', "User is connected!");
    });

    $('#sendMsg').click(function(){
        var msg = $('#text_input').val();
        if(msg.length != 0){
            socket.emit('send_message', msg);
            $('#text_input').val('');
        }
        else{
            console.log('empty msg. please try again');
        }
    });

    socket.on('message', function(res){
        console.log(res.msg +"\n"+ res.audio_file);
        $('#messages').append('<li>'+ res.msg +'</li>');
        playAudio(res.audio_file);
    });

    function playAudio(filename){
        var audioElement = document.createElement('audio');
        audioElement.setAttribute('src', filename);

        audioElement.play();
        console.log("playing audio");

        audioElement.addEventListener('ended', function(){
            socket.emit('del_audio', filename);
            console.log('audio removed');
        });
    }
});











