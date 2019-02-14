from app import app, db
from flask import render_template, url_for, redirect
from app.forms import ContactForm
from app.models import SubmitContact

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        message = form.message.data
        submit_to_db = SubmitContact(name=name, phone=phone, email=email, message=message)

        db.session.add(submit_to_db)
        db.session.commit()

        return redirect(url_for('contact'))

    contacts = SubmitContact.query.all()


    return render_template('contact.html', title='Contact', form=form, contacts=contacts)
