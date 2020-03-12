from spellchecker import SpellChecker
from config import ROOT_DIR

class TextProcessor:

    def __init__(self):
        self.spell = SpellChecker()
        self.right = open(ROOT_DIR + "/data/literature.txt", 'r').read().split(' ')

    def detectMisspelledWords(self, text):
        words = text.split(' ')
        wrong = self.spell.unknown(words)
        return wrong
    
    def replaceMispelledWords(self, text):
        text = text.lower()
        wrong = self.detectMisspelledWords(text)
        for word in wrong:
            suggestions = self.spell.candidates(word)
            if len(suggestions) == 0:
                text = text.replace(word, '')
            else:
                for suggest in suggestions:
                    if suggest in self.right:
                        text = text.replace(word, suggest)
                    else:
                        text = text.replace(word, '')
        return text
