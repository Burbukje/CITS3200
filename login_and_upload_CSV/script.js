function showHidePassword() {
    var buttonName = document.getElementById("show-hide")
    var pInput = document.getElementById("pass-input");
    if (pInput.type == "password") {
        pInput.type = "text";
        buttonName.innerHTML = "Hide";
    }  
    else {
         pInput.type = "password";
        buttonName.innerHTML = "Show";
    }
}