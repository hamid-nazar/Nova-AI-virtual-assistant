import json
import random



def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"
  
  # learn_instruction = {"role": "system", 
  #                      "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior position. Your name is Adam. The user is called Hamid. Keep responses under 30 words. "}
  
  # learn_instruction = {"role": "system",
  #                      "content": "You are a helpful and versatile assistant. Your name is Nova.The user is called Hamid. Keep responses under 30 words. "}
  # # Initialize messages
  # messages = []

  # Add Random Element
  x = random.uniform(0, 1)
  # if x < 0.5:
  #   learn_instruction["content"] = learn_instruction["content"] + " Your response will have some light humour. "
  # else:
  #   learn_instruction["content"] = learn_instruction["content"] + " Your response will have some sarcastic humour. "


  # # Append instruction to message
  # messages.append(learn_instruction)
  
  
  instruction = {"role": "system", "content": "You are a voice controlled assistant.Your name is Nova. If the question requires a longer answer, ask the user first if they would like to know more. After confirmation, you can provide a full answer. "}
  
  messages = []
  
  if x < 0.5:
    instruction["content"] = instruction["content"] + " Your response will have some light humour. "
  
  messages.append(instruction)

  
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 10:
          for item in data:
            messages.append(item)
        else:
          for item in data[-10:]:
            messages.append(item)
  except:
    pass
  
  return messages

  
  
def store_messages(request_message, response_message):
    
     file_name = "stored_data.json"
     
     messages = get_recent_messages()[1:]
     
     user_message = {"role": "user", "content": request_message}
     assistant_message = {"role": "assistant", "content": response_message}
     
     messages.append(user_message)
     messages.append(assistant_message)
     
     with open(file_name, 'w') as user_file:
        json.dump(messages, user_file )


def reset_messages():
    
    file_name = "stored_data.json"
    
    with open(file_name, 'w') as user_file:
        json.dump([], user_file )
