$(function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
});

$(document).ready(function () {
    let req = new XMLHttpRequest();
    var sortableList = $(".sortableList");

    var sortEventHandler = function(event, ui){
        console.log("New Sort order!");
        sortableList = $(".sortableList");

        var listElements = sortableList.children();

        let listValues = [];
        for (i = 0; i < listElements.length; i++){
            listValues.push(listElements[i].innerHTML);
        }
        console.log(listValues);
        var str = listValues[0];
        var e = listValues[0].split(/"/)[1];
        console.log(e);
        $.post("/reorder", {"listValues[]":listValues});
    };

    sortableList.sortable({
        stop: sortEventHandler
    });

});
