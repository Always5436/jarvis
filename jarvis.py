# import wmi
import time
# import turtle
import winsound
import PyPDF2
import instaloader
import requests
from time import sleep
import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import pywhatkit as kit
from requests import get
import smtplib
import sys
import pyautogui


# import threading
# from multiprocessing import Process,Queue
# import time
# os.system('taskkill /f /im notepad.exe') [To close any window follow this command]


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("what can i do for you")


# it will take mic input and will give output as string
# to add timeout and phase time limit
def takecommand():
    # audio setting
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognition....')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        speak("Sorry, Say that again please...")
        return 'blank'
    return query


def game():
    my_choice = ["rock", "scissor", "paper"]
    print("lets play the game")
    comp = 0
    point = 0
    print("how many time do you like to play this game ")
    i = int(input())
    while i >= 1:
        cpu = random.choice(my_choice)
        print("\nentre r, s, p for rock, scissor, paper respectively")
        user = input()
        if user == "r" or "s" or "p":
            if user == "r":
                if cpu == "rock":
                    print("both have same hands so no point to both ")
                    speak("that's a tie")
                elif cpu == "scissor":
                    print("player broke mine scissor so player won")
                    speak("user won")
                    point += 1
                else:
                    print("ahha, i wrapped rock so i won")
                    speak("computer won")
                    comp += 1
            elif user == "s":
                if cpu == "rock":
                    print("my rock broke your scissor so i won")
                    speak("computer won")
                    comp += 1
                elif cpu == "scissor":
                    print("both have same choice so no point ")
                    speak("thats a tie")
                else:
                    print("you cut me into pieces, you won")
                    speak("user won")
                    point += 1
            else:
                if cpu == "rock":
                    print("you wrapped me in your paper so you won ")
                    speak("user won")
                    point += 1
                elif cpu == "scissor":
                    print("my scissor cutted your paper in pieces so i won ")
                    speak("computer won")
                    comp += 1
                else:
                    print("both have same choice so no point")
                    speak("that is a tie")
        else:
            print("you lost this round because you are not making right choice. So choice from s, w, g")
            comp += 1
        print("number of round left = ", i - 1)
        speak(f"number of round left = {i - 1}")
        print(f"score is\n user = {point} and computer = {comp}")
        speak(f"users score is {point}")
        i -= 1
    if point > comp:
        g = "congrats you won"
        print(g)
        speak(g)
    elif point == comp:
        g = "thats a tie"
        print(g)
        speak(g)
    else:
        g = "computer won the game"
        print(g)
        speak(g)


def news():
    main_url = 'https://newsapi.org/v2/everything?q=Apple&from=2021-12-04&sortBy=popularity&apiKey=62ad00018952499da5e50db8deef7ec5'

    main_page = requests.get(main_url).json()
    articles = main_page['articles']
    head = []
    day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


# to send mail
# hadnt added this in main function
def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    id = "abc@example.com"
    pas = 'New Password'
    server.login(id, pas)
    server.sendmail(id, to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    # i = 1
    # query = 'selfie'
    # query = 'close everything'
    while True:
        query = takecommand().lower()
        # query = 'music'
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            print('Searching wikipedia...')
            query = query.replace("on wikipedia", " ")
            query = query.replace("search", " ")
            results = wikipedia.summary(query, sentences=2)
            # if we want more sentences then change the upper number
            speak("According to wikipedia")
            print(results)
            speak(results)
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'presentation' in query:
            path = "E:\\jarvis\\CHATBOT.ppsx"
            os.startfile(path)
            

        elif 'close presentation' in query:
            os.system('taskkill /f /im CHATBOT.ppsx')
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'notepad' in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'close notepad' in query:
            speak('closing notepad')
            os.system('taskkill /f /im notepad.exe')
            speak('sir any another task for me')
            print('sir any another task for me')


        elif 'open command prompt' in query:
            os.system('start cmd')

        # to get result from google
        elif 'search' in query:
            speak('searching on google')
            print('Searching on Google')
            query = query.replace("search", "")
            results = kit.search(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
             

        elif 'close youtube' in query:
            pyautogui.keyDown('win')
            pyautogui.press('3')
            pyautogui.keyUp('win')
            pyautogui.keyDown('ctrl')
            pyautogui.press('w')
            pyautogui.keyUp('ctrl')
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'goto' in query:
                pyautogui.keyDown('win')
                if 'first' in query:
                    pyautogui.press('1')
                elif 'second' in query:
                    pyautogui.press('2')
                elif 'third' in query:
                    pyautogui.press('3')
                elif 'fourth' in query:
                    pyautogui.press('4')
                elif 'fifth' in query:
                    pyautogui.press('5')
                elif 'six' in query:
                    pyautogui.press('6')
                elif 'seven' in query:
                    pyautogui.press('7')
                elif 'eight' in query:
                    pyautogui.press('8')
                pyautogui.keyUp('win')
                speak('anything else in which i may help')
                print('anything else in which i may help')

        elif 'open google' in query:
            webbrowser.open("google.com")
             

        elif 'close google' in query:
            pyautogui.keyDown('win')
            pyautogui.press('m')
            pyautogui.keyUp('win')
            speak('anything else in which i may help')
            print('anything else in which i may help')



        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
             

        elif 'read' in query:
            name = input('enter the name of pdf') + ".pdf"
            book = open(name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(f'total number of pages are {pages}')
            print('sir tell me the page number i should start reading from')
            speak('sir tell me the page number i should start reading from')
            pg = int(input())
            page = pdfReader.getPage(pg)
            text = page.extractText()
            speak(text)
             

        elif 'screen' in query:
            name = 'scrsht' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            print('hold screen for a while please')
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f'{name}.png')
            print('screen shot captured, whats next')
            sys.exit()
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'insta profile' in query:
            print('sir please enter the user name ')
            speak('sir please enter the user name ')
            name = input('Enter username here : ')
            webbrowser.open(f'www.instagram.com/{name}')
            print(f'sir here is the profile of the user {name}')
            speak(f'sir here is the profile of the user {name}')
            # time.sleep(5)
            print('sir would you lke to download profile picture')
            speak('sir would you lke to download profile picture')
            query = takecommand.lower()
            if 'yes' in query:
                mod = instaloader.Instaloader()
                # mod.download_profile()
                mod.download_profile(name, profile_pic_only=True)
                print('download complete')
                speak('sir any another task for me')
                print('sir any another task for me')
            else:
                pass


        elif 'hide' or 'show' in query:
            query = input()
            if 'hide' in query:
                os.system('attrib +h /s /d')
                print('all files of this folder are hidden')

            elif 'show' in query:
                os.system('attrib -h /s /d')
                print('all the files are visible now')

            else:
                pass
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'open instagram' in query:
            if 'message' in query:
                webbrowser.open("https://www.instagram.com/direct/inbox/")
            else:
                webbrowser.open("instagram.com")
             

        elif 'open mail' in query:
            pyautogui.hotkey('win', '1')
            speak('sir any another task for me')
            print('sir any another task for me')


        elif 'open code' in query:
            pyautogui.hotkey('win', '6')
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'music' in query:
            music_dir = 'E:\\music\\music\\selected'
            songs = os.listdir(music_dir)
            while True:
                song = random.choices(songs)
                if '.mp3' in song[0]:
                    os.startfile(os.path.join(music_dir, song[0]))
                    break
                else:
                    continue
            break
             

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'the date' in query:
            strTime = datetime.datetime.now().date()
            print(f"Sir, the date is {strTime}")
            speak(f"Sir, the date is {strTime}")
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'open brave' in query:
            bravepath = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(bravepath)
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'game' in query:
            j = 1
            while j == 1:
                game()
                print('do you want to play this again')
                speak('do you want to play this again')
                p = takecommand()
                if yes in query:
                    pass
                else:
                    j = 2


        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your ip address in {ip}')
            print(f'your ip address in {ip}')
            speak('anything else sir')
            print('anything else sir')

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            print('anything else sir')
            speak('anything else sir')

        elif 'play' in query:
            gaana = 'leave me alone'
            speak('playing' + gaana)
            kit.playonyt(gaana)


        elif 'app message' in query:
            speak('whom you want to send the message ')
            print('Whom you want to send the message ')
            while True:
                speak("please tell me there number")
                print("please tell me there number")
                num = takecommand()
                # num = '9812864649'
                num = "+91" + num
                speak(f'entred number is {num}')
                # query = 'yes'
                query = takecommand()
                if 'yes' in query:
                    while True:
                        speak('is message a picture')
                        print('Is message a picture')
                        query = takecommand().lower()
                        # query = 'no'
                        if query is 'none':
                            continue
                        else:
                            if query is 'yes':
                                speak('entre the path')
                                print('Entre the path')
                                f = input()
                                while True:
                                    speak('entre the caption')
                                    print('Entre the caption')
                                    cap = takecommand()
                                    # cap = input()
                                    print("is your caption ")
                                    speak("Is your caption ")
                                    print(cap)
                                    speak(cap)
                                    query = takecommand()
                                    if 'yes' in query:
                                        if cap is 'none':
                                            cap = ''
                                        kit.sendwhats_image(phone_no=num, img_path=f, caption=cap)
                                        pyautogui.press('Enter')
                                        break
                                    else:
                                        continue
                            else:
                                while True:
                                    speak('ok, tell me the message')
                                    print('Ok, Tell me the message')
                                    mess = takecommand()
                                    # mess = 'hello'
                                    speak('is your message')
                                    print('is your message')
                                    speak(mess)
                                    query = takecommand()
                                    # query = 'yes'
                                    if 'yes' in query:
                                        speak('do you want to schedule that message')
                                        print('Do you want to schedule that message')
                                        query = takecommand()
                                        # query = 'no'
                                        if 'yes' in query:
                                            speak('ok')
                                            print('Ok')
                                            speak('tell me the time you want to send the message in 24 hour format')
                                            print('Tell me the time you want to send the message in 24 hour format')
                                            speak('tell me hour')
                                            print('Tell me hour')
                                            hr = takecommand()
                                            # hr = input()
                                            hr = int(hr)
                                            speak('tell me minute')
                                            print('Tell me minute')
                                            mint = takecommand()
                                            # mint = input()
                                            mint = int(mint)
                                            speak(f'time given is {hr} hours and {mint} minutes')
                                            print(f'time given is {hr} hours and {mint} minutes')
                                            kit.sendwhatmsg(num, mess, hr, mint)
                                            pyautogui.press('Enter')
                                            break
                                        else:
                                            kit.sendwhatmsg_instantly(num, mess)
                                            pyautogui.press('Enter')
                                            break
                                    else:
                                        continue
                            break
                    break
                else:
                    continue
            break
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'send email' in query:
            try:
                speak('whom you want to send email')
                to = input("Entre email: ")
                while True:
                    speak('what should i send')
                    mess = takecommand()
                    speak(f'message is {mess}')
                    print(f'message is {mess}')
                    query = takecommand().lower()
                    if query == 'yes':
                        sendEmail(to, mess)
                        speak(f'Email sent to {to}')
                        print(f'Email sent to {to}')
                        break
                    else:
                        continue

            except Exception as e:
                print(e)
                speak("sorry email not sent")

        elif 'who are' in query:
            print('Hello sir, This ia jarvis a bot. A project created by Mohit .')
            speak('Hello sir, This ia jarvis a bot. A project created by Mohit.')

        elif 'which python' in query:
            print(
                'Sir i am working on python 3.7.1 Because this is not so old version and is highly stable with most '
                'of the modules available')
            speak(
                'Sir i am working on python 3.7.1 Because this is not so old version and is highly stable with most '
                'of the modules available')

        elif 'what can you' in query:
            print(
                'Sir, I can search any query for you on wikipedia, or youtube or google, and can also play jokes and '
                'songs for you, and can even send message on whatsapp, and you can also play rock scissor paper with '
                'me ')
            speak(
                'Sir, I can search any query for you on wikipedia, or youtube or google, and can also play jokes and '
                'songs for you, and can even send message on whatsapp, and you can also play rock scissor paper with '
                'me ')

        elif 'selfie' in query:
            print('Sir just smile in the camera and i will capture that moment')
            speak('Sir just smile in the camera and i will capture that moment')
            cap = cv2.VideoCapture(0)
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
            while True:
                _, frame = cap.read()
                original_frame = frame.copy()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = face_cascade.detectMultiScale(gray, 1.3, 5)
                for x, y, w, h in face:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    face_roi = frame[y:y + h, x:x + w]
                    gray_roi = gray[y:y + h, x:x + w]
                    smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                    for x1, y1, w1, h1 in smile:
                        cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
                        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                        file_name = f'selfie-{time_stamp}.png'
                        cv2.imwrite(file_name, original_frame)
                cv2.imshow('cam star', frame)
                if cv2.waitKey(10) == ord('q'):
                    break


        elif 'no' in query:
            speak("thanks for using me have a great day")
            sys.exit()

        elif 'switch app' in query:
            pyautogui.hotkey('alt', 'tab')

        elif 'brightness' in query:
            cap = cv2.VideoCapture(0)

            mpHands = mp.solutions.hands
            hands = mpHands.Hands()
            mpDraw = mp.solutions.drawing_utils

            while True:
                success, img = cap.read()
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = hands.process(imgRGB)

                lmList = []
                if results.multi_hand_landmarks:
                    for handlandmark in results.multi_hand_landmarks:
                        for id, lm in enumerate(handlandmark.landmark):
                            h, w, _ = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmList.append([id, cx, cy])
                        mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

                if lmList != []:
                    x1, y1 = lmList[4][1], lmList[4][2]
                    x2, y2 = lmList[8][1], lmList[8][2]

                    cv2.circle(img, (x1, y1), 4, (255, 0, 0), cv2.FILLED)
                    cv2.circle(img, (x2, y2), 4, (255, 0, 0), cv2.FILLED)
                    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                    length = hypot(x2 - x1, y2 - y1)

                    bright = np.interp(length, [15, 220], [0, 100])
                    print(bright, length)
                    sbc.set_brightness(int(bright))

                    # Hand range 15 - 220
                    # Brightness range 0 - 100

                cv2.imshow('Image', img)
                if cv2.waitKey(1) & 0xff == ord('q'):
                    break

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close everything' in query:
            j = 1
            while j < 10:
                pyautogui.hotkey('alt', 'tab')
                pyautogui.hotkey('alt', 'f4')
                j += 1



        elif 'news' in query:
            speak('sir let me fetch latest one ')
            print('sir let me fetch latest one ')
            news()
            speak('sir any another task for me')
            print('sir any another task for me')

        elif 'wait' in query:
            while True:
                query = takecommand()
                if 'jarvis' in query:
                    pass
            break


