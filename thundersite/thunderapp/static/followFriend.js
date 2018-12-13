function followMember(mID) {
    $.ajax({
        type: "PUT",
        url:'/profiles/followMember/',
        data: {
            'mID':mID,
            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response) {
            if (response.success) {
                $("#followMembersuccessAlert").show();
                $("#followMembersuccessAlert").delay(1200).addClass("in").fadeOut(2000);

                setTimeout(function () {
                    window.location = '/profiles/';
                }, 1200);

            }else{
                $("#followMembererrorAlert").show();
                $("#followMembererrorAlert").delay(1500).addClass("in").fadeOut(2000);
            }

        }
    });
}

