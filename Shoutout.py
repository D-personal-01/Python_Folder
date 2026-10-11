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