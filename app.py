from flask import Flask, render_template
from utils import occupations

app = Flask(__name__)
   
@app.route("/")
def intro():
    return '''<meta http-equiv="refresh" content="0; URL='occupations'" />'''

@app.route("/occupations/")
def occupations():
    # randomizer
    d = job_dict()
    l = link_dict()
    pickJob = occupations.random_job(d)
    
    # render
    return render_template('occupations.html',table = d, links = l, rand = pickJob)

if __name__ == '__main__':
    app.debug = True
    app.run()
