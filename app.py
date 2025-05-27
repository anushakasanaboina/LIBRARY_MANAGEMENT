from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)

books = []
members = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    books.append({
        'title': title,
        'author': author,
        'added_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return redirect('/books')

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['name']
    membership_type = request.form['membership_type']
    members.append({
        'name': name,
        'membership_type': membership_type,
        'registration_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    return redirect('/members')

@app.route('/books')
def view_books():
    return render_template('books.html', books=books)

@app.route('/members')
def view_members():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)
