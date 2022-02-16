$("svg.radial-progress").each(function (index, value) {
    $("svg.radial-progress").each(function (index, value) {
        $(this).find($("circle.complete")).removeAttr("style");
    });

    percent = $(value).data("percentage");
    radius = $(this).find($("circle.complete")).attr("r");
    circumference = 2 * Math.PI * radius;
    strokeDashOffset = circumference - (percent * circumference) / 100;
    $(this)
        .find($("circle.complete"))
        .animate({ "stroke-dashoffset": strokeDashOffset }, 1250);
});


const labels = ["Field1", "Field2", "Field3", "Field4", "Field5", "Field6"]
const data = {
  labels: labels,
  datasets: [{
    label: 'Average Density per Field in Percent ( % )',
    data: [1, 12, 15, 14, 3, 2],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1
  }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    },
};

const densityChart = new Chart(
    document.getElementById('densityChart'),
    config
  );

const squareData = {
  labels: labels,
  datasets: [{
    label: 'Square for every Field in m^2',
    data: [75471, 12423, 16745, 552514, 353453, 23556],
    backgroundColor: [
      'rgba(255, 99, 132, 0.2)',
      'rgba(255, 159, 64, 0.2)',
      'rgba(255, 205, 86, 0.2)',
      'rgba(75, 192, 192, 0.2)',
      'rgba(54, 162, 235, 0.2)',
      'rgba(153, 102, 255, 0.2)',
      'rgba(201, 203, 207, 0.2)'
    ],
    borderColor: [
      'rgb(255, 99, 132)',
      'rgb(255, 159, 64)',
      'rgb(255, 205, 86)',
      'rgb(75, 192, 192)',
      'rgb(54, 162, 235)',
      'rgb(153, 102, 255)',
      'rgb(201, 203, 207)'
    ],
    borderWidth: 1
  }]
};

const squareConfig = {
    type: 'bar',
    data: squareData,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    },
};

  const squareChart = new Chart(
    document.getElementById('squareChart'),
    squareConfig
  );

