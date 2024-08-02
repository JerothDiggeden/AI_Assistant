import openai
import requests
import pyaudio
import pyttsx3
from datetime import date
from icecream import ic
from openai import OpenAI
import speech_recognition as sr


pyttsx3.init("sapi5", False)
url_gpt = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
engine = pyttsx3.init()
engine.say("How can I be of assistance?")
engine.runAndWait()


# CHAT GPT
def chat_gpt():
	payload = {
		"messages": [
			{
				"role": "user",
				"content": msg
			}
		],
		"system_prompt": "",
		"temperature": 0.9,
		"top_k": 5,
		"top_p": 0.9,
		"max_tokens": 256,
		"web_access": False
	}
	headers = {
		"x-rapidapi-key": "1b6ce2494dmshf74f9c461b4cdbbp1d3b11jsndd6ab0d8575c",
		"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
		"Content-Type": "application/json"
	}

	response_gpt = requests.post(url_gpt, json=payload, headers=headers)
	response_gpt = response_gpt.json()
	response_gpt = response_gpt['result']
	speak = response_gpt

	engine.say(speak)
	engine.runAndWait()


# WEATHER API
def weather_current():
	url_weather_current = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"Perth"}

	headers = {
		"x-rapidapi-key": "1b6ce2494dmshf74f9c461b4cdbbp1d3b11jsndd6ab0d8575c",
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
	}

	response_current = requests.get(url_weather_current, headers=headers, params=querystring)

	response_current = response_current.json()
	weather_current = (f"The current temperature is {response_current['current']['temp_c']}, "
					   f"{response_current['current']['condition']['text']}")
	engine.say(weather_current)
	engine.runAndWait()
	print(response_current)


def weather_future():
	url_weather_future = "https://weatherapi-com.p.rapidapi.com/future.json"

	querystring = {"q": "Perth"}

	headers = {
		"x-rapidapi-key": "1b6ce2494dmshf74f9c461b4cdbbp1d3b11jsndd6ab0d8575c",
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
	}

	response_future = requests.get(url_weather_future, headers=headers, params=querystring)

	print(response_future.json())


def date_time():
	today = date.today()
	engine.say(today.strftime("%A %d. %B %Y"))
	engine.runAndWait()


while True:
	msg = input("Ask a question... ")
	# chat_gpt()
	date_time()
	weather_current()
	weather_future()

