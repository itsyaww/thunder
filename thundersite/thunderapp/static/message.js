$("#msg-form").submit(function(event) {
    $.ajax({
        type : $(this).attr('method'),
        url : $(this).attr('action'),
        data: {
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val(),
            'recip' : $('input[name=recip]').val(),
            'text' : $('textarea[name=text]').val(),
            'pm' : $(".pm_class:checked").val(),
        },
        success : function(data) {
            $(data).prependTo("#messages-div").hide().fadeIn(400);
            $('.remove-btn').click(remove_button);
        },
        error: function(jqXHR, textStatus, error) {
            console.log(error);
        },
    });
    // prevent normal submission
    event.preventDefault();
});