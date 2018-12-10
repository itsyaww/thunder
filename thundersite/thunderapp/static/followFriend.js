function followMember(event, mID) {
    $.ajax({
        type: "PUT",
        url:'/profiles/followMember/',
        data: {
            'mID':mID,
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