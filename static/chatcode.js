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
        $('div.message-holder').append('<div class="message"><b style="color: '+msg.color+'">'+msg.user_name+'</b> '+msg.message+'</div>');
        $('div.message-holder').scrollTop($(document).height());
    }
});

socket.on('user connect', function(data) {
    if (user_name === null) {
        user_name = data.player_name;
        user_color = data.player_color;
    }
    $('div.message-holder').append('<div class="message"><b style="color: #000">'+data.user_name+'</b> '+data.message+'</div>');
    $('div.message-holder').scrollTop($(document).height());
});

socket.on('session full', function() {
    if (user_name === null) {
        window.location.href = '/static/session_full.html';
    }
});

$('button.start-button').on('click', function(e) {
    e.preventDefault();
    socket.emit('start game');
});

socket.on('start game', function(data) {
    $('button.start-button').replaceWith('<div class="card-container"></div>'+
        '<button type="button" class="chance-button">Draw card</button>'+
        '<!-- dice roll button and display --><div class="dice"><div class="dice-image-holder">'+
        '<img src="/static/Images/dice_1.png" class="Die-1" width="50" height="50">'+
        '<img src="/static/Images/dice_1.png" class="Die-2" width="50" height="50"></div>'+
        '<button type="button" class="dice-button">Roll dice</button></div>'
    );
    $('button.chance-button').on('click', function(e) {
        e.preventDefault();
        socket.emit('chance');
    });
    $('button.dice-button').on('click', function(e) {
        e.preventDefault();
        socket.emit('roll dice');
    });
    for (i = 0; i < data.players.length; i++) {
        $('#cell0 > div.spotc').append('<div class="'+data.players[i]+'-piece gamePiece" style="background-color: '+data.colors[i]+'"></div>')
        let x = i+1
        $('#moneytable').append('<tr id="moneybarrow'+x+'" class="money-bar-row">' +
                            '<td class="moneybararrowcell"><img src="/static/Images/arrow.png" id="p'+x+'arrow" class="money-bar-arrow" alt=">"/></td>' +
                            '<td id="p'+x+'moneybar" class="moneybarcell'+x+'">' +
                                '<div><span id="p'+x+'moneyname" >'+data.players[i]+'</span>:</div>' +
                                '<div>$<span id="p'+x+'money">1500</span></div>' +
                            '</td>' +
                        '</tr>'
        );
    }
});

socket.on('chance', function(data) {
    console.log(data);
    $('div.card-container').replaceWith('<div class="card-container">'+data.card_content+'</div>');
});

socket.on('roll result', function(json) {
    console.log('Roll result: ' + json.roll_int);
    $('img.Die-1').replaceWith('<img src="' + json.die_file_1 + '" class="Die-1" width="50" height="50">');
    $('img.Die-2').replaceWith('<img src="' + json.die_file_2 + '" class="Die-2" width="50" height="50">');
    $('div.message-holder').append('<div class="message"><b style="color: #000">'+json.user_name+'</b> '+json.message+'</div>');
    $('div.message-holder').scrollTop($(document).height());
    if (json.is_movement) {
        $('div.'+json.player+'-piece').remove();
        $('#cell'+json.space+' > div.spotp').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
        $('#cell'+json.space+' > div.spotc').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
    }
});
