from flask import Flask, Blueprint

m1 = Blueprint('module1', __name__, url_prefix='/m1')

@m1.route('/mm')
def hello():
    return 'Default page Module 1'

@m1.route('/welcome')
def welcome():
    return 'Welcome to module 1'