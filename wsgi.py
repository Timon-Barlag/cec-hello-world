import socket
import os
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    if socket.gethostname().startswith("cec-hello-world"):
        write_path = "/mnt/"
    else:
        write_path = "/home/t/Desktop/tmp/tmp2/"


    hostname = socket.gethostname()

    hello_string = "Hello World! Greetings from " + hostname + "\n"
    #hello_string += "/mnt/ content: " + str(os.listdir("mnt")) + "\n"
    if os.path.exists(write_path):
        hello_string += "<p>dir content: " + str(os.listdir(write_path)) + "</p>\n"
    else:
        hello_string += "<p>dir not found</p>\n"
        hello_string += str(next(os.walk('.'))[1])

    #hello_string += "_________"

    timestamp = time.time()

    #file = open("/mnt/my_log.log", "w")
    #file.write("host: ",hostname, "time: ",timestamp)
    if os.path.exists(write_path + "my_log.log"):
        with open(write_path + "my_log.log") as f:
            content = ""
            for line in f:
                content += "<p>" + line + "</p>\n"
            #content = f.read()

        hello_string += " content:_" + content + "_end content" 

    return hello_string


if __name__ == "__main__":
    application.run()
