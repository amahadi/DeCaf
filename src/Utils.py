import os
from gensim import utils
from gensim.parsing.preprocessing import preprocess_string, strip_tags, \
strip_punctuation, strip_multiple_whitespaces, strip_numeric, \
remove_stopwords, strip_short
from nltk.stem import WordNetLemmatizer

class FileManager:
    
    def __init__(self, path):
        self.path = path
        
    def create_directory(self, name):
        if not os.path.exists(self.path + '/' + name):
            os.mkdir(self.path + '/' + name)
            
    def create_literature(self):
        if not os.path.exists(self.path + '/' + 'literature.txt'):
            return 'File Not found. Need to download'

class TextProcessor:

    def lemmitizer(self, s):
        wnl = WordNetLemmatizer()
        return " ".join(wnl.lemmatize(word) for word in s.split())

    def strip_long(self, s, maxsize=25):
        s = utils.to_unicode(s)
        return " ".join(e for e in s.split() if len(e) <= maxsize)

    def process(self, text):
        custom_filters = [
            lambda x: self.strip_long(x),
            lambda x: self.lemmitizer(x),
            strip_tags,
            strip_punctuation,
            strip_multiple_whitespaces,
            strip_numeric,
            remove_stopwords,
            strip_short    
        ]
        text = " ".join(preprocess_string(text, custom_filters))
        return text