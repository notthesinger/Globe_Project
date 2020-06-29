$(document).ready(function () {
    console.log("ready!");
    $("g:nth-of-type(1)").on("click", country);
    function country() {
        // get current ccountry name from tspan tag and past country from div tag in nav bar
        var countrycurrent = document.querySelectorAll('tspan')[1].innerHTML;
        var countrylast = document.getElementById("Current_country").innerHTML.split(": ")[1]
        var cond = document.querySelector("#chartdiv > div > svg > g > g:nth-child(2) > g:nth-child(2) > g > g:nth-child(4)").getAttribute("opacity");
        console.log(cond); // print country name to console
        if ((countrycurrent != countrylast) && (cond > 0.80)) {
            $.post("/data", { countrydata: countrycurrent });
            document.getElementById("Current_country").innerHTML = "Country: " + countrycurrent;
        }
    }
});

