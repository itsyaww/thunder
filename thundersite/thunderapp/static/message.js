$(function() {
    function postmessage(event) {
    $.ajax({
        type : "POST",
        url : "/postmessage/",
        data: {
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
            'recip' : $('input[name=recip]').val(),
            'messageText' : $('textarea[name=messageContent]').val(),
        },
        success : function(data) {
            $(data).appendTo("#messages-div").hide().fadeIn(400);
        },
        error: function(jqXHR, textStatus, error) {
            console.log(error);
        },
    });
    // prevent normal submission
    event.preventDefault();
    };
    // Execute a function when the user releases a key on the keyboard
    $("#messageSend").click( function(event) {
        event.preventDefault();
        postmessage(event)
    });

    function getMessage(followingUserId, userId) {
        alert("following user"+followingUserId)
        alert(" user"+userId)

    }

});