from flask_app import app
from flask_app.models.email_model import Email
from flask import render_template, redirect, request

@app.route('/')
def home():
    emails = Email.read_all()
    return render_template('index.html', emails=emails)

@app.route('/insert', methods=['POST'])
def insert_email():
    if not Email.validate_email(request.form['email']):
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    Email.insert(data)
    return redirect('/success')

@app.route('/success')
def success():
    emails = Email.read_all()
    return render_template('success.html', emails=emails)