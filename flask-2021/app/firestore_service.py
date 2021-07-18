import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'curso-de-flask-platzi'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential,{'projectId':project_id})

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_favorite_books(user_id):
    return db.collection('users').document(user_id).collection('favorite-books').get()


def book_put(user_id,title):
    book_collection_ref = db.collection('users').document(user_id).collection('favorite-books')
    book_collection_ref.add({'title': title, 'read': False})


def delete_book(user_id,book_id):
    # book_ref = db.document(f'users/{user_id}/favorite-books/{book_id}')
    book_ref = db.collection('users').document(user_id)\
        .collection('favorite-books').document(book_id)
    book_ref.delete()


def update_book(user_id,book_id, read):
    book_read = not bool(read)
    book_ref = _get_book_ref(user_id,book_id)
    book_ref.update({'read': book_read})


def _get_book_ref(user_id,book_id):
    return db.document(f'users/{user_id}/favorite-books/{book_id}')
