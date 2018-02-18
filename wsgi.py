import socket
import os
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    hello_string = "Hello World! Greetings from "+socket.gethostname()+"\n"
    #hello_string += "/mnt/ content: " + str(os.listdir("mnt")) + "\n"
    if os.path.exists("/mnt"):
    	hello_string += "mnt content: " + str(os.listdir("/mnt")) + "\n"
    else:
    	hello_string += "no mnt dir found\n"
    	hello_string += str(next(os.walk('.'))[1])

    hello_string += "_________"

    return hello_string


if __name__ == "__main__":
    application.run()
