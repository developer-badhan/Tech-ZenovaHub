// Admin Theme Toggle
document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    if (!themeToggle) return;

    themeToggle.addEventListener("click", () => {
        let htmlTag = document.documentElement;
        if (htmlTag.getAttribute("data-bs-theme") === "dark") {
            htmlTag.setAttribute("data-bs-theme", "light");
            localStorage.setItem("adminTheme", "light");
        } else {
            htmlTag.setAttribute("data-bs-theme", "dark");
            localStorage.setItem("adminTheme", "dark");
        }
    });
    if (localStorage.getItem("adminTheme") === "dark") {
        document.documentElement.setAttribute("data-bs-theme", "dark");
    }
});

document.querySelectorAll('[id^="adminTogglePassword"]').forEach(toggleBtn => {
    toggleBtn.addEventListener("click", () => {
        const input = toggleBtn.parentElement.querySelector("input");
        const icon = toggleBtn.querySelector("i");
        if (input.type === "password") {
            input.type = "text";
            icon.classList.replace("fa-eye", "fa-eye-slash");
        } else {
            input.type = "password";
            icon.classList.replace("fa-eye-slash", "fa-eye");
        }
    });
});
