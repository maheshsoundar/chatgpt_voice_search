from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatGPTResponse:

    def __init__(self,max_length:int=200,num_return_sequences:int=1):
        # Load pre-trained GPT-2 model and tokenizer
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.max_length = max_length
        self.num_return_sequences = num_return_sequences

    def get_response(self,search:str=''):
        try:
            # Tokenize input prompt
            input_ids = self.tokenizer.encode(search, return_tensors="pt")

            # Generate text based on the input prompt
            output = self.model.generate(input_ids, max_length=self.max_length, \
                                         num_return_sequences=self.num_return_sequences, no_repeat_ngram_size=2)
            
            return self.tokenizer.decode(output[0], skip_special_tokens=True)
        except Exception as e:
            print("Error in chat gpt response")
            print(e)
            raise e     