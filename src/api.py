from flask import Flask, request, jsonify
from WordEmbedder import WordEmbedder
from SimilarWordInjector import SimilarWordInjector
from Vectorizer import Vectorizer
from Classifier import Classifier
from Utils import TextProcessor
from pathlib import Path
import nltk

app = Flask(__name__)
ROOT_DIR = str(Path(__file__).parent.parent)

Injector = SimilarWordInjector()
Vectorizer = Vectorizer()
Classifier = Classifier()
nltk.download('wordnet')

@app.route('/classify', methods=['POST'])
def classify():
    return jsonify(
        {
            'label': 
            Classifier.classify(
                Vectorizer.text_to_vector(
                    Injector.inject(
                        TextProcessor().process(
                            request.json['text']
                        )
                    )
                )
            )
        }
    )

@app.route('/we', methods=['GET'])
def we():
    return jsonify(WordEmbedder().create())

app.run(debug=True)
