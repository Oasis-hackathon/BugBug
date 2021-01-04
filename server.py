from flask import Flask, render_template, request, redirect
from bugbugScrapper import give_me_job

app = Flask("BugBug")

@app.route("/")
def home():
  return render_template('home2.html')

@app.route("/report")
def report():
  render_template('loading.html')
  word = request.args.get('word').strip()
  if word != '':
    word = word.capitalize()
    jobs = give_me_job(word)
  else:
    return redirect('/')
  return render_template('report2.html', keyword=word, jobs=jobs, resultNum=len(jobs))

app.run(host='0.0.0.0')