import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):     # This function speak string which pass as audio parameter.
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good Morning!")

	elif hour >=12 and hour < 18:
		speak("Good Afternoon!")

	else:
		speak("Good Evening!")

	speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():   # This function takes microphone input from the user and returns string output.
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening................")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Rcongnizing............")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		# print(e)
		print("Say that again please........")
		return "None"

	return query


def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('anils.rana97@gmail.com', 'maid_id password')
	server.sendmail('anils.rana97@gmail.com', to, content)
	server.close()


if __name__ == '__main__':
	wishMe()
	while True:
		query = takeCommand().lower()

	# Logic for executing tasks based on query............
		if 'wikipedia' in query:
			speak('Searching Wikipedia........')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=1)
			print(results)
			speak("According to wikipedai")
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			music_dir = 'D:\\AUDIO SONGS\\MP3 SONGS\\music'
			songs = os.listdir(music_dir)
			# print(songs)
			song_number = random.randint(0, 200)
			os.startfile(os.path.join(music_dir, songs[song_number]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		elif 'open vs code' in query:
			code_path = "C:\\Users\\rana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
			os.startfile(code_path)

		elif 'mail to anil' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "anils.rana97@gmail.com"  #to = "ranasuraj48@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent to Anil Rana")

			except Exception as e:
				print(e)
				speak("Sorry my friend Anil I am not able to send this email")

		elif 'mail to suraj' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "ranasuraj48@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent to Suraj Rana")

			except Exception as e:
				print(e)
				speak("Sorry my friend Anil I am not able to send this email")









