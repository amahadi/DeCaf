from flask import Flask, request, jsonify
from WordEmbedder import WordEmbedder
from Classifier import Classifier

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def home():
    return "<h1>Hello world</h1>"

@app.route('/books', methods=['GET'])
def books(): 
    return jsonify(Book().index())

@app.route('/classify', methods=['POST'])
def classify():
    return jsonify(Classifier().classify(request.json))

@app.route('/we', methods=['GET'])
def we():
    return jsonify(WordEmbedder().create())

app.run(debug=True)
