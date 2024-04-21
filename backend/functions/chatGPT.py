import openai
import dotenv
import os
import json
import datetime
from functions.tasks import get_local_time, get_flight_info , get_weather_info
from functions.database import get_recent_messages
from functions.functions_descriptions import descriptions

dotenv.load_dotenv()



# openai.api_key = os.getenv("OPENAI_API_KEY")

openai_client = openai.OpenAI()
openai.api_key = os.getenv("OPENAI_API_KEY")



def convert_speech_to_text(audio_file):
  try:
    
    transcript = openai_client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file)

    message_text = transcript.text
    
    
    print(transcript)
  
    return message_text
  
  except Exception as e:
    print(e)
    return



def get_chat_response(message):
  
  messages = get_recent_messages()
  user_masege = {"role": "user", "content": message}
  messages.append(user_masege)
  
  print(messages)
  
  try:
    
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages)
    
    message_text = response["choices"][0]["message"]["content"]
    
    return message_text
    
  except Exception as e:
    print(e)
    return
  
  
  
  
# alternative
  



def chat(message):
    #model="gpt-3.5-turbo-0613",
    messages = get_recent_messages()
    
    messages.append({"role": "user", "content": message})
    
    response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    tools=descriptions,
    tool_choice="auto",)

    print(response)
    
    output = response.choices[0].message
    
    print(output)
    
    if output.tool_calls:
        function_to_call = output.tool_calls[0]
        function_name = function_to_call.function.name
        
        if function_name == "get_local_time":
          
          print("GPT: called function ", function_name)
        
            
          chosen_function = eval(function_name)
            
            
          time = chosen_function()
          
          
          messages.append({"role": "function", "name": function_name, "content": time})
        
    
          response = fix_format(messages)
            
          return response
          
        elif function_name == "get_flight_info":
          
          print("GPT: called function " + function_name)
          
          origin = json.loads(output.tool_calls[0].function.arguments).get("origin")
          destination = json.loads(output.tool_calls[0].function.arguments).get("destination")
          
          chosen_function = eval(function_name)
          
          cheapest_flight = chosen_function(origin, destination)
          
          messages.append({"role": "function", "name": function_name, "content": cheapest_flight})
          
          response = fix_format(messages)
          
          return response
        
        elif function_name == "get_cheapest_flight":
          
          print("GPT: called function " + function_name)
          
          origin = json.loads(output.tool_calls[0].function.arguments).get("origin")
          destination = json.loads(output.tool_calls[0].function.arguments).get("destination")
          
          chosen_function = eval(function_name)
          
          cheapest_flight = chosen_function(origin, destination)
          
          messages.append({"role": "function", "name": function_name, "content": cheapest_flight})
          
          response = fix_format(messages)
          
          return response
           
        elif function_name == "get_weather_info":
          
          print("GPT: called function " + function_name)
          
          city = json.loads(output.tool_calls[0].function.arguments).get("city")
          
          chosen_function = eval(function_name)
          
          weather = chosen_function(city)
          
          messages.append({"role": "function", "name": function_name, "content": weather})
          
          response = fix_format(messages)
          
          return response
        
        
    else:
        print("Function does not exist")
        print("GPT: " + response.choices[0].message.content)
        
        return response.choices[0].message.content
      
      
      
      

def fix_format(messages):

    response = openai_client.chat.completions.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    tools=descriptions,
    tool_choice="auto",)
            
    response = response.choices[0].message.content
    print("GPT: " + response)
    
    return response


  
  
  