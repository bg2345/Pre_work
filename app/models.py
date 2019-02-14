from app import app, db

class SubmitContact(db.Model):
    contact_num = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(100))
    message = db.Column(db.String(200))
