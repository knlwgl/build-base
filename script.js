
let signinBtn = document.getElementById("signinBtn");
let registerBtn = document.getElementById("registerBtn");
let emailField = document.getElementById("email");
let title = document.getElementById("title");

signinBtn.onclick = function() {
    signinBtn.classList.remove("disable");
    registerBtn.classList.add("disable");
    emailField.style.maxHeight = "0px";
    title.innerHTML = "Build Base";
}

registerBtn.onclick = function() {
    emailField.style.maxHeight = "65px";
    title.innerHTML = "Register";
    registerBtn.classList.remove("disable");
    signinBtn.classList.add("disable");
}