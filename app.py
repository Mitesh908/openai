import os
from flask import Flask, render_template, request
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# print(openai.api_key)

#set up Flask app
app = Flask(__name__)

#Define the home page route
@app.route("/")
def home():
    return render_template("index.html")


#Define the chatbot route
@app.route("/chatbot",methods=["POST"])
def chatbot():
    # pass
    #Get the message input form the user
    user_input = request.form["message"]
    #use the openia api to generate a response
    prompt = f"User: {user_input}\nChatbot: "
    chat_history = []
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_token=60,
        top_p=1,
        frequnecy_penalty=0,
        stop=["\nUser: ", "\nChatbot: "]

    )

    #Extract the response text from the oopenai api result
    bot_response =response.choices[0].text.strip()

    #add the user input and bot reponse to the chat history
    chat_history.append(f"User: {user_input}\nChatbot: {bot_response}")

    #Rendetr the chtabot templates with the response text
    return render_template(
        "chatbot.html",
        user_input=user_input,
        bot_response=bot_response,
        
    )

#start the flask app
if __name__ ==" _main_":
    app.run(debug=True)


