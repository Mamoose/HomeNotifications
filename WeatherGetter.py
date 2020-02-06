import pyowm
owm = pyowm.OWM(API_key="92eed9c3261fc479722a309d91fd04c1")
observation = owm.weather_at_coords(40.0334,83.1582)
w = observation.get_weather()
humidity = w.get_humidity()
temp = w.get_temperature('fahrenheit')['temp']
dewpoint = w.get_dewpoint()
