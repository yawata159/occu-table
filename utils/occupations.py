import string, random

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

def random_job(d):
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
