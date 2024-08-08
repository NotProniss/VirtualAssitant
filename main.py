import pyttsx3
import speech_recognition as sr
import webbrowser
#from nicegui import ui

import Moduals.wiki as wiki
import Moduals.time as tTime


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

def Hello():
	
	# This function is an intro fuction for startup.
	speak("hello, I am your desktop assistant. \
		How may I help you")


def Take_query():

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
			webbrowser.open("www.google.com")
			continue
			
		elif "what day is it" in query:
			speak(tTime.tellDay())
			continue
		
		elif "what time is it" in query:
			speak(tTime.tellTime())
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye.")
			exit()
		
		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			speak(wiki.Wikipedia(query))
			speak("According to wikipedia")
		
		elif "tell me your name" in query:
			speak("I am Jarvis. Your desktop Assistant")

#ui.button('Click to speak', on_click=lambda: Take_query())

if __name__ in {"__main__", "__mp_main__"}:
	# main method for executing
	# the functions
	# ui.run()
	# calling the Hello function for 
	# making it more interactive
	Hello()
	Take_query()