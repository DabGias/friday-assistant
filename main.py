import speech_recognition as sr
from bot_commands import Bot

recogn = sr.Recognizer()
mic = sr.Microphone()
bot = Bot()

with mic:
    while True:
        recogn.adjust_for_ambient_noise(mic, duration=1)

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
                    recogn.adjust_for_ambient_noise(mic, duration=1)

                    try:
                        audio = recogn.listen(mic)
                        command = recogn.recognize_google(audio, language='pt-BR')

                        print(command)

                        if command.lower() in [
                            "adicionar na agenda",
                            "adicionar evento na agenda",
                            "adicionar evento"
                        ]:
                            bot.add_event_schedule()

                        elif command.lower() in [
                            "ler agenda",
                            "ver agenda",
                            "agenda",
                            "ver eventos",
                            "ler eventos",
                            "meus eventos",
                            "minha agenda",
                            "ler minha agenda",
                            "ver minha agenda",
                            "ler meus eventos",
                            "ver meus eventos"
                        ]:
                            bot.read_schedule()

                        elif command.lower() in [
                            "abrir meu navegador",
                            "abrir navegador",
                            "navegador",
                            "google"
                        ]:
                            bot.open_browser()

                        elif command.lower() in [
                            "me conte uma piada",
                            "conte uma piada",
                            "conte-me uma piada",
                            "piada",
                            "me faça rir",
                            "faz-me rir",
                            "quero rir",
                            "quero sorrir",
                            "me anime",
                            "estou triste",
                            "estou cabisbaixo"
                        ]:
                            bot.tell_joke()

                        elif command.lower() in [
                            "que horas são",
                            "horas",
                            "horário"
                        ]:
                            bot.what_time()

                        elif command.lower() in [
                            "me conte um fato aleatório",
                            "me conte algo aleatório",
                            "me fale uma informação aleatória",
                            "me conte uma informação aleatória"
                        ]:
                            bot.random_info()

                        elif command.lower() in [
                            "abrir vs code",
                            "abrir code",
                            "abrir visual studio code",
                            "vs code",
                            "visual studio code",
                            "code"
                        ]:
                            bot.vscode()

                        elif command.lower() in [
                            "hora de programar",
                            "hora de trabalhar",
                            "ambiente de trabalho",
                            "ativar ambiente de trabalho"
                        ]:
                            bot.set_env()

                        elif command.lower() in [
                            "calculadora",
                            "abrir calculadora",
                            "calcular"
                        ]:
                            bot.calc()

                        elif command.lower() in [
                            "dicionário",
                            "me ajude com uma palavra"
                        ]:
                            bot.dict()

                        elif command.lower() in [
                            "parar",
                            "ok muito obrigado",
                            "ok muito obrigada",
                            "obrigado",
                            "obrigada",
                            "muito obrigado",
                            "muito obrigada",
                            "valeu",
                            "falou",
                            "tchau"
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
