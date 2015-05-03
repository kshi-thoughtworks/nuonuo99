$(function(){
    var select_province, $select_province;
    var select_city, $select_city;
    var select_region, $select_region;
    function on_change(select, type, value){
        if (value == "")
            return
        select.clearOptions();
        select.load(function(callback){
            $.get("/get_location/", {ct:type, cv: value}, function(data){
                if (data.status == "ERROR") {
                    alert("Error happened");
                }
                else {
                    callback(data.data);
                }
            });
        });
    }

    $select_province = $("#id_province").selectize({
        onChange: function(value){
            select_region.clearOptions();
            on_change(select_city, "p", value);
        }
    });
    $select_city = $("#id_city").selectize({
        valueField: "id",
        labelField: "name",
        searchField: ["name"],
        onChange: function(value){
            on_change(select_region, "c", value);
        }
    });
    $select_region = $("#id_region").selectize({
        valueField: "id",
        labelField: "name",
        searchField: ["name"]
    });
    select_region = $select_region[0].selectize;
    select_city  = $select_city[0].selectize;
    select_state = $select_province[0].selectize;
    /*
    $("#id_province").change(function(){
        $.get("/get_location/", {ct:"p", cv: $("#id_province").val()}, function(data){
            if (data.status == "ERROR") {
                alert("Error happened");
            }
            else {
                var html = "";
                $.each(data.data, function(index, value){
                    html += '<div data-value="' + value.id + '" data-selectable="" class="option">' + value.name + '</div>';
                });
                $("#id_city").val(data.data[0].id);
                $("#id_city").next().find("div.item").text(data.data[0].name);
                $("#id_city").next().find("div.selectize-dropdown-content").html(html);
            }
        });
    });
    */
});
