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
    $('div.message-holder').append('<div class="message"><b style="color: '+msg.color+'">'+msg.user_name+'</b> '+msg.message+'</div>');
    $('div.message-holder').scrollTop(function() { return this.scrollHeight; });
});

socket.on('user connect', function(data) {
    if (user_name === null) {
        user_name = data.player_name;
        user_color = data.player_color;
    }
    $('div.message-holder').append('<div class="message"><b style="color: #000">'+data.user_name+'</b> '+data.message+'</div>');
    $('div.message-holder').scrollTop(function() { return this.scrollHeight; });
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
    $('button.start-button').replaceWith('<div class="cards"><div class="card-container"></div>'+
        '<button type="button" class="chance-button">Draw chance</button>'+
        '<button type="button" class="community-chest-button">Draw community chest</button></div>'+
        '<!-- dice roll button and display --><div class="dice"><div class="dice-image-holder">'+
        '<img src="/static/Images/dice_1.png" class="Die-1" width="50" height="50">'+
        '<img src="/static/Images/dice_1.png" class="Die-2" width="50" height="50"></div>'+
        '<button type="button" class="dice-button">Roll dice</button></div>'
    );
    $('button.chance-button').on('click', function(e) {
        e.preventDefault();
        socket.emit('chance');
    });

    $('button.community-chest-button').on('click', function(e) {
        e.preventDefault();
        socket.emit('community chest');
    });
    $('button.dice-button').on('click', function(e) {
        e.preventDefault();
        socket.emit('roll dice');
    });
    for (i = 0; i < data.players.length; i++) {
        $('#cell0 > div.spotc').append('<div class="'+data.players[i]+'-piece gamePiece" style="background-color: '+data.colors[i]+'"></div>')
        const x = i+1
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

socket.on('update money', function(json) {
    for (i = 0; i < json.players.length; i++) {
        const x = i + 1
        $('#p'+x+'money').replaceWith('<span id="p'+x+'money">'+json.money[i]+'</span>')
    }
});


socket.on('roll result', function(json) {
    $('img.Die-1').replaceWith('<img src="' + json.die_file_1 + '" class="Die-1" width="50" height="50">');
    $('img.Die-2').replaceWith('<img src="' + json.die_file_2 + '" class="Die-2" width="50" height="50">');
});

socket.on('chance result', function(json){
     /* display monopoly_game.chance() */
    console.log(json);
    $('div.card-container').replaceWith('<div class="card-container">'+json.card_content+'</div>');
});

socket.on('community chest result', function(json){
     /* display monopoly_game.chance() */
    console.log(json);
    $('div.card-container').replaceWith('<div class="card-container">'+json.card_content+'</div>');
});

socket.on('move piece', function(json){
    $('div.'+json.player+'-piece').remove();
    if (json.in_jail) {
        $('#cell'+json.space+' > div.injail').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
    } else {
        $('#cell'+json.space+' > div.spotp').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
        $('#cell'+json.space+' > div.spotc').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
        $('#cell'+json.space+' > div.visit').append('<div class="'+json.player+'-piece gamePiece" style="background-color: '+json.color+'"></div>');
    }
});

socket.on('purchase', function(json){
    $('#cell'+json.space).css('border-color', json.color);
});
