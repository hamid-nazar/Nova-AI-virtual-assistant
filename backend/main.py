
# uvicorn main:app --reload

# Mai imports
from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, Response
from fastapi.middleware.cors import CORSMiddleware  
# from decouple import config
import openai
import playsound
import shutil

# Custom functions imports
from functions.chatGPT import convert_speech_to_text, chat
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

# Initialize FastAPI
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://localhost:3000",
]



# CORS - Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/audio")
async def post_audio(file: UploadFile = File(...)):
    
    # audio_input = open("./voice.mp3","rb")
    
    
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    
    audio_input = open(file.filename, "rb") 
    
    request_message = convert_speech_to_text(audio_input)
    
    print(request_message)
    
    if not request_message:
        raise HTTPException(status_code=404, detail="Could not convert audio to text")
    
   
        
    # response_message = get_chat_response(request_message)
    
    response_message = chat(request_message)
    
    if not request_message:
        raise HTTPException(status_code=404, detail="Could not get response from chatGPT")
        
    store_messages(request_message, response_message)
        
    print(response_message)
    
    audio_output = convert_text_to_speech(response_message)
    
    if not audio_output:
        raise HTTPException(status_code=404, detail="Elvenlabs could not convert text to audio")
    

    def generate():
        yield audio_output
        
        
    return StreamingResponse(generate(), media_type="application/octet-stream")
   
   
@app.get("/reset")
async def reset_conversation():
    
    reset_messages()
    
    return Response(status_code=200)
    



