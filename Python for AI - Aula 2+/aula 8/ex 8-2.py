import speech_recognition as sr
import pyautogui

funcoes = {}
numfuncoes = 0

with open('biblioteca', 'r') as file:
    for linha in file:
        linha = linha.split(';')
        funcoes[numfuncoes]=linha

print(funcoes)
rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Say something!")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)
    for i in funcoes:
        if funcoes[i][0]==texto:
            exec(funcoes[i][1])
