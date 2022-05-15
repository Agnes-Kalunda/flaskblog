from flask import Flask,render_template , url_for,request,redirect
from . import main
from flask_login import login_required,current_user
# import forms
# import models
@main.route('/')
def home():

    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html',title='About')