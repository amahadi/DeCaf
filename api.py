from flask import Flask, request, jsonify
from src.WordEmbedding import Book

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def home():
    return "<h1>Hello world</h1>"

@app.route('/books', methods=['GET'])
def books(): 
    return jsonify(Book().index())

app.run()
