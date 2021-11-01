from dotenv import load_dotenv
load_dotenv()
import os
password = os.getenv('PASSWORD')
print(password)
# The chunk of code here will be publushed but the file (.env) will contain a series of key value pairs that we
#  dont want to be published at all, so we add passwords, keys and connection strings into this file (.env).

# Now How to manage our keys, passwords ...etc on a web app or whatever that we have deployed it into a server or web server
# such as Azure .
# In Azure when you deployed your app, you can go for the web service and go to configuration and you will see key value pairs the names are displayed 
# but the values are hidden.

