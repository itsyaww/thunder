
$(function(){

    $(document).on('submit', '#usersignin' , function(e){
    e.preventDefault();
    var context ={
        'loginusername' : $('#inputUserName').val(),
        'loginpassword':$('#inputPassword').val(),
        csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val()

    };

    $.ajax({
        type: "POST",
        url:'/login/',
        data: context ,
        success: searchSuccess,
    });

    });
});

function searchSuccess(data,textStatus,jqXHR) {
    alert("User login success")
}

