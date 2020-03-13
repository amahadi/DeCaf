import os

class FileManager:
    
    def __init__(self, path):
        self.path = path
        
    def create_directory(self, name):
        if not os.path.exists(self.path + '/' + name):
            os.mkdir(self.path + '/' + name)
            
    def create_literature(self, path):
        return 0