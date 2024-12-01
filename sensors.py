from const import BLACK

import numpy as np 
import math
import pygame

def uncertainity_add(distance, angle, sigma):
    mean = np.array([distance, angle])
    covariance = np.diag(sigma ** 2)
    distance, angle = np.random.multivariate_normal(mean, covariance)
    distance = max(distance, 0)
    angle = max(angle, 0)
    return [distance, angle]

class LaserSensor:
    def __init__(self, lidar_range, map, uncertainity):
        self.lidar_range = lidar_range
        self.sigma = np.array([uncertainity[0], uncertainity[1]]) 
        self.position = (0, 0)
        self.map = map
        self.map_width, self.map_height = pygame.display.get_surface().get_size()
        self.sensed_obstacles = []

    def distance(self, obstacle_position):
        px = (obstacle_position[0] - self.position[0])**2
        py = (obstacle_position[1] - self.position[1])**2
        return math.sqrt(px+py)

    def sense_obstacles(self):
        data = []
        x1, y1 = self.position[0], self.position[1]
        for angle in np.linspace(0, 2 * math.pi, 60, False):
            #endpoint of laser beam - a line of length lidar_range from the position at an angle
            x2, y2 = (x1 + self.lidar_range * math.cos(angle), y1 - self.lidar_range * math.sin(angle)) 
            #breaks the laser beam into 100 points using linear interpolation and checks if each point is black or not
            for i in range(0, 100):
                u = i / 100
                x = int(x2 * u + x1 * (1 - u)) 
                y = int(y2 * u + y1 * (1 - u))
                if 0 < x < self.map_width and 0 < y < self.map_height:
                    color = self.map.get_at((x, y))
                    if (color == BLACK):
                        distance = self.distance((x, y))
                        output = uncertainity_add(distance, angle, self.sigma)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False

