"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""


from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request
import csv


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


#This decorator maps the application's home page to the RunOne() function.It runs the function once the application is run
@app.route('/')

def RunOne():

    return '''<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>    
    <meta charset="utf-8" />    
    <title>Postcode Webservice</title>    
</head>

<body>       
    <form action="/link/" method="POST">
        Enter postcode here:
        <input type="text" name="text" class="textBox" /><br />
        <input type="submit" value="Submit" class="submitButton" /><br />
    </form>     
</body>

</html>'''


#This decorator maps the application's /link page to RunTwo() function.It runs the function once the from submitted 
@app.route('/link/', methods=['POST'])

def RunTwo():
    Val=request.form['text']
    with open("CanadaPostalCode.xlsx", "r") as f:
       csvLines = list(csv.reader(f))
       for num, line in enumerate(csvLines):
           if Val in line:
               return str(line)

   
#This block is system configuration 
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)