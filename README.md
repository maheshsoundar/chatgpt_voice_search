Use voice commands to searcth for responses from GPT-2 or GPT-3. For learning and educational purposes only. 
1. Set up virtual env from root directory using python -m venv .venv. Then activate venv by running the activate.bat file in .venv/Scripts.
2. Run pip install -r requirements.txt and make sure all dependencies are installed in .venv/Scripts folder. 
3. Run speech_to_search.py using "python speech_to_search.py" from a terminal (root directory)
4. The search is sent to GPT3 API which returns a response. If needed the response argument can be set to "gpt2" to use the pretrained gpt2 modelinsteadof the API.
5. For use of API, please create a personal key by logging into openai and setting the key as an env variable ("OPENAI_API_KEY").
