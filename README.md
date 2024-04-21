# Nova - An intelligent virtual assistant 

  Nova is a virtual web voice assistant implemented using ChatGPT 3.5 and Elevenlabs. It creates humanlike responses to your input and reads them out using some of the best AI text generation, voice transcription and text-to-speech technology available. The purpose of the project is to attempt to utilize the new major improvements in artificial intelligence to create a voice assistant that is more adaptive and more capable of humanlike behaviour and responses than voice assistants utilizing older technology. 

# Table of contents

  [Backend](#backend)

  [Frontend](#frontend)

# Backend
## Setup Instructions
### Prerequisites & Dependencies

  - Python >=3.9 
  - For flight info: account on [flightradar24](https://www.flightradar24.com)
  - OpenAI API (you will need an API key from OpenAI) 
  - Elevenlabs API key 
  - Conda or pip (for managing virtual environment) 
  - Node and Yarn 

### Clone the repository:

  - `git clone https://github.com/hamid-nazar/AI-virtual-assistant.git` 
  - `cd AI-virtual-assistant/backend`

### Create a Virtual Environment

  - `conda create --name myenv python=3.x` 
  - `conda activate myenv` 
  - `pip install -r requirements.txt`

### Set Up Your .env file
    
  OPENAI_API_KEY = your_openai_api_key \
  ELEVENLABS_API_KEY = your_elevenlabs_api_key \
  EMAIL = your_flightradar_email \
  PASSWORD = your_flightradar_password 

### Run The Application

    uvicorn main:app --reload

## Backend Structure

  - `main.py`: Defines all the API endpoints that interact with the frontend of the application. 
  - `chatGPT.py`: Sets up the generative AI model with system prompts and functions to respond to input. Also uses OpenAI voice transcription to transcribe audio messages. 
  - `tasks.py`: Additional functions the chatGPT model can call upon via function calling. Descriptions of the functions for the model are found in function_descriptions.py. 
  - `text_to_speech.py`: Converts response from OpenAI to speech using elevenlabs. 
  - `database.py`: Stores messages of current session for the chatbot in JSON format. Also implements function to reset the messages. 
  - `requirements.txt`: Lists all project-specific dependencies.

# Frontend
## Install Dependencies and Run The Application

  If yarn is not installed: `npm install --global yarn`

  - `cd generative-AI/front` 
  - `yarn install` 
  - `yarn run dev`

## Tech Stack

  - React + Vite 
  - Tailwind CSS 
  - Axios 

## Additional Notes
The functionality for the inding the cheapest fligh between tow locations does not work very well due to significant delays in receiving response back from the API. As a result, using this functionality may not be very practical in real-world scenarios.
