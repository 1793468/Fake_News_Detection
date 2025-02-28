document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.onsubmit = function (e) {
        const textarea = document.querySelector("textarea");
        if (textarea.value.trim() === "") {
            alert("Please enter news content before prediction.");
            e.preventDefault();
        }
    };
});
