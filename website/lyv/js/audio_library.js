function fillTable(data) {
    $("#audiotable").jstree({
        "core" : {
            "data": data
        },
        "plugins" : ["themes", "ui"]
    }).bind("select_node.jstree", function(e, data) {
        if(data.node.li_attr.link) {
            console.log(data.node.li_attr);
            $("#audio_details").css("visibility", "visible");
            $("#audio_title").text(data.node.li_attr.title);
            $("#audio_language").text(data.node.li_attr.language);
            $("#audio_link").attr("href", data.node.li_attr.link);
        } else {
            $("#audio_details").css("visibility", "hidden");
            data.instance.toggle_node(data.node);
            // console.log("No href defined for this element");
        }
    })
}

$(document).ready(function(){
    $.ajax({
        url: "/audio-library/get",
        method: 'GET',
    }).done(function(data) {
        data = data.replace(/'/g, '"');
        console.log(data);
        fillTable(JSON.parse(data));
    }).fail(function(data) {
        alert("FAIL");
    });
})