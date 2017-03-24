from bottle import run, request, get, post, static_file, view, error

import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Chat:
    def __init__(self):
        self.messages = {}

    def get_messages(self,f,to):
        if f in self.messages and to in self.messages[f]: return self.messages[f][to]        
        return []

    def set_message(self,f,to,msg):
        if f not in self.messages: self.messages[f] = {}
        if to not in self.messages[f]: self.messages[f][to] = []
        self.messages[f][to].append(msg)

@get("/msg_history")
def msg_history():
    global chat
    src = request.query.src
    dest = request.query.dest
    messages = chat.get_messages(src,dest)
    if len(messages):        
        msg = "Messages sent from " + src + " to " + dest + ":"
        return render_index(msg,messages)
    msg = "There is no message from " + src + " to " + dest + "."
    return render_index(msg)

@post("/send_msg")
def send_msg():
    global chat
    f = request.forms.get("from")
    to = request.forms.get("to")
    msg = request.forms.get("message")        
    chat.set_message(f,to,msg)    
    return render_index("Message Sent!")

@error(404)
def error404(error):
    return "Nothing here, sorry."

@view("client")
def render_index(title = "",history = []):
    return dict(title = title,history = history)

@get("/")
def index():
    return render_index("Hi, use our chat!")

chat = Chat()
run(host="localhost", port=8080, debug = True)