"use strict"

function search_lga(param) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("NICEEE " + param);
        }
    };
    xhttp.open("GET", "/search", true);
    xhttp.send();

}