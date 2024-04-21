import dotenv
import requests
import os
import playsound

dotenv.load_dotenv()


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")


def convert_text_to_speech(message):
    
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
        }
    
    voice_adam = "pNInz6obpgDQGcFmaJgB" 
    rashid = "E7oTDx0NfVneOdjFNIn7"
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"
    maya = "DQjb7khvAR0aCV9IJXD5"
    
    headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": ELEVENLABS_API_KEY }
    
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"
    
    try:
        
        response = requests.post(url, json=body, headers=headers)
        
    except Exception as e:
        
        print(e)
        
    if response.status_code == 200:
        print("Success!")
        
        return response.content
    
    else:
        return     
    
    
    
    
if __name__ == "__main__":
    convert_text_to_speech("Hello, Hamid! How can I assist you today?")
    