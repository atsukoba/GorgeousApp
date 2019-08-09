let chart_opt = {
    legend: {
        display: false
    },
    tooltips: {
        enabled: false
    }
}

function draw(_id) {
    let canvas = document.getElementById(_id)
    let ctx = canvas.getContext('2d');
    console.log(ctx)
    let score = Number(document.getElementById(_id + "_data").innerHTML)
    console.log(score)
    let myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ["M", "T"],
        datasets: [{
        backgroundColor: [
            "#f000ff",
            "#f5f5f5"
        ],
        data: [score, 100 - score]
        }],
    },
    options: chart_opt
    });
    canvas.nextElementSibling.innerHTML = String(score) + "%"
}

window.onload = function() {
    draw("myChart");
    draw("myChart_2");
    draw("myChart_3");
    draw("myChart_4");
    draw("myChart_5");
}
