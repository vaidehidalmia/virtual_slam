from const import RED

import pygame
import math

class BuildEnvironment:
    def __init__(self, map_dimensions):
        pygame.init()
        self.point_cloud = []
        self.external_map = pygame.image.load("map.png")
        self.map_height, self.map_width = map_dimensions
        self.map_window_name = "Mapping"
        pygame.display.set_caption(self.map_window_name)
        self.map = pygame.display.set_mode((self.map_width, self.map_height))
        self.map.blit(self.external_map, (0, 0))

    def polar_to_cartesian(self, distance, angle, robot_position):
        x = distance * math.cos(angle) + robot_position[0]
        y = -distance * math.sin(angle) + robot_position[1]
        return (int(x), int(y))

    def data_storage(self, data):
        if not data: return
        for element in data:
            point = self.polar_to_cartesian(element[0], element[1], element[2])
            if point not in self.point_cloud:
                self.point_cloud.append(point)

    def show_sensor_data(self):
        self.info_map = self.map.copy()
        for (x, y) in self.point_cloud:
            self.info_map.set_at((x, y), RED)