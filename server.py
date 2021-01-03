from flask import Flask, render_template, request, redirect
from keywordScrapping import give_me_job

app = Flask("BugBug")

db = {}


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/report")
def report():
    word = request.args.get('word').strip()
    if word != '':
        word = word.capitalize()
        fromDb = db.get[word]
        if fromDb:
            jobs = fromDb
        else:
            jobs = give_me_job(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template('report.html', keyword=word, resultNum = len(jobs))


app.run(host='0.0.0.0')
