from pathlib import Path
import fasttext as ft
from src.Utils import FileManager as fm

class WordEmbedder:
    
    ROOT_DIR = str(Path(__file__).parent.parent)
    
    def __init__(self):
        fm(self.ROOT_DIR).create_directory('data')
        self.DATA_PATH = self.ROOT_DIR + '/data'
        fm(self.ROOT_DIR).create_directory('models')
        self.MODEL_PATH = self.ROOT_DIR + '/models'
    
    def create(self):
        fm(self.DATA_PATH).create_literature()
        model = ft.train_unsupervised(self.DATA_PATH + '/literature.txt')
        model.save_model(self.MODEL_PATH + '/wordembeddings.bin')
        