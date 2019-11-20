from flask import Flask, Blueprint

m2 = Blueprint('module2', __name__)

@m2.route('/new')
def hello():
    return 'Default page Module 2'

@m2.route('/welcome')
def welcome():
    return 'Welcome to module 2'

@m2.route('/sp')
def special():
    return 'Im special'