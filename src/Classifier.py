from joblib import load
from pathlib import Path
import warnings

class Classifier:
    
    def __init__(self):
        warnings.simplefilter("ignore")
        ROOT_DIR = str(Path(__file__).parent.parent)
        print("Loading Classifier Model")
        self.model = load(ROOT_DIR + "/models/lsvm.joblib") 
        print('Classifier ready!!')
        
    def classify(self, data):
        label = self.model.predict(data)[0]
        if label == 1:
            return 'design'
        else:
            return 'general'