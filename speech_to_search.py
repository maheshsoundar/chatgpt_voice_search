import sys

from speech_to_text import *
from chatgpt_response import *

if __name__ == "__main__":

    while True:
        # Convert voice to text
        print("Listening for search query...")
        voice_text = ListenAudio().take_command()

        if voice_text:
            print(f"You want to search for: {voice_text}")

            # Use the text to chat with GPT
            response = ChatGPTResponse().get_response(voice_text)

            print("Here is the chat gpt response:")
            print(response)
        else:
            print("Error in responding or recognizing voice. Please try again!")
        
        print('Do you want to make another search')
        reply = ListenAudio().take_command()
        print(reply)
        if(s in reply.lower() for s in ['yes','continue']):
            continue
        print("Exiting the program...")
        sys.exit(0)

		            
