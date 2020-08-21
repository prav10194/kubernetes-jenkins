$(document).ready(() => {

    $("#civilizationNameButton").click(() => {
        var settings = {
            "url": "/civilization?civilization=" + $("#civilizationNameInput").val(),
            "method": "GET",
            "timeout": 0,
        };

        $.ajax(settings).done(function (response) {
            console.log(response);
            $("#civilizationDescription").html("<pre>" + response + "</pre>");
        });
    })



})