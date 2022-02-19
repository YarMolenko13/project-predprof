let results = document.getElementById("data_json").value;
let totalDensity = 0;
let totalSquare = 0;
// let totalWheat = 0;
let densityList = [];
let squareList = [];
// let wheatList = 0;

resultsList = JSON.parse(results)["results"];
console.log(resultsList)
let resultsLength = resultsList[0].length;
console.log(resultsLength)
for (let i = 0; i < resultsLength; i++) {
    console.log(resultsList[0][i], resultsList[1][i])
    densityList.push(resultsList[0][i]);
    squareList.push(resultsList[1][i]);
    // wheatList.push(resultsList[i][2])

    totalDensity += resultsList[0][i];
    totalSquare += resultsList[1][i];
    // totalWheat += resultsList[i][2];
}

let averageDensity = Math.round(totalDensity / resultsLength, 2);
let averageSquare = Math.round(totalSquare / resultsLength);
console.log(averageDensity, averageSquare)

let averageSquareElem = document.getElementById("avg-square");
averageSquareElem.innerHTML = averageSquare.toString() + " m^2";
let averageDensityData = document.getElementById("avg-dens-data");
averageDensityData.setAttribute("data-percentage", averageDensity)
let averageDensityText = document.getElementById("avg-dens-text");
averageDensityText.innerHTML = averageDensity.toString();

let generatedColors = Array(resultsLength)
    .fill()
    .map(() => random_rgba());

$("svg.radial-progress").each(function (index, value) {
    $("svg.radial-progress").each(function (index, value) {
        $(this).find($("circle.complete")).removeAttr("style");
    });

    percent = $(value).data("percentage");
    radius = $(this).find($("circle.complete")).attr("r");
    circumference = 2 * Math.PI * radius;
    strokeDashOffset = circumference - (percent * circumference) / 100;
    $(this).find($("circle.complete")).animate({ "stroke-dashoffset": strokeDashOffset }, 1250);
});

const labels = range(1, resultsLength);
const data = {
    labels: labels,
    datasets: [
        {
            label: "Average Density for Fields in Wheats/m^2",
            data: densityList,
            backgroundColor: generatedColors,
            borderWidth: 1,
        },
    ],
};

const config = {
    type: "bar",
    data: data,
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    },
};

const densityChart = new Chart(document.getElementById("densityChart"), config);

const squareData = {
    labels: labels,
    datasets: [
        {
            label: "Square of every Field in m^2",
            data: squareList,
            backgroundColor: generatedColors,
            borderWidth: 1,
        },
    ],
};

const squareConfig = {
    type: "bar",
    data: squareData,
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    },
};

const squareChart = new Chart(document.getElementById("squareChart"), squareConfig);

function range(start, end) {
    if (start === end) return [start];
    return [start, ...range(start + 1, end)];
}

function random_rgba() {
    var o = Math.round,
        r = Math.random,
        s = 255;
    return "rgba(" + o(r() * s) + "," + o(r() * s) + "," + o(r() * s) + "," + 0.2 + ")";
}
