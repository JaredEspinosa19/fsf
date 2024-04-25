

class Files:
    
    def __init__(self) -> None:
        self.mainFile = None
        self.extraFile = None

    def setMainFile(self, name: str):
        self.mainFile = name
    
    def setExtraFile(self, name: str):
        self.extraFile = name