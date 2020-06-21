$(document).ready(function () {
    console.log("ready!");
    var test = "Cool"
    var t = $("g:nth-of-type(1)").on("click", country);
    function country(i) {
        var num = document.querySelectorAll('tspan')[1].innerHTML;
        console.log(i);
        $.post("/data", { numdata: num });
    }
});