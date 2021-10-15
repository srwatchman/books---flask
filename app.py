from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello, Worldzzz!'
    return render_template('index.html')

@app.route('/books')
def book_page():
    #return 'The contact page'
    return render_template('books.html')

@app.route('/contact')
def contact_page():
    #return 'The contact page'
    return render_template('contacts.html')