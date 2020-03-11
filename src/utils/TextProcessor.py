from spellchecker import SpellChecker

class TextProcessor:

    def __init__(self):
        self.spell = SpellChecker()

    def detectMisspelledWords(self, text):
        words = text.split(' ')
        right = self.spell.known(words)
        wrong = self.spell.unknown(words)
        return right, wrong
    
    def replaceMispelledWords(self, text):
        right, wrong = self.detectMisspelledWords(text)
        # print(right)
        # print(wrong)
        for word in wrong:
            suggestions = self.spell.candidates(word)
            # print("For "+word+" suggestions: "+', '.join(suggestions))
            if len(suggestions) == 0:
                text = text.replace(word, '')
            else:
                for suggest in suggestions:
                    if suggest in right:
                        text = text.replace(word, suggest)
                    else:
                        text = text.replace(word, '')
        return text
            
            
if __name__ == '__main__':
    main()