
$(function(){

$('#genderBtn2').change(function(){

    $.ajax({
        type: "GET",
        url:'/profiles/searchgender/',
        data:{
            'filter_by_gender':'Male',
            'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
        },
        success: searchSuccess,
        dataType:'html'
        })

    });

    $('#genderBtn1').change(function(){

        $.ajax({
            type: "GET",
            url:'/profiles/searchgender/',
            data:{
                'filter_by_gender':'',
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType:'html'
        })

    });

    $('#genderBtn3').change(function(){

        $.ajax({
            type: "GET",
            url:'/profiles/searchgender/',
            data:{
                'filter_by_gender':'Female',
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










