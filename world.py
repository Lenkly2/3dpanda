
class Mapmanager():
    def __init__(self):
        self.model = "block.glb"
        self.texture = "grass.png"
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.color=[(60,200,1,1),
                    (60,200,1,1),
                    (60,200,1,1),
                    (60,200,1,1)]
        self.start_new()
        self.add_block((0,10,0))

    def start_new(self):
        self.land = render.attachNewNode("Land")

    def getColor(self,z):
        if z < len(self.color):
            return self.color[z]
        else:
            return self.color[len(self.color)-1]

    def add_block(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color1 = self.getColor(int(position[2]))
        self.block.setColor(self.color1)
        self.block.reparentTo(self.land)

    def loadMap(self):
        self.land.removeNode()
        self.start_new()
        with open("land.txt") as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(" ")
                for l in line:
                    for z0 in range(int(l)+1):
                        block = self.add_block((x,y,z0))
                    x +=1
                y += 1

