# -*- coding: utf-8 -*-
import urllib.request, urllib.parse, urllib.error
import json

class Weather():
	
	def __init__(self):

		# ref: https://open-meteo.com/en/docs , using timezone: JST
		request = urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?latitude=35.69&longitude=139.69&current_weather=true&windspeed_unit=ms&forecast_days=1&timezone=Asia%2FTokyo")
		self.weather_data = json.loads(request.read())

	def getTemperature(self):
		return self.weather_data["current_weather"]["temperature"]

	def getWindSpeed(self):
		return self.weather_data["current_weather"]["windspeed"]

	def getUpdateTime(self):
		# 2023-01-12T12:00 -> 01-12 1200
		return self.weather_data["current_weather"]["time"].replace("T", " ").replace(":", "")[5:]


if __name__ == "__main__":
	weather = Weather()
	print(f"Tokyo: {weather.getTemperature()} {weather.getWindSpeed()} {weather.getUpdateTime()}")
