import unittest
from flask import (request,
make_response, redirect,render_template,
session, url_for,flash)
from flask_login import login_required, current_user

from app import create_app
from app.forms import BookForm, DeleteBookForm, UpdateBookForm
from app.firestore_service import (get_users,
get_favorite_books, book_put, delete_book, update_book)

app = create_app()



'''favorite_books = ['Ready Player One','Les Misérables ',
'Paper Towns','The four fundamental forces']'''


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    book_form = BookForm()
    delete_form = DeleteBookForm()
    update_form = UpdateBookForm()


    context = {
        'user_ip':user_ip,
        'favorite_books':get_favorite_books(user_id=username),
        'username': username,
        'book_form': book_form,
        'delete_form':delete_form,
        'update_form': update_form}

    if book_form.validate_on_submit():
        book_put(user_id=username,title=book_form.title.data)

        flash('The book has been added successfully')

        return redirect(url_for('hello'))

    return render_template('hello.html', **context)

@app.route('/book/delete/<book_id>',methods=['POST'])
def delete(book_id):
    user_id = current_user.id
    delete_book(user_id=user_id,book_id=book_id)

    return redirect(url_for('hello'))


@app.route('/book/update/<book_id>/<int:read>',methods=['POST'])
def update(book_id,read):
    user_id = current_user.id
    update_book(user_id=user_id,book_id=book_id,read=read)

    return redirect(url_for('hello'))


# use them if you use the comand 'flask run'
# export  FLASK_APP=main.py
# export FLASK_DEBUG=1
# export FLASK_ENV=development


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
