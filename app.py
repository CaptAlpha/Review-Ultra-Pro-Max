#Flask App
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
from flask import make_response
from sqlalchemy import create_engine

app = Flask(__name__)

#First Page Render - Home Page
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    #Request for link from index.html
    if request.method == 'POST':
        link = request.form['link']
    return render_template('home.html', link=link)


