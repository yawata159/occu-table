from flask import Flask, render_template
import string, random

app = Flask(__name__)
   
def job_dict():
    s = open("occupations.csv").read().strip().split("\r\n")
    d = dict()
    for line in s:
        key = line.rsplit(",",1)[0]
        key = string.strip(key,'\"') # remove double quotes
    
        value = line.rsplit(",",1)[1]
        d[key] = value
    del d["Job Class"]
    return d

@app.route("/")
def intro():
    return "Donde esta la bibllioteca?"

@app.route("/occupations")
def occupations():
    return render_template('occupations.html', table = job_dict())

if __name__ == '__main__':
    app.debug = True
    app.run()
