
#!/usr/bin/python3                                                                                                                                                                           
"""Alta3 APIs and HTML"""                                                                                                                                                                    
                                                                                                                                                                                             
## best practice says don't use commas in imports                                                                                                                                            
# use a single line for each import                                                                                                                                                          
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

## This is where we want to redirect users to for success
@app.route("/success/<name>")
def success(name):
    return f"Correct answer! \nToday is {name}\n"

## This is where we want to redirect users to for retry
@app.route("/tryagain")
def tryagain():
    return f"Incorrect answer :( \nTry Again\n"

'''
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("trivia.html") # look for templates/postmaker.html
'''

# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.json:
        answer = request.json  # if naswer was assigned via the POST
        if answer["today"] == "Thursday":
            return redirect("/success", name = answer["today"])
    else:
        return redirect("/tryagain")


'''
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name
'''

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application


