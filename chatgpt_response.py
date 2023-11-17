import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import openai

class ChatGPTResponse:

    def __init__(self,max_length:int=200,num_return_sequences:int=1):
        # Load pre-trained GPT-2 model and tokenizer
        self.openai_client = self.__get_openai_client()
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.max_length = max_length
        self.num_return_sequences = num_return_sequences

    def __get_openai_client(self):
        return openai.OpenAI()  #Please set the env variable "OPENAI_API_KEY" with the appropriate open ai key
    
    def __interact_gpt3(self,search:str):
        messages = [ {"role": "user", "content":search} ] 

        response = self.openai_client.chat.completions.create(model="gpt-3.5-turbo", \
                                               messages=messages)
    
        return response.choices[0].message.content
    
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