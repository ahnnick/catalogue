import os
import requests
from flask import Flask, Blueprint, render_template, url_for, request, redirect, flash, current_app
from .models import Book
from . import db


catalogue = Blueprint('main', __name__)

@catalogue.route('/')
def index():
        return render_template('index.html')

@catalogue.route('/second_page')
def second_page():
        records = Book.query.all()
        return render_template('second_page.html', records=records)

@catalogue.route('/save_input', methods=['POST'])
def save_input():
	user_input_content = request.form['user_input']
	if not user_input_content.strip():
		return redirect(url_for('main.index'))
	user_input = Book(content=user_input_content)
	db.session.add(user_input)
	db.session.commit()
	return redirect(url_for('main.index'))

@catalogue.route('/add_book', methods=['GET', 'POST'])
def add_book():
    print("add_book route called")  # Debug print statement
    if request.method == 'POST':
        print("POST request received")  # Debug print statement
        isbn = request.form['isbn']
        print(f"Received ISBN: {isbn}")  # Debug print statement
        api_key = current_app.config['GOOGLE_BOOKS_API_KEY']
        url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}'
        #  print(f"URL: {url}")  # Debug print statement
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")  # Debug print statement

        if response.status_code == 200:
            book_data = response.json()

            if 'items' in book_data:
                book_info = book_data['items'][0]['volumeInfo']
                title = book_info.get('title', 'N/A')
                authors = ', '.join(book_info.get('authors', []))
                publisher = book_info.get('publisher', 'N/A')
                published_date = book_info.get('publishedDate', 'N/A')
                description = book_info.get('description', 'N/A')
                page_count = book_info.get('page_count', 0)
                main_category = ', '.join(book_info.get('categories', []))
                location = 'shelf'

                # Save book info to the database
                new_book = Book(
                    title=title,
                    authors=authors,
                    publisher=publisher,
                    published_date=published_date,
                    description=description, 
                    page_count = page_count, 
                    main_category = main_category, 
                    location = location

                )
                db.session.add(new_book)
                db.session.commit()
                flash(f'Book "{title}" by {authors} added successfully.', 'success')
            else:
                flash('No book found with that ISBN', 'danger')
        else:
            flash('Error fetching book data', 'danger')
    return render_template('add_book.html')
