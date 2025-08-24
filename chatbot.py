# Step 2: Import libraries and download your model
# From the transformers library, we will use the pipeline class to download our model
from transformers import pipeline

# The pipeline class will manage the model for us
# We will use the 'EleutherAI/gpt-neo-125m' model for this project
# This will download the model to your local machine (1-2 minutes)
chatbot = pipeline('text-generation', model='EleutherAI/gpt-neo-125m')

# Step 3: Create a loop to talk to your chatbot
# This loop will allow you to have a continuous conversation
while True:
    try:
        # Prompt the user for input and save it in the variable 'prompt'
        prompt = input('You: ')
        # Use the pipeline to generate a response
        res = chatbot(prompt, max_length=50)
        # Print the response from the chatbot
        print('Chatbot: ' + res[0]['generated_text'])
    except KeyboardInterrupt:
        # Exit the loop if the user presses Ctrl+C
        break