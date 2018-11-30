
function uploadProfilePicture(mID) {
    var formdata = new FormData();
    var file = document.getElementById('regprofileimage'+mID).files[0];
    formdata.append('profileimage', file);
    formdata.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
    $.ajax({

        type: 'POST',
        url: '/profile/'+mID+'/uploadimage/',
        data:formdata,
        success: function (response) {
            if (response.success) {
                $('#profilePicture').load(location.href + " #profilePicture");

                $("#successAlert").show();
                $("#successAlert").delay(500).addClass("in").fadeOut(2000);

            }else{
                $("#errorAlert").show();
                $("#errorAlert").delay(1500).addClass("in").fadeOut(2000);
            }
        },
        processData: false,
        contentType: false
    });
}

