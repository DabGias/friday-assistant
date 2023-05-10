import random
import webbrowser
import datetime
import os

import pyttsx3
import speech_recognition as sr
import wikipedia
import requests
import json


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
        if 0 <= datetime.datetime.now().hour < 12:
            self.speak("Bom dia! Estou ao seu dispor!")
            print("Bom dia! Estou ao seu dispor!")

        elif 12 <= datetime.datetime.now().hour < 18:
            self.speak("Boa tarde! Estou ao seu dispor!")
            print("Boa tarde! Estou ao seu dispor!")

        else:
            self.speak("Boa noite! Estou ao seu dispor!")
            print("Boa noite! Estou ao seu dispor!")

    def add_event_schedule(self):
        recogn = sr.Recognizer()
        mic = sr.Microphone()

        with mic:
            while True:
                recogn.adjust_for_ambient_noise(mic, duration=1)
                self.speak("Que evento gostaria de adicionar?")
                print("Que evento gostaria de adicionar?")

                try:
                    audio = recogn.listen(mic)
                    event = recogn.recognize_google(audio, language='pt-BR')

                    self.speak("Você quer adicionar {} na sua agenda?".format(event))
                    print("Você quer adicionar {} na sua agenda?".format(event))

                    audio = recogn.listen(mic)
                    perm = recogn.recognize_google(audio, language='pt-BR')

                    if perm.lower() in [
                        "sim",
                        "com certeza",
                        "positivo",
                        "ok",
                        "afirmativo",
                        "certamente"
                    ]:
                        try:
                            f = open("agenda.txt", "x")

                        except FileExistsError:
                            f = open("agenda.txt", "a")

                        f.write(event.lower())
                        f.close()

                        self.speak("{} foi adicionado na sua agenda!".format(event))
                        print("{} foi adicionado na sua agenda!".format(event))

                        break

                    else:
                        continue

                except sr.exceptions.UnknownValueError:
                    self.speak("Desculpe, não entendi! Pode repetir?")
                    print("Desculpe, não entendi! Pode repetir?")

    def read_schedule(self):
        self.speak("Lendo sua agenda...")
        print("Lendo sua agenda...")

        try:
            for line in open("agenda.txt"):
                self.speak(line)
                print(line)

            self.speak("Não há mais eventos na sua agenda!")
            print("Não há mais eventos na sua agenda!")

        except FileNotFoundError:
            self.speak("Você não possui eventos na sua agenda!")
            print("Você não possui eventos na sua agenda!")

    def show_schedule(self):
        self.speak("Abrindo sua agenda...")
        print("Abrindo sua agenda")

        os.system("agenda.txt")

    def open_browser(self):
        self.speak("Abrindo seu navegador padrão!")
        print("Abrindo seu navegador padrão!")

        webbrowser.open("https://google.com")

    def tell_joke(self):
        jokes = [
            """
Joãozinho chega atrasado à escola. Quando ele entra na sala de aula, a professora diz:
- De novo atrasado, Joãozinho?
- Ué, professora! Não é a senhora que diz que nunca é tarde para aprender?
            """,
            """
Mais uma vez, Joãozinho chega atrasado à escola.
- O que houve dessa vez, Joãozinho?
- Fui atacado por um pit-bull no caminho da escola, professora!
- Nossa! E tá tudo bem? Ele mordeu você?
- Morder ele não mordeu. Mas comeu toda a lição de casa.
            """,
            """
Joãozinho chegou à escola mais uma vez atrasado.
- Joãozinho, que desculpa você vai dar desta vez?
- É que eu estava sonhando com um jogo de futebol, professora.
- Ah, é? E o que isso tem a ver com o seu atraso?
- É que o jogo empatou, teve prorrogação e foi pros pênaltis!
            """,
            """
- Joãozinho, preciso regar as plantas lá no quintal. Preste atenção quando ferver o leite, hein?
- Claro, mamãe.
O leite ferveu e o chão da cozinha ficou todo molhado. Quando a mãe voltou, não acreditou no que viu.
- Mas, Joãozinho, eu te pedi para prestar atenção quando fervesse o leite.
- E eu prestei. Eram exatamente 10:35.
            """,
            """
Pra variar, Joãozinho está boiando na aula de Língua Portuguesa.
- Joãozinho, me diga dois pronomes.
- Quem? Eu?
- Muito bem, Joãozinho!
            """,
            """
- Mãe, meus amigos estão dizendo que eu sou interesseiro.
- Quais amigos, Joãozinho?
- Se você me der 10 reais eu te conto.
            """,
            """
A professora pergunta pro Joãozinho:
- Joãozinho, se eu lhe der dois gatos, mais dois gatos, mais dois gatos, quantos gatos você terá?
- Sete.
- Acho que o Joãozinho não entendeu a pergunta. Eu lhe dou dois gatos, mais dois gatos, mais dois gatos. Com quantos gatos você fica?
- Sete, professora.
- Vamos mudar a pergunta. Eu lhe dou duas laranjas, mais duas laranjas, mais duas laranjas. Com quantas laranjas você fica?
- Seis.
- Muito bem, Joãozinho! Agora vamos voltar ao exemplo dos gatos. Dois gatos, mais dois gatos, mais dois gatos: com quantos gatos você fica?
- Sete.
- Mas por que sete, Joãozinho?
- Porque eu já tenho um gato em casa.
            """,
            """
Joãozinho foi o único aluno da classe a acertar o problema matemático que a professora havia dado de lição. Desconfiada, ela pergunta:
- Joãozinho, você fez a lição junto com seu pai?
- Claro que não, professora!
- Que ótima notícia, Joãozinho!
- Meu pai fez sozinho mesmo.
            """,
            """
A professora pergunta para o Joãozinho:
- Joãozinho, por que você não fez a lição de casa?
- Porque eu moro em apartamento.
            """,
            """
Joãozinho chegou em casa pulando de alegria.
- Mãe! Mãe! Hoje a professora fez uma pergunta pra classe e eu fui o único a levantar a mão!
- Mas que boa notícia, filho! E o que foi que ela perguntou?
- Quem não fez a lição de casa.
            """,
            """
Joãozinho chega em casa depois da escola. A mãe pergunta:
- Como foi na escola hoje, Joãozinho?
- Foi como no Polo Norte.
- Como assim?! Polo Norte?!
- Tudo abaixo de zero.
            """,
            """
- Joãozinho, quanto é um menos um?
- Não sei, professora.
- Um menos um, Joãozinho! É fácil!
- Sei não, fessora...
- Vamos lá: eu tenho uma manga e como essa manga. O que sobra?
- O caroço.
            """,
            """
Joãozinho interrompe a explicação para fazer uma pergunta;
- Professora, como faz para colocar um elefante na geladeira?
- Não sei, Joãozinho.
- Ora, abre a porta da geladeira e põe ele lá.
A turma cai na gargalhada. Menos a professora, é claro.
- E como faz para colocar uma girafa dentro da geladeira?
- Abre a porta da geladeira e põe ela lá - respondeu a professora.
- Não, professora. Primeiro tem que tirar o elefante de lá de dentro.
A professora dá um longo suspiro e retoma a explicação.
- Professora!
- De novo, Joãozinho?
- O leão fez uma festa na savana. Sabe qual o único animal que não pôde ir?
- Qual, Joãozinho?
- A girafa. É que ela ainda estava na geladeira.
Assim que a professora retoma a explicação, Joãozinho a interrompe pela terceira vez:
- Professora!
- Ah, Joãozinho, mais uma vez?
- Prometo que é a última pergunta. Como a gente faz pra atravessar um rio cheio de jacaré?
- Entra num barco e atravessa o rio.
- Não precisa de tudo isso, professora. Dá para ir nadando.
- Mas e os jacarés?
- Estão na festa do leão.
            """,
            """
Joãozinho pergunta para sua mãe:
- Mãe, a senhora sabia que vermelho é a cor do amor?
- Claro que sim, filho.
- Te amo, mãe. Toma aqui meu boletim.
            """,
            """
Joãozinho telefona para a professora tarde da noite.
- Professora, será que a senhora poderia repetir o que disse hoje na aula?
- Nossa, Joãozinho! Ficou tão interessado assim?
- Não, é que eu não consigo pegar no sono.
            """,
            """
- Joãozinho, conjugue o verbo andar.
- Eu ando, tu andas, ele anda, nós...
- Mais rápido, Joãozinho!
- Eu corro, tu corres, ele corre, nós...
            """,
            """
Ansioso pelo resultado da prova, Joãozinho pergunta:
- Professora, já corrigiu as provas?
- Ainda não, Joãozinho. Tenho várias turmas.
Logo em seguida, a professora pergunta:
- Todos fizeram a lição de casa?
Joãozinho responde:
- Ainda não, professora, tenho vários professores.
            """,
            """
Quando Joãozinho chega em casa, seu pai pergunta:
- Recebeu o boletim, filho?
- Sim, pai, recebi.
- E cadê ele?
- Emprestei pro Juca.
- Como assim emprestou pro Juca?!
- É que ele queria dar um susto no pai dele.
            """,
            """
Na aula de Geografia, a professora diz:
- Juquinha, aponta no mapa onde fica a América.
A Juquinha se levanta e aponta corretamente onde fica a América no mapa.
- Agora você, Joãozinho. Quem descobriu a América?
- A Juquinha, professora.
            """,
            """
Joãozinho pergunta para a professora:
- Professora, alguém pode ser castigado por algo que não fez?
- Isso jamais, Joãozinho.
- Que bom! É que não fiz a lição de casa.
            """,
            """
- Mãe, quero dar dinheiro para aquele velhinho que está na rua.
A mãe fica super contente com a iniciativa do filho. Que alma generosa! Ela dá uns trocados para Joãozinho e pergunta quem é o velhinho para quem ele vai dar o dinheiro.
- Aquele que está vendendo sorvete.
            """,
            """
A professora de inglês pede para que Joãozinho formule uma frase com a palavra window. Joãozinho pensa e diz:
- Quando me chamam, eu digo: "Já estou window".
            """,
            """
Quando Joãozinho chega em casa, a mãe pergunta:
- Como foi na escola hoje, filho?
- Fui bem, mãe!
- Que bom! Aprendeu tudo?
- Acho que não, mãe. Se tivesse aprendido tudo não teria que voltar lá amanhã.
            """,
            """
Joãozinho entrega para o pai o boleto da mensalidade escolar.
- Puxa! Como é caro estudar nessa escola, hein?
- Pois é, pai. E olha que eu quase não estudo.
            """
        ]
        joke = random.choice(jokes)

        self.speak(joke)
        print(joke)

    def what_time(self):
        self.speak("São {} e {}".format(
            datetime.datetime.now().hour,
            datetime.datetime.now().minute
        ))
        print("São {}:{}".format(
            datetime.datetime.now().hour,
            datetime.datetime.now().minute
        ))

    def random_info(self):
        wikipedia.set_lang("pt")
        self.speak(wikipedia.page(wikipedia.random()).content.split("\n")[0])
        print(wikipedia.page(wikipedia.random()).content.split("\n")[0])

    def vscode(self):
        self.speak("Abrindo o VSCode...")
        print("Abrindo o VSCode...")

        os.system('cmd /c "code"')

    def set_env(self):
        self.speak("Setando seu ambiente...")

        webbrowser.open("https://google.com")
        webbrowser.open("https://www.youtube.com/")
        webbrowser.open("https://mail.google.com/")
        os.system('cmd /c "code"')

    def calc(self):
        self.speak("Abrindo calculadora...")
        os.system("calc.exe")

    def dict(self):
        recogn = sr.Recognizer()
        mic = sr.Microphone()

        with mic:
            while True:
                recogn.adjust_for_ambient_noise(mic, duration=1)
                self.speak("Que palavra deseja buscar no dicionário?")
                print("Que palavra deseja buscar no dicionário?")

                try:
                    audio = recogn.listen(mic)
                    word = recogn.recognize_google(audio, language='pt-BR')

                    self.speak("Você quer que eu procure a definição de {}?".format(word))
                    print("Você quer que eu procure a definição de {}?".format(word))

                    audio = recogn.listen(mic)
                    perm = recogn.recognize_google(audio, language='pt-BR')

                    if perm.lower() in [
                        "sim",
                        "com certeza",
                        "positivo",
                        "ok",
                        "afirmativo",
                        "certamente"
                    ]:
                        self.speak("Estou procurando a definição de {}...".format(word))
                        print("Estou procurando a definição de {}...".format(word))

                        resp = json.loads(requests.get("https://dicio-api-ten.vercel.app/v2/{}".format(word)).content)

                        self.speak(word)
                        print(word.title())

                        self.speak(resp[0]["partOfSpeech"])
                        print(resp[0]["partOfSpeech"])

                        for meaning in resp[0]["meanings"]:
                            self.speak(meaning)
                            print(meaning)

                        self.speak(resp[0]["etymology"])
                        print(resp[0]["etymology"])

                        break

                    else:
                        continue

                except sr.exceptions.UnknownValueError:
                    self.speak("Desculpe, não entendi! Pode repetir?")
                    print("Desculpe, não entendi! Pode repetir?")
