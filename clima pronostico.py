import pyowm

owm = pyowm.OWM('f92b732fb564fd9ae89096f6542dde43')

location = owm.weather_at_coords(20.6, -100.3833)
weather = location.get_weather()

fc = owm.three_hours_forecast_at_coords(20.6, -100.3833)


print(weather )
print(fc)