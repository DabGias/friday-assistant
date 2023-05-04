import python_weather
import pyttsx3
import datetime
from datetime import time
import os
import wikipedia


class Bot:
    def __init__(self):
        self.__bot = pyttsx3.init()
        self.__voices = self.__bot.getProperty('voices')

        self.__bot.setProperty('voice', 'voices[1].id')
        self.__bot.setProperty('volume', 1.0)
        self.__bot.setProperty('rate', 260)

    def speak(self, text: str):
        self.__bot.say(text)
        self.__bot.runAndWait()

    def greetings(self):
        hour = datetime.datetime.now().hour

        if 0 <= hour < 12:
            self.speak("Bom dia! Estou ao seu dispor!")
            print("Bom dia! Estou ao seu dispor!")
        elif 12 <= hour < 18:
            self.speak("Boa tarde! Estou ao seu dispor!")
            print("Boa tarde! Estou ao seu dispor!")
        else:
            self.speak("Boa noite! Estou ao seu dispor!")
            print("Boa noite! Estou ao seu dispor!")

    def add_event_schedule(self):
        pass

    def read_schedule(self):
        pass

    async def weather(self):
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get('New York')

            print(weather.current.temperature)
            self.speak(weather.current.temperature)

            for forecast in weather.forecasts:
                print(forecast)
                self.speak(forecast)

                for hourly in forecast.hourly:
                    print(f"--> {hourly!r}")
