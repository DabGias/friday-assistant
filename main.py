import speech_recognition as sr
from bot_commands import Bot
import asyncio

recogn = sr.Recognizer()
mic = sr.Microphone()
bot = Bot()


with mic:
    while True:
        recogn.adjust_for_ambient_noise(mic)

        try:

            audio = recogn.listen(mic)
            command = recogn.recognize_google(audio, language='en')

            print(command)

            if command.lower() in [
                "ok friday",
                "friday",
                "okay friday"
            ]:
                bot.greetings()

                while True:
                    recogn.adjust_for_ambient_noise(mic)

                    try:
                        audio = recogn.listen(mic)
                        command = recogn.recognize_google(audio, language='pt-BR')

                        print(command)

                        if command.lower() in [
                            "clima",
                            "como está o clima",
                            "clima hoje"
                        ]:
                            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
                            asyncio.run(bot.weather())

                        elif command.lower() in [
                            "parar",
                            "ok muito obrigado",
                            "ok muito obrigada",
                            "obrigado",
                            "obrigada",
                            "muito obrigado",
                            "muito obrigada",
                            "valeu",
                            "falou"
                        ]:
                            bot.speak("Até mais! Estarei esperando por novos comandos!")
                            print("Até mais! Estarei esperando por novos comandos!")
                            break

                        else:
                            bot.speak("Desculpe, esse comando não existe!")
                            print("Desculpe, esse comando não existe!")

                    except sr.exceptions.UnknownValueError:
                        bot.speak("Desculpe, não entendi! Pode repetir?")
                        print("Desculpe, não entendi! Pode repetir?")

        except sr.exceptions.UnknownValueError:
            print("Nenhum chamado detectado!")
