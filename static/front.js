$(document).ready(function(){
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
        console.log("message: " +res.msg+ "\naudio_file: " +res.audio_file);
        $('#messages').append('<li>'+ res.msg +'</li>');
        playAudio(res.audio_file);
    });

    function playAudio(filename){
        var audioElement = document.createElement('audio');
        audioElement.setAttribute('src', filename);
        audioElement.load();

        audioElement.play();
        console.log("playing audio");
        audioElement.addEventListener('ended', function(){
            socket.emit('del_audio', filename);
            console.log('request for audio removal send');
        });
        playSample();
    }

    function playSample(){
        var sampleElement = document.getElementById('sampleAudio');
        var path_to_sample = '/static/audio/samples/yo.mp3';
        sampleElement.setAttribute('src', path_to_sample);
        sampleElement.play();
    }

});











