import os
from flask import Flask, Blueprint, render_template, url_for, request, redirect
from .models import UserInput
from . import db


catalogue = Blueprint('main', __name__)

@catalogue.route('/')
def index():
        return render_template('index.html')

@catalogue.route('/second_page')
def second_page():
        records = UserInput.query.all()
        return render_template('second_page.html', records=records)

@catalogue.route('/save_input', methods=['POST'])
def save_input():
	user_input_content = request.form['user_input']
	if not user_input_content.strip():
		return redirect(url_for('main.index'))
	user_input = UserInput(content=user_input_content)
	db.session.add(user_input)
	db.session.commit()
	return redirect(url_for('main.index'))
