import socket
import os
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    WRITE_TO_LOG = True       #specify whether or not to write to log file

    hostname = socket.gethostname()

    write_path = "/mnt/"

    hello_string = "Hello World! Greetings from " + hostname + "\n"


    #write content of write_path directory if it exists and list contents of current directory otherwise 
    if os.path.exists(write_path):
        hello_string += "<p>" + write_path + " content: " + str(os.listdir(write_path)) + "</p>\n"
    else:
        hello_string += "<p>" + write_path + " not found</p>\n"
        hello_string += str(next(os.walk('.'))[1])

    timestamp = time.ctime(time.time())


    #write to log if specified
    if WRITE_TO_LOG:
        with open(write_path + "my_log.log", "a") as file:
            file.write("host: " + hostname + "  time: " + str(timestamp) + "\n")

    #read from log if the file exists
    if os.path.exists(write_path + "my_log.log"):
        content = ""
        with open(write_path + "my_log.log") as f:
            for line in f:
                content += line.replace("\n", "") + "<br>\n"

        hello_string += "<p>my_log.log content:</p>\n" + content 
    else:
        hello_string += "<p>logfile not found</p>\n"

    return hello_string


if __name__ == "__main__":
    application.run()
