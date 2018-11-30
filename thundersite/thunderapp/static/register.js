
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
        success: searchSuccess
    });

    });
});

function searchSuccess(response) {
    if (response.success) {
        $("#successRegisterAlert").show();
        $("#successRegisterAlert").delay(500).addClass("in").fadeOut(2000);
    }
    else {
        $("#errorRegisterAlert").show();
        $("#errorRegisterAlert").delay(1500).addClass("in").fadeOut(2000);
    }
    if (response.redirect !== undefined && response.redirect) {

        window.location.href = response.redirect_url;

    }
}
