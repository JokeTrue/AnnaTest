$(document).ready(function () {
    var socket = new ReconnectingWebSocket('ws://' + window.location.host + '/ws');

    socket.onopen = function () {
        console.log('WS Connection established!')
    };

    socket.onmessage = function (event) {
        var results = $('.results');
        var data = JSON.parse(event.data);

        if (data.type == 'new_value') {
            results.append($('<div class="f_value">' + data.value + '</div>').hide());
            $('.f_value:last').fadeIn(500);
        } else if (data.type == 'error') {
            alert('Enter valid value');
        }
    };

    socket.onclose = function (event) {
        if (event.wasClean) {
            console.log('Clean connection close');
        } else {
            console.log('Exception');
        }
        console.log('Code: ' + event.code + ' Reason: ' + event.reason);
    };

    $('#find_btn').click(function () {
        var val = $('#factorial_value').val();

        if (val) {
            $('.results').empty();
            if (socket.readyState === 1) {
                socket.send(JSON.stringify({
                    'type': 'factorial',
                    'value': val
                }))
            }
        } else {
            alert('Enter value')
        }
    })

});