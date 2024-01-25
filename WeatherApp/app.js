const API_KEY = '32f207058ff47eb4a41cafbd136c33fc';
const form = document.querySelector("form");
const search = document.querySelector("#search");
const weather = document.querySelector("#weather");

const getWeather = async(city) => {
    console.log('Fecting weeather for city')
    console.log(city);
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;
    const response = await fetch(url);
    const data = await response.json();
    // console.log(data);
    if(data.cod == "404"){
        weather.innerHTML = `<h2> City Not Found </h2>`;
        return;
    }



    weather.innerHTML = `
    <div>
         <h2> ${data.main.temp} °C</h2>
         <h4> ${data.weather[0].main} </h4>
    </div>
`;
   
};

form.addEventListener (
    "submit",
    function(event) {
        getWeather(search.value)
        event.preventDefault();
    }
)