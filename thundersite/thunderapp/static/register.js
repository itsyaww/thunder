
$(function(){

    $(document).on('submit', '#signupuser' , function(e){
    e.preventDefault();
    var context ={
            'firstname': $('#regfirstname').val(),
            'lastname': $('#reglastname').val(),
            'username' : $('#regusername').val(),
            'password':$('#regpassword').val(),
            'gender':$('#reggender').val(),
            'DofB':$('#regbday').val(),
            'email':$('#regEmail').val(),

            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val()

    };

    $.ajax({
        type: "POST",
        url:'/register/',
        data: context ,
        success: searchSuccess,
    });

    });
});

function searchSuccess(data,textStatus,jqXHR) {
    alert("Added user")
}

