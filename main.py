from env import BuildEnvironment
from sensors import LaserSensor
from const import BLACK

import pygame

environment = BuildEnvironment((600, 1200))
environment.original_map = environment.map.copy()
laser = LaserSensor(200, environment.original_map, uncertainity = (0.5, 0.01))
environment.map.fill(BLACK)
environment.info_map = environment.map.copy()

running = True

while running:
    sensor_on = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensor_on = True
        elif not pygame.mouse.get_focused():
            sensor_on = False

    if sensor_on:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.data_storage(sensor_data)
        environment.show_sensor_data()

    environment.map.blit(environment.info_map, (0, 0))
    pygame.display.update()

