document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let messages = document.getElementById("flash-messages");
        if (messages) {
            messages.style.display = "none";
        }
    }, 5000);
});
