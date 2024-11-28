import pygame

class buildEnvironment:
    def __init__(self, mapDimensions):
        pygame.init()
        self.pointCloud = []
        self.externalMap = pygame.image.load("map.png")
        self.mapHeight, self.mapWidth = mapDimensions
        self.mapWindowName = "Mapping"
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapWidth, self.mapHeight))
        self.map.blit(self.externalMap, (0, 0))

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)

