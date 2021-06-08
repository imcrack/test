from flask import Flask, render_template, request
import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__)
english_bot= ChatBot("Chatterbot")
trainer=ChatterBotCorpusTrainer(english_bot)
trainer.train('chatterbot.corpus.english')
trainer.train("data/data.yml")
trainer.train("data/data1.yml")
trainer.train("data/data2.yml")
trainer.train("data/data3.yml")
text=print('reminder about your training')
local_time=172800*60
time.sleep(local_time)
print(text)


@app.route("/")
def index():
    return render_template('index.html') #send context to html file

@app.route("/get")
def get_bot_response():
    userText=request.args.get("msg") #get data from input, we write js to index.html
    return str(english_bot.get_response(userText))

if __name__=='__main__':
    app.run(debug=True)