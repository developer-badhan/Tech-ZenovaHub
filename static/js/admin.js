document.addEventListener("DOMContentLoaded", function() {
    const toggle = document.getElementById("themeToggle");
    toggle.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");
        if (document.body.classList.contains("dark-mode")) {
            toggle.classList.replace("fa-moon", "fa-sun");
        } else {
            toggle.classList.replace("fa-sun", "fa-moon");
        }
    });
});
