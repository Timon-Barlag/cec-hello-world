import socket
import os
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    hostname = socket.gethostname()

    hello_string = "Hello World! Greetings from " + hostname + "\n"
    #hello_string += "/mnt/ content: " + str(os.listdir("mnt")) + "\n"
    if os.path.exists("/mnt"):
    	hello_string += "mnt content: " + str(os.listdir("/mnt")) + "\n"
    else:
    	hello_string += "no mnt dir found\n"
    	hello_string += str(next(os.walk('.'))[1])

    #hello_string += "_________"

    timestamp = time.time()

    #file = open("/mnt/my_log.log", "w")
    #file.write("host: ",hostname, "time: ",timestamp)

    with open("/mnt/my_log.log") as f:
    	content = f.read()

    hello_string += " conent:_" + content + "_end content" 

    return hello_string


if __name__ == "__main__":
    application.run()
