from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
#global var over web application ie shared ar across different users

@app.route("/", methods=["POST","GET"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
#this makes user specific 
    if request.method=="POST":
        note = request.form.get("Note")
        session["notes"].append(note)
    
    return render_template("index.html",notes=session["notes"])