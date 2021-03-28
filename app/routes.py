from flask import Flask, flash, request, redirect, url_for, render_template
from app import app

@app.route('/')
def index():
    return render_template('lander.html')