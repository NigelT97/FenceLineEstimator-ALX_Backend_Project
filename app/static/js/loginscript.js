// JavaScript source code

var registerLink = document.getElementById("registerLink");

document.querySelector("#loginLink").addEventListener("click", function () {
    document.querySelector(".form").classList.add("active");
});

registerLink.onclick = function (event) {
    event.preventDefault();
    window.location.href = "/register";
}