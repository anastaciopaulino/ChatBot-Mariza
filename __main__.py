#-*- coding: utf-8 -*-

# Importando módulos
import os
import speech_recognition as sr
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Mariza", read_only=True)
trainer = ListTrainer(bot)

for _file in os.listdir("chats"): # percorrendo todos os arquivos
    lines = open("chats/" + _file, "r").readlines() # vamos ler linhas
    trainer.train(lines)


def Speak(phrase):
    os.system("espeak %s"%(phrase))

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio =  r.listen(s)
        try:
            speech = r.recognize_google(audio, language="pt-PT", show_all=False)
            print ('Você disse: ',  speech)
        except sr.UnknownValueError:
            print("Bot: Não compriendo!")
            continue
        else:
            print("Bot: ", bot.get_response(speech))
    