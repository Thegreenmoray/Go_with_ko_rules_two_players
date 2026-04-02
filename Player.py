class Player:

  #constructor
    def __init__(self, color):
        self.color = color
        self.prisoners = 0

    def getcolor(self):
        return self.color

    def getprisoners(self):
        return self.prisoners

    def setprisoners(self, prisoners):
        self.prisoners = prisoners