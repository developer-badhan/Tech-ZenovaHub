$(document).ready(function () {
    toastr.options = {
        closeButton: true,
        progressBar: true,
        positionClass: "toast-top-right",
    };

    // Show toast if data is passed from backend in template
    if (typeof toast_status !== "undefined" && toast_message) {
        toastr[toast_status](toast_message);
    }

    // Show toast from query params
    const urlParams = new URLSearchParams(window.location.search);
    const status = urlParams.get("status");
    const message = urlParams.get("message");

    if (status && message) {
        toastr[status](message);
        // Remove query params from URL without refreshing
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});
