import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import openai

class ChatGPTResponse:

    def __init__(self,max_length:int=200,num_return_sequences:int=1):
        # Load pre-trained GPT-2 model and tokenizer
        self.openai = openai
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.max_length = max_length
        self.num_return_sequences = num_return_sequences

    def __interact_gpt3(self,search:str):
        self.openai.api_key = os.getenv("OPENAI_API_KEY") #Please set this env variable with the appropriate open ai key

        response = self.openai.ChatCompletion.create(model="gpt-3.5-turbo", \
                                               messages=[{"role": "user", "content": search}])
    
        return response.choices[0].text.strip()
    
    def __interact_gpt2(self,search:str):
        # Tokenize input prompt
        input_ids = self.tokenizer.encode(search, return_tensors="pt")

        # Generate text based on the input prompt
        output = self.model.generate(input_ids, max_length=self.max_length, \
                                            num_return_sequences=self.num_return_sequences, no_repeat_ngram_size=2)
                
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
    
    def get_response(self,search:str='',gpt_version:str='gpt3'):
        try:
            if(gpt_version=='gpt2'):
                return self.__interact_gpt2(search)
            #For GPT-3 use Open AI API
            return self.__interact_gpt3(search)
        except Exception as e:
            print("Error in chat gpt response")
            print(e)
            raise e     