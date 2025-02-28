const ctx = document.getElementById("pieChart").getContext("2d");

new Chart(ctx, {
    type: "pie",
    data: {
        labels: ["Fake News", "Real News"],
        datasets: [{
            label: "News Type",
            data: [40, 60],
            backgroundColor: ["#FF4136", "#28a745"],
            hoverOffset: 4
        }]
    }
});
