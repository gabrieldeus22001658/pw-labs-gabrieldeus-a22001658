let weather = {
  apiKey: "ce2a845e3a0cf3ad0456eb08cf5bb48d",
  fetchWeather: function () {
    fetch(
     "https://api.openweathermap.org/data/2.5/weather?lat=38.7&lon=-9.1&appid=ce2a845e3a0cf3ad0456eb08cf5bb48d"
    )
     .then((response) => response.json())
     .then((data) => this.displayWeather(data));
  },
  displayWeather : function(data) {
    const {name} = data;
    const {icon} = data.weather[0];
    let {temp} = data.main;
    temp2 = Math.round(temp - 273.15);
    console.log(name, icon, temp2);
     document.querySelector(".icon").src =
      "https://openweathermap.org/img/wn/" + icon + ".png";
    document.querySelector(".temp").innerText = temp2 + "ºC";
    document.querySelector(".cidade").innerText = name;
  }
};