
class Mapmanager():
    def __init__(self):
        self.model = "block.glb"
        self.texture = "grass.png"
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.color = (60,200,1,1)
        self.start_new()
        self.add_block((0,10,0))

    def start_new(self):
        self.land = render.attachNewNode("Land")

    def add_block(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)


