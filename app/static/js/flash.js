document.addEventListener("DOMContentLoaded", function () {
    const flashcontainer = document.querySelectorAll('.flashcontainer li');
    flashcontainer.forEach(function (flash) {
        setTimeout(function () {
            flash.style.opacity = 0;
            setTimeout(function () {
                flah.remove();
            }, 500);
        }, 3000);
    });
});