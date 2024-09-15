from direct.showbase.ShowBase import ShowBase
from world import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        # base.camLens.setPov(90)


game = Game()
game.run()