
$(document).on('submit', '#signupuser' , function(e){
    e.preventDefault();


    $.ajax({
        type: "POST",
        url:'/users/register/',
        data:  {
            'username' : $('#regusername').val(),
            'password':$('#regpassword').val(),
            'gender':$('#reggender').val(),
            'DofB':$('#regbday').val(),
            'email':$('#regEmail').val(),

            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val()

        },
        success: searchSuccess,
        dataType:'html'
    })


});

function searchSuccess(data,textStatus,jqXHR) {
    alert("Added user")
}
