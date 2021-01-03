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
        jobExist = db.get[word]
        if jobExist:
            jobs = jobExist
        else:
            jobs = give_me_job(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template(
        'report.html', keyword=word, resultNum=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.capitalize()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        return f"'{word}' 다운로드"
    except:
        return redirect("/")

app.run(host='0.0.0.0')