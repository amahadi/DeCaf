from pathlib import Path
import fasttext as ft
from Utils import FileManager as fm

class WordEmbedder:
    """
    Here we make the embedding for word representation.
    1. we take literature.txt as our input data.
    2. we train the classifier upsupervised since we just want to group the data according to the similarity.
    3. we have used skipgram as we have observe that skipgram models works better with subword information that cbow
    4. we are taking words with character number from 4-20. since we are removing every word less than three characters,
    its not important to take the characters less than 4 characters. Also, the design words seems to be on the bigger side.
    for ex. reproduceability contains 16 characters. we are considering characters upto 25 characters.
    5. We are taking 300 dimension of the words. Also looping for 10 epochs. Both because the training corpus is relatively small.
    """
    
    ROOT_DIR = str(Path(__file__).parent.parent)
    
    def __init__(self):
        fm(self.ROOT_DIR).create_directory('data')
        self.DATA_PATH = self.ROOT_DIR + '/data'
        fm(self.ROOT_DIR).create_directory('models')
        self.MODEL_PATH = self.ROOT_DIR + '/models'
    
    def create(self):
        fm(self.DATA_PATH).create_literature()
        model = ft.train_unsupervised(self.DATA_PATH + '/literature.txt', "skipgram", minn=4, maxn=25, dim=300, epoch=10)
        model.save_model(self.MODEL_PATH + '/wordembeddings.bin')
        