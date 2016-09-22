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
    return d

def random_job():
    copy = job_dict()
    del copy["Job Class"]
    del copy["Total"]
    for key in copy:
        copy[key] = float(copy[key])    
    random_num = random.random()*100
    threshold = 0.0
    for key in copy:
        threshold += copy[key]
        if random_num < threshold:
            return key
    return "Other"


@app.route("/")
def intro():
    return "Donde esta la bibllioteca?"

@app.route("/occupations")
def occupations():
    job_dict = job_dict()
    random_job = random_job()
    return render_template('occupations.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
