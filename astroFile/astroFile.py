import os 

class AstroFile:

    def __init__(self, path):
        self.path = path
    
    def get_path(self):
        print(f'path:  {self.path}')
        return self.path

    def get_dimencions(self, file: str) -> str:
        return "200 x 260"