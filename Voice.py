import speech_recognition as sr
import os
from pygame import mixer # Load the required library
import time

mixer.init()

finished = False

r = sr.Recognizer()

mic = sr.Microphone()

while not finished:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Ready.")
        audio = r.listen(source)

    command = r.recognize_google(audio)
    command = command.lower()
    print(command)

    if command == "start chrome":
        finished = True
        os.system("start chrome")
    elif command == "start wireshark":
        finished = True
        os.system("start Wireshark")
    elif command.startswith("search youtube "):
        query = command[15:]
        if " " in query:
            query = query.replace(" ", "+")
        os.system('start chrome --app=https://www.youtube.com/results?search_query={}'.format(query))
        finished = True
    elif command.startswith("search google "):
        query = command[14:]
        if " " in query:
            query = query.replace(" ", "+")
        os.system('start chrome "https://www.google.com/search?q={}" --new-window'.format(query))
        finished = True

    if finished == False:
        print("Sorry we didn't recognize that. Let's try again.\n")
        mixer.music.load('Didntrecognize.mp3')
        mixer.music.play()
        time.sleep(5)
