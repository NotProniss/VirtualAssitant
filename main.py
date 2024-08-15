import pyttsx3
import speech_recognition as sr
from playsound import playsound as ps
#from nicegui import ui

import Moduals.wiki as wiki
import Moduals.time as tTime
import Moduals.google as google
import Moduals.imdb_lu as imdb

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module 
	# we will use the Microphone module
	# to listen for a command
	with sr.Microphone() as source:
		print('Listening')
		ps('Data/sfx/start_speaking.mp3')
		#ui.label('Listening')
		# seconds of non-speaking audio before 
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized 
		# it is good else we will have exception 
		# handling
		try:
			print("Recognizing")
			ps('Data/sfx/stop_speaking.mp3')
			#ui.label('Recognizing')
			
			# for Listening the command in indian
			# english we can also use 'hi-In' 
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("heard command = ", Query)
			#ui.label('the command is printed=', Query)
			
		except Exception as e:
			print(e)
			print("Say that again")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[1].id)
	
	# Method for the speaking of the assistant
	engine.say(audio) 
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def hello():
	
	# This function is an intro fuction for startup.
	ps('Data/sfx/greeting.mp3')
	speak("hello, I'm Q your desktop assistant. \
		How may I help you")

#### Attempting to set up an "always listening" feature that starts ###
#### the takeQuery command with an "ok google" like thing ####
'''def main():
	while(True):
		start = takeCommand().lower()
		if "lucy" in start:
			takeQuery()
			continue
		elif "exit" or "quit" or "bye" in start:
			speak('Goodbye')
			ps('Data/sfx/goodbye.mp3')
			exit()
		else:
			continue'''
#########################################################################

def takeQuery():

	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate 
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times 
		# query matches and we get the perfect 
		# output
		query = takeCommand().lower()	
		if "open google" in query:
			speak("Opening Google ")
			google.open_google()
			continue
			
		elif "what day is it" in query:
			speak(tTime.tellDay())
			continue
		
		elif "what time is it" in query:
			speak(tTime.tellTime())
			continue
		
		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			speak(wiki.Wikipedia(query))
			speak("According to wikipedia")
			continue
		
		elif "tell me your name" in query:
			speak("I am Q. Your desktop Assistant")
			continue
		
		elif 'imdb' in query:
			speak('would you like me to search IMDB?')
			query = takeCommand().lower()
			if 'yes' in query:
				speak('search for what exactly?')
				query = takeCommand().lower()
				imdb.search_movie(query)
				continue
			else:
				speak('Alright I wont')
				continue

		elif "bye" in query:
			speak('Goodbye')
			ps('Data/sfx/goodbye.mp3')
			exit()


#ui.button('Click to speak', on_click=lambda: Take_query())

if __name__ in {"__main__", "__mp_main__"}:
	# main method for executing
	# the functions
	# ui.run()
	# calling the Hello function for 
	# making it more interactive
	hello()
	takeQuery()