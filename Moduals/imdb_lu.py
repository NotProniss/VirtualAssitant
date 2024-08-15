import imdb
import datetime
import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def search_movie(query):
    moviesdb = imdb.IMDb()
    movies = moviesdb.search_movie(query)
    speak('Searching for ' + query)
    if len(movies) == 0:
        speak('No result found')
    else:
        speak('I found these:')
        for movie in movies:
            title = movie['title']
            year = movie['year']
            speak(f'{title}-{year}')
            info = movie.getID()
            movie = moviesdb.get_movie(info)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            plot = movie['plot outline']
            if year < int(datetime.datetime.now().strftime('%Y')):
                print(f'{title} was released in {year} has IMDB rating of {rating}. The plot summary of the movie is {plot}')
                speak(f'{title} was released in {year} has IMDB rating of {rating}. The plot summary of the movie is {plot}')
                break
            else:
                print(f'{title} will release in {year} has IMDB rating of {rating}. The plot summary of the movie is {plot}')
                speak(f'{title} will release in {year} has IMDB rating of {rating}. The plot summary of the movie is {plot}')
                break