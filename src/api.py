from flask import Flask, request, jsonify
from SimilarWordInjector import SimilarWordInjector
from Vectorizer import Vectorizer
from Classifier import Classifier
from Utils import TextProcessor
from pathlib import Path
import nltk

app = Flask(__name__)

nltk.download('wordnet')
Vectorizer = Vectorizer()
Classifier = Classifier()
Injector = SimilarWordInjector()

@app.route('/classify', methods=['POST'])
def classify():
    return jsonify(
        {
            'text': request.json['text'],
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

app.run(
    debug=True,
    host='0.0.0.0'
)
