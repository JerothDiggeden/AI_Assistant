import openai
import requests
import pyaudio
import pyttsx3
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

	response = requests.post(url_gpt, json=payload, headers=headers)
	response = response.json()
	response = response['result']
	speak = response

	engine.say(speak)
	engine.runAndWait()


# WEATHER API
def weather():
	url_weather = "https://weatherapi-com.p.rapidapi.com/current.json"

	querystring = {"q":"53.1,-0.13"}

	headers = {
		"x-rapidapi-key": "1b6ce2494dmshf74f9c461b4cdbbp1d3b11jsndd6ab0d8575c",
		"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
	}

	response = requests.get(url_weather, headers=headers, params=querystring)

	print(response.json())


while True:
	msg = input("Ask a question... ")
	chat_gpt()
