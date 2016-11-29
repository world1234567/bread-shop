#  -*- coding: utf-8 -*-
from . import main
from flask import render_template
from app.database import db_session
from app.models import User



@main.route('/')
def index():
    admin = User('admin', 'admin@example.com')
    db_session.add(admin)
    db_session.commit()
    return render_template('main/index.html')