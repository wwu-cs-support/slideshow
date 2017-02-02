$(function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
});

$(document).ready(function () {
    var sortableList = $(".sortableList");

    var sortEventHandler = function(event, ui){
        console.log("New Sort order!");
        sortableList = $(".sortableList");

        var listElements = sortableList.children();

        var listValues = [];
        for (i = 0; i < listElements.length; i++){
            listValues.push(listElements[i].innerHTML);
        }
        console.log(listValues);
    };

    sortableList.sortable({
        stop: sortEventHandler
    });

});
