from iebank_api import db
from datetime import datetime
import string, random
from sqlalchemy import func

# add country field to the account model
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    account_number = db.Column(db.String(20), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default = 0.0)
    currency = db.Column(db.String(1), nullable=False, default="€")
    country = db.Column(db.String(32),nullable=False, default="Spain")
    status = db.Column(db.String(10), nullable=False, default="Active")
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return '<Event %r>' % self.account_number

    def __init__(self, name, currency, country):
        self.name = name
        self.account_number = ''.join(random.choices(string.digits, k=20))
        self.currency = currency
        self.balance = 0.0
        self.status = "Active"
        self.country = country.capitalize() # Capitalize the country name