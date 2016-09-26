from flask import Flask, render_template
import string, random

app = Flask(__name__)
   
def job_dict():
    s = open("occupations.csv").read().strip().split("\r\n")
    d = dict()
    for line in s:
        key = line.rsplit(",",2)[0]
        key = string.strip(key,'\"') # remove double quotes
    
        value = line.rsplit(",",2)[1]
        d[key] = value
    del d["Job Class"]
    del d["Total"]
    for key in d:
        d[key] = float(d[key])
    return d


def link_dict():
    s = open("occupations.csv").read().strip().split("\r\n")
    d = dict()
    for line in s:
        key = line.rsplit(",",2)[0]
        key = string.strip(key,'\"') # remove double quotes
    
        value = line.rsplit(",",2)[2]
        d[key] = value
    del d["Job Class"]
    del d["Total"]
    return d


@app.route("/")
def intro():
    return '''<meta http-equiv="refresh" content="0; URL='occupations'" />'''

@app.route("/occupations")
def occupations():
    # randomizer
    d = job_dict()
    l = link_dict()
    pickJob = ''
    random_num = random.random()*100
    threshold = 0.0
    for key in d:
        threshold += d[key]
        if random_num < threshold:
            pickJob = key
            break
    if pickJob == '':
        pickJob = "Other"
    
    # render
    return render_template('occupations.html',table = d, links = l, rand = pickJob)

if __name__ == '__main__':
    app.debug = True
    app.run()
