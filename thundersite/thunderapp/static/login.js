

var input = document.getElementById("inputPassword");

// Execute a function when the user releases a key on the keyboard
input.addEventListener("keyup", function(event) {
    // Cancel the default action, if needed
        if (event.keyCode === 13) {
            // Trigger the button element with a click
            loginUser()
        }
});

var input2 = document.getElementById("inputUserName");

// Execute a function when the user releases a key on the keyboard
input2.addEventListener("keyup", function(event) {
    // Cancel the default action, if needed
    if (event.keyCode === 13) {
        // Trigger the button element with a click
        loginUser()
    }
});



function loginUser() {

    $.ajax({
        type: "POST",
        url:'/login/',
        data:  {
            'username' : $('#inputUserName').val(),
            'password':$('#inputPassword').val(),
            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {


            if (response.success ==false) {

                $("#errorLoginAlert").show();
                $("#errorLoginAlert").delay(1500).addClass("in").fadeOut(2000);
            }
            else {
                $("#successLoginAlert").show();
                $("#successLoginAlert").delay(700).addClass("in").fadeOut(2000);
                console.log("LOGIN SUCCESSFUL");
                setTimeout(function () {
                    window.location = '/profile/'
                }, 700);
            }
        }
    });
}


