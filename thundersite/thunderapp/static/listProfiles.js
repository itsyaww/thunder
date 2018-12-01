
$(function(){

$('#btn').click(function(){

    $.ajax({
        type: "GET",
        url:'/profiles/',
        data:{
        'members':$('#listProfiles').val(),
        'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'
        })

    })
});
function searchSuccess(data,textStatus,jqXHR) {
    $('#results').html(data)
}










