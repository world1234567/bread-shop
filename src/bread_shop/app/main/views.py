#  -*- coding: utf-8 -*-
from app.main import main
from flask import render_template
from app.models import User
from .. import db

@main.route('/')
def index():
    admin = User('admin', 'admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return render_template('main/index.html')