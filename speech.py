import pyttsx3
import speech_recognition as sr
import random
import numpy as np
import noisereduce as nr
import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        sr_audio = audio.sample_rate
        # Convert audio data to numpy array
        audio_data = np.frombuffer(audio.frame_data, dtype=np.int16)

        # Apply noise reduction
        reduced_audio_data = nr.reduce_noise(audio_data, sr_audio)

        # Convert back to AudioData
        cleaned_audio = sr.AudioData(reduced_audio_data.tobytes(), audio.sample_rate, audio.sample_width)
        try:
            user_input = recognizer.recognize_google(cleaned_audio)
            print("You said:", user_input)
            return user_input.lower()
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

def random_index(total_questions):
    return random.randint(0,total_questions)

def main():
     with open("conversation_log.txt", "a") as log_file:
        questions = ["Would you like to go on an adventure?",
                "Are you a fan of starwars",
                "Have you watched the Friend's series","Is technology making humanity better?", 
                "Do you believe in aliens?","Would you rather travel back in time or visit the future?",
                "Have you ever gone skydiving?",
                "Do you enjoy solving puzzles or brain teasers?",
                "Would you consider yourself an adventurous eater?",
                "Have you ever experienced a paranormal encounter?",
                "Do you believe in the concept of soulmates?",
                "Would you be interested in living on another planet?",
                "Do you enjoy watching horror movies?",
                "Would you like to learn a new language?",
                "Have you ever participated in a talent show?",
                "Do you believe in the existence of ghosts?",
                "Would you want to visit space if given the opportunity?",
                "Have you ever tried bungee jumping?",
                "Do you enjoy reading science fiction novels?",
                "Would you like to learn how to play a musical instrument?",
                "Have you ever gone scuba diving?",
                "Do you believe in luck or fate?",
                "Would you like to live in a different country for a year?",
                "Do you enjoy stargazing or astronomy?"]
        question = questions[random_index(len(questions)-1)]
        speak(question)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write("Timestamp: " + current_time + "\n")
        log_file.write("Question: " + question + "\n")
        attempts = 0
        while attempts < 3:
            response = get_audio().lower() 
            if response == "yes" or response == "no":
                # Log the response
                log_file.write("User's response: " + response + "\n")
                if response == "yes":
                    speak("Great! Let's embark on an exciting journey.")
                else:
                    speak("That's okay. Maybe next time.")
                break
            else:
                log_file.write("Invalid response\n")
                speak("Sorry, I didn't get that.")
                if attempts !=2: 
                    speak(question)
                attempts += 1

if __name__ == "__main__":
    main()