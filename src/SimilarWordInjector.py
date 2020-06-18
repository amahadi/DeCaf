from gensim.models.keyedvectors import KeyedVectors
from pathlib import Path
import warnings

class SimilarWordInjector:

    def __init__(self):
        warnings.simplefilter("ignore")
        ROOT_DIR = str(Path(__file__).parent.parent)
        print("Loading Similar Word Injector Model...")
        self.so_model = KeyedVectors.load_word2vec_format(ROOT_DIR + "/models/so.bin", binary=True)
        print("Similar Word Injector ready!!")

    
    def similar_stack_overflow_vocab(self, word):
        words_to_inject = []
        try:
            similar_words = self.so_model.most_similar(word)
            for similar_tuple in similar_words:
                if similar_tuple[1] > 0.5:
                    words_to_inject.append(similar_tuple[0])
        except:
            words_to_inject.append("")
        
        return " ".join(words_to_inject)

    def inject(self, text):
        words = text.split(" ")
        injected_text = []
        for word in words:
            so_similar_words = self.similar_stack_overflow_vocab(word)
            if len(so_similar_words) > 0:
                injected_text.append(word + " " + so_similar_words)
            else:
                injected_text.append(word)
        return " ".join(injected_text)
