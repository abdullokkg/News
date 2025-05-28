

$(document).ready(function() {
  function showDate() {
    var time = new Date();
    var date = time.getDate();
    var year = time.getFullYear();

    var monthArray = new Array();
    monthArray[0] = "January";
    monthArray[1] = "February";
    monthArray[2] = "March";
    monthArray[3] = "April";
    monthArray[4] = "May";
    monthArray[5] = "June";
    monthArray[6] = "July";
    monthArray[7] = "August";
    monthArray[8] = "September";
    monthArray[9] = "October";
    monthArray[10] = "November";
    monthArray[11] = "December";
    month = monthArray[time.getMonth()];

    var dateDiv = document.getElementById("date");
    dateDiv.innerText = month + " " + date + ", " + year;
  }

  function showTime() {
    var time = new Date();
    var hours = time.getHours();
    var minutes = time.getMinutes();
    var seconds = time.getSeconds();

    // format numbers
    if (hours < 10) {
      hours = "0" + hours;
    }
    if (minutes < 10) {
      minutes = "0" + minutes;
    }
    if (seconds < 10) {
      seconds = "0" + seconds;
    }
    if (hours == 0) {
      showDay();
      hours = 12;
    }

 
  }

  showDate();
  setInterval(showTime, 1);
});