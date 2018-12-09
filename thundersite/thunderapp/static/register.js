
$(function() {

    $(document).on('submit', '#signupuser', function (e) {
        e.preventDefault();
        var context = {
            'firstname': $('#regfirstname').val(),
            'lastname': $('#reglastname').val(),
            'username': $('#regusername').val(),
            'password': $('#regpassword').val(),
            'gender': $('#reggender').val(),
            'DofB': $('#regbday').val(),
            'email': $('#regEmail').val(),
            'hobby': $('#reghobby').val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()

        };

        $.ajax({
            type: "POST",
            url: '/register/',
            data: context,
            success: successfull
        });
    });

    function successfull(response) {
        console.log("here")
        if (response.success) {
            console.log("here")
            $("#successRegisterAlert").show();
            $("#successRegisterAlert").delay(700).addClass("in").fadeOut(2000);

            setTimeout(function () {
                window.location = '/login/'
            }, 700);
        }
        else {
            if(response.ageError){
                $("#ageerrorRegisterAlert").show();
                $("#ageerrorRegisterAlert").delay(1500).addClass("in").fadeOut(2000);
            }else if(response.usernameError) {
                $("#usernameerrorRegisterAlert").show();
                $("#usernameerrorRegisterAlert").delay(1500).addClass("in").fadeOut(2000);
            }
            else {
                $("#errorRegisterAlert").show();
                $("#errorRegisterAlert").delay(1500).addClass("in").fadeOut(2000);
            }
        }

    }


    // check new username is available
    function checkuseranswer(data, textStatus, jqHXR) {
        $('#info').html(data);
    }

    function f(page) {
        $.ajax({
            type: 'POST',
            url: '/checkuser/',
            data: {
                'username': $('input[name=username]').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'page': page,
            },
            success: checkuseranswer,
            dataType: 'html',
        });
    }

    $('#regusername').blur(function () {
        f('register');
    });
    $('#logusername').blur(function () {
        f('login');
    });

    $('#reghobby').searchableOptionList();
});

