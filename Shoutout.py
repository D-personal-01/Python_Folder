# I am following Code with Harry's Python course and this is my shoutout program. It uses the pyttsx3 library to convert text to speech.
#but im going to make it much better...

import pyttsx3

def speak_names(names):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # speed of speech
    
    for name in names:
        print(f"Speaking: {name}")
        engine.say(name)
        engine.runAndWait()

# Example usage
names_list = ["Alice", "Bob", "Charlie", "Diana"]
speak_names(names_list)