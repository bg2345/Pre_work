from app import app
from flask import render_template, url_for, redirect
from app.forms import ContactForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET'])
def contact():
    form = ContactForm()


    return render_template('contact.html', title='Contact', form=form)
