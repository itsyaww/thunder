count = 0;
function friendInfo(mID) {
    $.ajax({
        type: "GET",
        url:'/profile/friend/',
        data: {
            'friendID':mID,
            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
            if (response.success) {
                $("#friendUsername").text(response.username);
                $("#friendName").text(response.name);
                $("#friendDOB").text(response.DOB);
                $("#friendGender").text(response.gender);
                $("#friendImg").attr('src', response.image);
                $.each(response.hobbies, function(k, v) {

                    $("#friendHobby").append("<div id='hob" + k +"'>"+v+"</div>");
                    count = count + 1;

                });
                $("#profileinfo").show();

            }else{

            }

        }
    });
}

$("#closefriendInfo").click(function(){
    $("#profileinfo").fadeOut(700);

    while(count >= 0) {
        $("#hob" + count).remove();
        count = count -1;
    }

});

$("#messageUser").click(function(){
    window.location = '/messages/';
});
