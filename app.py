from flask import Flask, render_template, redirect
from utils import occupations

app = Flask(__name__)
   
@app.route("/")
def intro():
    return redirect("/occupations/")

@app.route("/occupations/")
def occ():
    # randomizer
    d = occupations.job_dict()
    l = occupations.link_dict()
    pickJob = occupations.random_job(d)
    
    # render
    return render_template('occupations.html',table = d, links = l, rand = pickJob)

if __name__ == '__main__':
    app.debug = True
    app.run()
