import wikipedia
from speechrecognitionfunc import listen

def wikisearch(command):
    if "tell me about" in command or "who is" in command or "explain" in command or "describe" in command or "what are" in command or "What can you tell me about" in command or "define" in command or "can you explain" in command or  "information on" in command or "give me" in command:
        prompt = command.lower()  # Corrected from 'rompt' to 'prompt'
    
        phrases_to_remove = ["tell me about", "who is", "explain", "describe", "what are", "what can you tell me about", "define", "Can you explain", "information on", "give me"]
        # Define phrases to remove
    
        # Remove each phrase from the prompt
        for phrase in phrases_to_remove:
            prompt = prompt.replace(phrase, "")
        
        prompt = prompt.strip()  # Call strip() as a method
      
        try:
            summary = wikipedia.summary(prompt, sentences=3)  # Get the summary from Wikipedia
            print(summary)  # Print the summary
            return(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            print("This term is ambiguous; please be more specific.")
        except wikipedia.exceptions.PageError:
            print("Sorry, I couldn't find a page for that.")
        except Exception as e:
            print(f"An error occurred: {e}")


        