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
        success: function(data) {
            alert("Profile Data Updated")
        }
    });

}
