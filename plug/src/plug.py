import sys, os
from PyP100 import PyP100
from dotenv import load_dotenv

load_dotenv()

p100 = PyP100.P100(os.getenv("ADDRESS"), os.getenv("EMAIL",), os.getenv("PASSWORD")) #Creates a P100 plug object
p100.handshake() #Creates the cookies required for further methods
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods
action = sys.argv[1].lower() if len(sys.argv) == 2 else ''

if action == "on":
    p100.turnOn()
elif action == 'off':
    p100.turnOff()
else:
    p100.toggleState()
