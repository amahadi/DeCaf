import fasttext as ft
from pathlib import Path
import warnings

class Vectorizer:

    def __init__(self):
        warnings.simplefilter("ignore")
        ROOT_DIR = str(Path(__file__).parent.parent)
        print("Loading Vectorizer Model...")
        self.model = ft.load_model(ROOT_DIR + "/models/enhanced_we_300d.bin")
        print('Vectorizer ready!!')

    def text_to_vector(self, text):
        vector = self.model.get_sentence_vector(text)
        return [vector]