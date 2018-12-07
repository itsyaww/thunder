
$(function(){

    $('#search').keydown(function() {
    if($('#search').val() != ''){
    $.ajax({
        type: "GET",
        url:'/profiles/search/',
        data:{
            'filter_gender':$('input[name=genderBtn]:checked').val(),

            'search_members':$('#search').val(),
        'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'
        })
       }
     else{
        $.ajax({
            type: "GET",
            url:'/profiles/search/',
            data:{
                'search_members':"",
                'filter_gender':$('input[name=genderBtn]:checked').val(),

                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType:'html'
        })

    }
    })


   });


function searchSuccess(data) {
    $('#results').html(data)
}



