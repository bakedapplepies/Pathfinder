import pickle
import os


class SaveLoadManager():
    def __init__(self, dir: str, extension: str):
        self.dir = dir
        self.extension = extension
        
        if not os.path.exists("save_data"):
            os.mkdir("save_data")
    
    def save(self, filename: str, data):
        with open(self.dir+"/"+filename+self.extension, "wb") as savefile:
            pickle.dump(data, savefile)
    
    def load(self, filename):
        with open(self.dir+"/"+filename+self.extension, "rb") as savefile:
            return pickle.load(savefile)