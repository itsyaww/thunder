function updateProfile(mID) {

    $.ajax({
        type: "PUT",
        url:'/profile/' +mID + '/updateprofile/',
        data:  {
            'updatefirstname':$('#profilefirstname').val(),
            'updatelastname':$('#profilelastname').val(),
            'updategender':$('#profilegender').val(),
            'updateemail':$('#profileemail').val(),

            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()

        },
        success: function(response) {
            if (response.success) {
                $("#successAlert").show();
                $("#successAlert").delay(500).addClass("in").fadeOut(2000);
            }else{
                $("#errorAlert").show();
                $("#errorAlert").delay(1500).addClass("in").fadeOut(2000);
            }

        }
    });

}

