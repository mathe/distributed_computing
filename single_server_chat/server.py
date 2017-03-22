from bottle import run, get, post, static_file, error

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Chat:
    def __init__(self):
        self.messages = {}

    def get_messages(self,f,to):
        if f in self.messages and to in self.messages[f]: return self.messages[f][to]
        return ["There is no message from " + f + " to " + to + "."]

    def set_message(self,f,to,msg):
        if f not in self.messages: self.messages[f] = {}
        if to not in self.messages[f]: self.messages[f][to] = []
        self.messages[f][to].append(msg)

@get("/msg_history/<f>/<to>")
def msg_history(f,to):
    global chat

    history = ""
    messages = chat.get_messages(f,to)
    for mi in messages: history += mi + "<br/>"

    return history

@post("/send_msg/<f>/<to>/<msg>")
def send_msg(f,to,msg):
    global chat
    print(f + " " + to + " " + msg)
    chat.set_message(f,to,msg)
    print(f + " " + to + " " + msg)
    return "Message sent!"

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@get("/")
def index():
    return static_file("client.tpl", root=dir_path)

chat = Chat()
run(host="localhost", port=8080, debug = True)
