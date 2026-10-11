import random
import time
import speech_recognition as sr


# ------------------------------
# Status Messages
# ------------------------------

LISTENING_MESSAGES = [
    "Listening to today's story...",
    "Your thoughts have my attention...",
    "Recording your reflection...",
    "Listening carefully...",
    "Collecting today's moments...",
    "Ready whenever you are...",
    "Capturing your experiences...",
    "Turning your voice into memories...",
    "One thought at a time...",
    "Waiting for today's journal...",
    "Listening beyond the words...",
    "Your journey begins here...",
    "Every story matters...",
    "Building today's reflection...",
    "I'm listening..."
]

PROCESSING_MESSAGES = [
    "Distilling today's thoughts...",
    "Connecting the dots...",
    "Finding meaningful moments...",
    "Extracting today's highlights...",
    "Understanding your journey...",
    "Looking beneath the surface...",
    "Transforming words into insights...",
    "Organizing your reflections...",
    "Finding patterns...",
    "Updating today's story...",
    "Building your reflection...",
    "Sorting today's experiences...",
    "Reading between the lines...",
    "Making sense of today's journal...",
    "Almost there..."
]

SUCCESS_MESSAGES = [
    "Journal captured successfully.",
    "Reflection saved.",
    "Today's thoughts are ready.",
    "Journal completed.",
    "Your story has been recorded.",
    "Ready for analysis.",
    "Today's journal is complete.",
    "Reflection successfully captured."
]

ERROR_MESSAGES = [
    "I couldn't understand that.",
    "Looks like the room was a little noisy.",
    "Let's try that once more.",
    "Nothing was detected.",
    "I couldn't catch your words."
]


# ------------------------------
# Animated Status
# ------------------------------

def animated_status(message, duration=2):

    frames = [
        ".",
        "..",
        "...",
        "...."
    ]

    end_time = time.time() + duration

    while time.time() < end_time:

        for frame in frames:

            print(f"\r{message}{frame}   ", end="", flush=True)

            time.sleep(0.25)

            if time.time() >= end_time:
                break

    print()


# ------------------------------
# Speech Recognition
# ------------------------------

recognizer = sr.Recognizer()


def record_journal(
        silence_timeout=10,
        ambient_duration=1):

    print(random.choice(LISTENING_MESSAGES))

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=ambient_duration
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=None
            )

        animated_status(
            random.choice(PROCESSING_MESSAGES),
            duration=2
        )

        text = recognizer.recognize_google(audio)

        print(random.choice(SUCCESS_MESSAGES))

        return text

    except sr.WaitTimeoutError:

        print("No speech detected.")

        return None

    except sr.UnknownValueError:

        print(random.choice(ERROR_MESSAGES))

        return None

    except sr.RequestError as e:

        print(f"Speech API Error : {e}")

        return None


# ------------------------------
# Demo
# ------------------------------

if __name__ == "__main__":

    journal = record_journal()

    print("\nJournal\n")

    print(journal)
    