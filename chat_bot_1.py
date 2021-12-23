import webbrowser
import datetime
import os

hello_intent = ["hello", "heyy", "good morning", "good afternoon", "hi", "hii"]
bye_intent = ["bye", "see you", "talk to you later", "ttyl", "soon", "later"]
date_intent = ["date", "show date", "date please", "day"]
time_intent = ["time", "show time", "time please"]
while True:
    msg = input("Enter your message: ")
    if msg.lower() in hello_intent:
        print("Heyy there")
    elif msg.lower() in bye_intent:
        print("See you around")
        break
    elif msg.lower() in date_intent:
        print(datetime.date.today())
    elif msg.lower() in time_intent:
        print(datetime.datetime.now().strftime("%H:%M:%S"))
    elif "google" in msg.lower():
        webbrowser.open("www.google.com")
    elif "youtube" in msg.lower():
        webbrowser.open("www.youtube.com")
    elif "song" or "play" in msg.lower():
        song_list = os.listdir(r"D:\songs")
        os.startfile(r"D:\songs\\"+song_list[0])
    else:
        print("I don't understand")
