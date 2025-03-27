from speech_recognition import Recognizer, AudioFile, RequestError, UnknownValueError
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()
analyzer = SentimentIntensityAnalyzer()

with AudioFile("chile.wav") as audio_file:
    audio = recognizer.record(audio_file)


text = recognizer.recognize_google(audio)
print("Transcription:", text)

scores = analyzer.polarity_scores(text)
print(scores)

if scores["compound"] > 0:
    print("Positive Speech")
else:
    print("Negative Speech")