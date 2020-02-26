import requests, json

api_key = "f92b732fb564fd9ae89096f6542dde43"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("city")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]

	current_pressure = y["pressure"]


	current_humidiy = y["humidity"]


	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))
    fc = owm.daily_forecast('London,uk', limit=6)

else:
	print(" City Not Found ")
