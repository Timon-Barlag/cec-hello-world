import socket
import os
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    WRITE_TO_LOG = False

    if socket.gethostname().startswith("cec-hello-world"):
        write_path = "/mnt/"
    else:
        write_path = "/home/t/Desktop/tmp/tmp2/"


    hostname = socket.gethostname()

    hello_string = "Hello World! Greetings from " + hostname + "\n"
    #hello_string += "/mnt/ content: " + str(os.listdir("mnt")) + "\n"
    if os.path.exists(write_path):
        hello_string += "<p>" + write_path + " content: " + str(os.listdir(write_path)) + "</p>\n"
    else:
        hello_string += "<p>" + write_path + " not foudn</p>\n"
        hello_string += str(next(os.walk('.'))[1])

    #hello_string += "_________"

    timestamp = time.time()

    if WRITE_TO_LOG:
        with open(write_path + "my_log.log", "a") as file:
            file.write("host: " + hostname + "  time: " + str(timestamp) + "\n")

    if os.path.exists(write_path + "my_log.log"):
        content = ""
        with open(write_path + "my_log.log") as f:
            for line in f:
                #print("test")
                content += line.replace("\n", "") + "<br>\n"	
            #content = f.read()

        hello_string += "<p>content:</p>\n" + content + "<p>end content</p>\n" 

    return hello_string


if __name__ == "__main__":
    application.run()
