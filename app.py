from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('indexn.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty/faculty.html')

@app.route('/about-cse')
def about_cse():
    return render_template('about/about-cse.html')

@app.route('/about-aisat')
def about_aisat():
    return render_template('about/about-aisat.html')

@app.route('/academics')
def academics():
    return render_template('academics/academics.html')

@app.route('/library')
def library():
    return render_template('library/library.html')


if __name__=="__main__":
    app.run(debug=True)