from flask import Flask, render_template, session, redirect, request
from survey_app import app
from survey_app.models.survey import Survey


@app.route('/', methods=['GET'])
def index():
    print(session)
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def route():
    print (request.form)
    # session['fullname'] = request.form['fullname']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['comment'] = request.form['comment']
    # if 'rating' in request.form:
    #     session['rating'] = request.form['rating']
    # if 'reason1' in request.form:
    #     session['reason1'] = request.form['reason1']
    # if 'reason2' in request.form:
    #     session['reason2'] = request.form['reason2']
    # if 'reason3' in request.form:
    #     session['reason3'] = request.form['reason3']
    # print (session)
    data = request.form
    if not Survey.validate_survey(data):
        return redirect ('/')
    newsubmission = Survey.savingform(data)
    redirecturl = f'/results/{newsubmission}'
    return redirect(redirecturl)

@app.route('/results/<int:id>', methods=['GET'])
def resultpage(id):
    information = Survey.getsubmission(id)
    return render_template('results.html', submission = information[0])

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect('/')