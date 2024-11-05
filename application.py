# import os
# from flask import Flask, request, Response
# from twilio.twiml.voice_response import VoiceResponse, Gather
# from twilio.rest import Client
# from dotenv import load_dotenv
# load_dotenv()  # Load environment variables from .env file

# app = Flask(__name__)

# # Get Twilio credentials from environment variables
# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)


# @app.route('/make_call', methods=['POST'])
# def make_call():
#     call = client.calls.create(
#         to="+923170700995",  # Replace with the destination phone number
#         from_="+17623272575",
#         url='https://4b7d-2407-d000-a-81ab-355b-13f6-43fa-692f.ngrok-free.app/answer_call'  # Use your ngrok URL here
#     )
#     return f'Call initiated with SID: {call.sid}'


# @app.route('/answer_call', methods=['POST'])
# def answer_call():
#     response = VoiceResponse()
#     gather = Gather(action='/handle_key', method='POST', num_digits=1)
#     gather.say('Press 1 to know about services of Developers Den')
#     gather.say('Press 2 to know about team lead of Developers Den')
#     gather.say('Press 3 to know about the CEO of Developers Den')
#     gather.say('Press 4 to repeat')
#     response.append(gather)
#     response.say('We didn\'t receive any input. Goodbye!')
#     return Response(str(response), mimetype='text/xml')


# @app.route('/handle_key', methods=['POST'])
# def handle_key():
#     digit_pressed = request.form['Digits']
#     response = VoiceResponse()
#     if digit_pressed == '1':
#         response.say('You pressed 1. At Developers Den LLC, we provide services in: Product Engineering, Generative AI, Natural Language Processing (NLP), AI & ML, Intelligent Chatbots, Voicebots, and LLMs.')
#         # Add more logic for option 1 if needed
#     elif digit_pressed == '2':
#         response.say('You pressed 2. Osama Rafique is the team lead of Developers Den.')
#         # Add more logic for option 2 if needed
#     elif digit_pressed == '3':
#         response.say('You pressed 3.  the CEO of Developers Den is Ahmed Riaz.')
#         # Add more logic for option 3 if needed
#     elif digit_pressed == '4':
#         response.redirect('/answer_call')  # Redirect to re-prompt
#     else:
#         response.say('Invalid input. Please press 1, 2, 3, or 4.')
#         response.redirect('/answer_call')  # Redirect to re-prompt
    
#     return Response(str(response), mimetype='text/xml')

# @app.route("/voice", methods=['GET', 'POST'])
# def voice():
#     """Respond to incoming phone calls with a menu of options"""
#     # Start our TwiML response
#     resp = VoiceResponse()

#     # Start our <Gather> verb
#     gather = Gather(num_digits=1)
#     gather.say('For sales, press 1. For support, press 2.')
#     resp.append(gather)

#     # If the user doesn't select an option, redirect them into a loop
#     resp.redirect('/voice')

#     return str(resp)


# if __name__ == '__main__':
#     app.run(debug=True)







# import os
# from flask import Flask, request, jsonify
# from twilio.twiml.voice_response import VoiceResponse, Gather
# from twilio.rest import Client
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# app = Flask(__name__)

# # Get Twilio credentials from environment variables
# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)

# @app.route('/make_call', methods=['POST'])
# def make_call():
#     call = client.calls.create(
#         to="+923170700995",  # Replace with the destination phone number
#         from_="+17623272575",  # Replace with your Twilio phone number
#         url="https://0e8c-2407-d000-a-81ab-355b-13f6-43fa-692f.ngrok-free.app/voice"  # This URL will handle the call instructions
#     )
#     return jsonify({"status": "Call initiated", "call_sid": call.sid})

# @app.route('/voice', methods=['POST'])
# def voice():
#     response = VoiceResponse()
#     gather = Gather(
#         input='speech',
#         timeout=5,  # Listen for 5 seconds
#         action='/handle_gather'  # URL to handle the result of the gather
#     )
#     gather.say("Please state your message after the beep.")
#     response.append(gather)
#     return str(response)

# @app.route('/handle_gather', methods=['POST'])
# def handle_gather():
#     response = VoiceResponse()
#     # Get the gathered input from the form
#     user_speech = request.form.get('SpeechResult', 'No speech detected')
    
#     # Respond with what the user said
#     response.say(f"You said: {user_speech}")
    
#     # End the call
#     response.hangup()
    
#     return str(response)

# if __name__ == '__main__':  
#     app.run(debug=True)











# import os
# from flask import Flask, request, jsonify
# from twilio.twiml.voice_response import VoiceResponse, Gather
# from twilio.rest import Client
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# app = Flask(__name__)

# # Get Twilio credentials from environment variables
# account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
# auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)

# @app.route('/make_call', methods=['POST'])
# def make_call():
#     call = client.calls.create(
#         to="+923170700995",  # Replace with the destination phone number
#         from_="+17623272575",  # Replace with your Twilio phone number
#         url=" https://a245-2402-ad80-fc-9af6-d036-22fc-3bf5-d547.ngrok-free.app/voice"  # Update with your ngrok URL
#     )
#     return jsonify({"status": "Call initiated", "call_sid": call.sid})

# @app.route('/voice', methods=['POST'])
# def voice():
#     response = VoiceResponse()
#     gather = Gather(
#         input='speech',
#         timeout=10,
#         action='/handle_gather'  # URL to handle the result of the gather
#     )
#     gather.say("Please state your message after the beep.")
#     response.append(gather)
#     print(f"VoiceResponse: {response}")
#     return str(response)

# @app.route('/handle_gather', methods=['POST'])
# def handle_gather():
#     response = VoiceResponse()
#     print(f"Request form data: {request.form}")
#     # Get the gathered input from the form
#     user_speech = request.form.get('SpeechResult', 'No speech detected')
    
#     # Respond with what the user said
#     response.say(f"You said: {user_speech}")
    
#     # End the call
#     response.hangup()
#     print(f"User speech: {user_speech}")
#     return str(response)

# if __name__ == '__main__':
#     app.run(debug=True)

# working code 
#---------------------

# import os
# from flask import Flask, request, jsonify
# from twilio.twiml.voice_response import VoiceResponse, Gather
# from twilio.rest import Client
# from dotenv import load_dotenv
# from langchain.llms import OpenAI

# load_dotenv()  # Load environment variables from .env file

# app = Flask(__name__)

# # Get Twilio credentials from environment variables
# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# # Debugging: Print environment variables to ensure they are loaded
# print(f"TWILIO_ACCOUNT_SID: {account_sid}")
# print(f"TWILIO_AUTH_TOKEN: {auth_token}")

# # Initialize Twilio client
# client = Client(account_sid, auth_token)
# api_key = os.getenv("OPENAI_API_KEY")
# llm = OpenAI(openai_api_key=api_key)

# # Define a custom prompt with guidelines for the model
# custom_prompt = """
# You are a helpful assistant providing responses in Indian English. 
# Your task is to generate concise and relevant responses based on the user's input. 
# If the user says 'Goodbye', you should end the conversation. 
# Make sure to stay polite and clear in your responses.
# """

# @app.route('/make_call', methods=['POST'])
# def make_call():
#     try:
#         call = client.calls.create(
#             to="+923170700995",  # Replace with the destination phone number
#             from_="+13346030779",  # Replace with your Twilio phone number
#             url="https://7ed0-39-34-184-21.ngrok-free.app/voice"  # Update with your ngrok URL
#         )
#         return jsonify({"status": "Call initiated", "call_sid": call.sid})
#     except Exception as e:
#         print(f"Error creating call: {e}")
#         return jsonify({"status": "Call initiation failed", "error": str(e)})

# @app.route('/voice', methods=['POST'])
# def voice():
#     response = VoiceResponse()
#     gather = Gather(
#         input='speech',
#         timeout=5,
#         action='/voice',  # URL to handle the result of the gather
#         method='POST',
#         language='en-IN'  # Set the language to English - India
#     )
#     #gather.say("Now Speak my love")
#     response.append(gather)
#     #if session: 

#     return str(response)

# @app.route('/handle_gather', methods=['POST'])
# def handle_gather():
#     user_speech = request.form.get('SpeechResult', 'No speech detected')

#     # Print the user's speech to the console
#     print(f"User speech: {user_speech}")

#     # Normalize the user speech for better matching
#     user_speech_normalized = user_speech.strip().lower()

#     # Check if the user said "Goodbye" exactly or as part of their speech
#     if "goodbye" in user_speech_normalized:
#         response = VoiceResponse()
#         print("Going to end call")
#         response.say("Good bye! Ending the call.")
#         response.hangup()
#     else:
#         # Combine the custom prompt with the user's speech
#         prompt = f"{custom_prompt}\nUser said: {user_speech}\nResponse:"

#         try:
#             response_text = llm(prompt, max_tokens=50).strip()
#             print(f"Model response: {response_text}")  # Debugging: Print the model's response

#             # Ensure the response is within a reasonable length
#             if not response_text:
#                 response_text = "Sorry, I didn't catch that."

#             answer = ' '.join(response_text.split()[:25])  # Ensure the response is within 25 words

#             # Respond with what the user said and continue the conversation
#             response = VoiceResponse()
#             response.say(f"{answer}")  # Ensure response is in English - India
#             response.redirect('/voice')  # Redirect to the same URL to repeat the gather

#         except Exception as e:
#             print(f"Error: {e}")
#             response = VoiceResponse()
#             response.say("Sorry, there was an error processing your request. Please try again.", language='en-IN')
#             response.redirect('/voice')

#     return str(response)

# if __name__ == "__main__":
#     app.run(debug=True)


# last working code 
#------------------------------------
import os
import uuid
from flask import Flask, request, jsonify, session
from flask_session import Session
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.rest import Client
from dotenv import load_dotenv
from langchain.llms import OpenAI

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Flask session
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the file system
Session(app)  # Initialize the session

# Get Twilio credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Initialize Twilio client
client = Client(account_sid, auth_token)
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=api_key)

# Define a custom prompt with guidelines for the model
custom_prompt = """
You are a helpful assistant providing responses in Indian English. 
Your task is to generate concise and relevant responses based on the user's input. 
If the user says 'Goodbye', you should end the conversation. 
Make sure to stay polite and clear in your responses.
"""

def save_session_to_file(session_id, conversation):
    """Save session data to a text file."""
    file_path = f"session_{session_id}.txt"
    with open(file_path, 'a') as f:
        for message in conversation:
            if 'user' in message:
                f.write(f"User: {message['user']}\n")
            if 'assistant' in message:
                f.write(f"Assistant: {message['assistant']}\n")
        f.write("\n")  # Add a newline after each conversation exchange

@app.route('/make_call', methods=['POST'])
def make_call():
    try:
        call = client.calls.create(
            to="+923170700995",  # Replace with the destination phone number
            from_="+13346030779",  # Replace with your Twilio phone number
            url="https://7ed0-39-34-184-21.ngrok-free.app/voice"  # Update with your ngrok URL
        )
        return jsonify({"status": "Call initiated", "call_sid": call.sid})
    except Exception as e:
        print(f"Error creating call: {e}")
        return jsonify({"status": "Call initiation failed", "error": str(e)})

@app.route('/voice', methods=['POST'])
def voice():
    response = VoiceResponse()

    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
        session['conversation'] = []

        # Initial greeting message
        initial_message = "Hi, how can I help you today?"
        response.say(initial_message, language='en-IN')

        # Store the initial greeting message in conversation history
        session['conversation'].append({'assistant': initial_message})

        # Gather user input
        gather = Gather(
            input='speech',
            timeout=10,  # Wait for 10 seconds for speech input
            speechTimeout='auto',  # End gathering automatically after a pause
            action='/voice',  # Handle gathered input in the same route
            method='POST',
            language='en-IN'
        )
        response.append(gather)
        response.say("Please say something after the beep.", language='en-IN')

    else:
        user_speech = request.form.get('SpeechResult', 'No speech detected')

        # Print the user's speech to the console
        print(f"User speech: {user_speech}")

        # Normalize the user speech for better matching
        user_speech_normalized = user_speech.strip().lower()

        # Store user speech in conversation history
        session['conversation'].append({'user': user_speech})

        # Check if the user said "Goodbye" exactly or as part of their speech
        if "goodbye" in user_speech_normalized:
            print("Ending the call.")
            response.say("Goodbye! Ending the call.")

            # Store assistant's "Goodbye" in conversation history
            session['conversation'].append({'assistant': "Goodbye! Ending the call."})
            response.hangup()
        else:
            # Combine the custom prompt with the user's speech
            prompt = f"{custom_prompt}\nUser said: {user_speech}\nResponse:"

            try:
                response_text = llm(prompt, max_tokens=500).strip()
                print(f"Model response: {response_text}")

                # Ensure the response is within a reasonable length
                if not response_text:
                    response_text = "Sorry, I didn't catch that."

                answer = ' '.join(response_text.split()[:200])  # Ensure the response is within 25 words

                # Store assistant's response in conversation history
                session['conversation'].append({'assistant': answer})

                # Respond with the assistant's answer and continue the conversation
                response.say(answer, language='en-IN')

                # Gather user input again
                gather = Gather(
                    input='speech',
                    timeout=10,  # Wait for 10 seconds for speech input
                    speechTimeout='auto',  # End gathering automatically after a pause
                    action='/voice',  # Handle gathered input in the same route
                    method='POST',
                    language='en-IN'
                )
                response.append(gather)
                response.say("Please say something after the beep.", language='en-IN')

            except Exception as e:
                print(f"Error: {e}")
                response.say("Sorry, there was an error processing your request. Please try again.", language='en-IN')

                # Gather user input again
                gather = Gather(
                    input='speech',
                    timeout=10,  # Wait for 10 seconds for speech input
                    speechTimeout='auto',  # End gathering automatically after a pause
                    action='/voice',  # Handle gathered input in the same route
                    method='POST',
                    language='en-IN'
                )
                response.append(gather)
                response.say("Please say something after the beep.", language='en-IN')

    # Save session data to a file
    save_session_to_file(session['session_id'], session['conversation'])

    # Print session data to the console for debugging
    print(f"Session data: {session}")

    return str(response)

@app.route('/get_session', methods=['GET'])
def get_session():
    # Return the session data as JSON
    session_data = {
        'session_id': session.get('session_id'),
        'conversation': session.get('conversation')
    }
    return jsonify(session_data)


if __name__ == "__main__":
    app.run(debug=True)





#------------------------------------


#--------------------------------


#-----232




# import os
# from flask import Flask, render_template, jsonify, request
# from flask_sock import Sock
# from twilio.rest import Client
# from twilio.twiml.voice_response import VoiceResponse, Gather
# from dotenv import load_dotenv
# from langchain.llms import OpenAI

# # Load environment variables from .env file
# load_dotenv()

# # Initialize Flask app
# app = Flask(__name__)
# sock = Sock(app)

# # Dictionary to keep track of WebSocket connections
# connections = {}

# # Get Twilio credentials from environment variables
# account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# client = Client(account_sid, auth_token)

# # Initialize OpenAI client using langchain
# api_key = os.getenv("OPENAI_API_KEY")
# llm = OpenAI(openai_api_key=api_key)

# # Define a custom prompt for the language model
# custom_prompt = """
# You are a helpful assistant providing responses in Indian English. 
# Your task is to generate concise and relevant responses based on the user's input. 
# If the user says 'Goodbye', you should end the conversation. 
# Make sure to stay polite and clear in your responses.
# """

# @app.route('/')
# def index():
#     return render_template('index.html')

# @sock.route('/call')
# def call(ws):
#     connections['default'] = ws
#     while True:
#         message = ws.receive()
#         if message == 'Initiate Call':
#             try:
#                 call = client.calls.create(
#                     to="+923170700995",  # Replace with the destination phone number
#                     from_="+18108888997",  # Replace with your Twilio phone number
#                     url="https://c06e-39-34-173-202.ngrok-free.app/voice"  # Update with your ngrok URL
#                 )
#                 ws.send(f"Call initiated with SID: {call.sid}")
#             except Exception as e:
#                 ws.send(f"Error creating call: {str(e)}")
#         else:
#             ws.send("Unknown command")

# @app.route('/voice', methods=['POST'])
# def voice():
#     response = VoiceResponse()
#     gather = Gather(
#         input='speech',
#         timeout=5,
#         action='/handle_gather',  # URL to handle the result of the gather
#         method='POST',
#         language='en-IN'  # Set the language to English - India
#     )
#     response.append(gather)
#     response.say("Please say something.")
#     return str(response)

# @app.route('/handle_gather', methods=['POST'])
# def handle_gather():
#     user_speech = request.form.get('SpeechResult', 'No speech detected')
#     print(f"User speech: {user_speech}")  # Debugging: Log the user input

#     user_speech_normalized = user_speech.strip().lower()
#     response = VoiceResponse()

#     if "goodbye" in user_speech_normalized:
#         response.say("Goodbye! Ending the call.")
#         response.hangup()
#         # Notify WebSocket client
#         if 'default' in connections:
#             connections['default'].send(f"User: {user_speech}")
#             connections['default'].send("AI: Goodbye! Ending the call.")
#     else:
#         prompt = f"{custom_prompt}\nUser said: {user_speech}\nResponse:"

#         try:
#             response_text = llm(prompt, max_tokens=50).strip()
#             print(f"Model response: {response_text}")  # Debugging: Log the model's response

#             if not response_text:
#                 response_text = "Sorry, I didn't catch that."

#             answer = ' '.join(response_text.split()[:25])

#             response.say(answer)
#             response.redirect('/voice')

#             # Notify WebSocket client with both user and AI messages
#             if 'default' in connections:
#                 connections['default'].send(f"User: {user_speech}")
#                 connections['default'].send(f"AI: {answer}")

#         except Exception as e:
#             print(f"Error processing request: {e}")  # Debugging: Log any errors
#             response.say("Sorry, there was an error processing your request. Please try again.", language='en-IN')
#             response.redirect('/voice')

#             # Notify WebSocket client about the error
#             if 'default' in connections:
#                 connections['default'].send(f"User: {user_speech}")
#                 connections['default'].send("AI: Sorry, there was an error processing your request.")

#     return str(response)

# if __name__ == "__main__":
#     app.run(debug=True)
