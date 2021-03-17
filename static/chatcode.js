const socket = io.connect('http://' + document.domain + ':' + location.port);
let user_name = null;
let user_color = null;

socket.on('connect', function() {
    let form = $('form').on('submit', function(e) {
        e.preventDefault();
        let user_input = $('input.message').val();
        socket.emit('new chat', {
            user_name : user_name,
            color: user_color,
            message : user_input
        });
        $('input.message').val('').focus();
    });
});

socket.on('new chat', function(msg) {
    console.log(msg);
    if(typeof msg.user_name !== 'undefined') {
        $('div.message_holder').append('<div class="message"><b style="color: '+msg.color+'">'+msg.user_name+'</b> '+msg.message+'</div>');
        $('div.message_holder').scrollTop($(document).height());
    }
});

socket.on('user connect', function(data) {
    if (user_name === null) {
        user_name = data.player_name;
        user_color = data.player_color;
    }
    $('div.message_holder').append('<div class="message"><b style="color: #000">'+data.user_name+'</b> '+data.message+'</div>');
    $('div.message_holder').scrollTop($(document).height());
});