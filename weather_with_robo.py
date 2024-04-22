import requests
import json
import win32com.client 

city = input("Enter the name of the city\n");

url =f"http://api.weatherapi.com/v1/current.json?key=9151d0f5ab0042f5a84180648241802&q={city}"


speaker = win32com.client.Dispatch("SAPI.SpVoice") 
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
lang = wdic["location"]["lat"]
time = wdic["location"]["localtime"]

# while 1: 
    # print("Enter the word you want to speak it out by computer") 
s =  f"The current weather in {city} is {w} degrees, latitudes is {lang} and time is {time}"
speaker.Speak(s) 
print(s)

