class Classifier:
    
    def __init__(self):
        print('Classifier ready!!')
        
    def classify(self, data):
        res = {
            'status': 'Processed',
            'action': 'lowercased',
            'text': data['text'].lower()
        }
        return res