import socket
import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
	hello_string = "Hello World! Greetings from "+socket.gethostname()+"\n"
	hello_string += "/mnt/ content: " + os.listdir("mnt")
    return hello_string


if __name__ == "__main__":
    application.run()