import wikipedia

def Wikipedia(query):        
        # if any one wants to have a information
		# from wikipedia
		query = query.replace("wikipedia", "")
			
		# it will give the summary of 4 lines from 
		# wikipedia we can increase and decrease 
		# it also.
		result = wikipedia.summary(query, sentences=4)
		return result