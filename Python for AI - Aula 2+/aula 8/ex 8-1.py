import pyttsx3 as tts

engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say(f'Hello World')
engine.runAndWait()
