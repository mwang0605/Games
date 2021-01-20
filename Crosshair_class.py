import pygame

import Constants

class Crosshair:
    line_thickness = 3
    line_length = 7
    color = Constants.RED

    def basic_crosshair(self, screen, pos):
        pygame.draw.line(screen, self.color, (pos[0]+self.line_length,pos[1]), (pos[0]-self.line_length,pos[1]), self.line_thickness)
        pygame.draw.line(screen, self.color, (pos[0], pos[1]+self.line_length), (pos[0], pos[1]-self.line_length), self.line_thickness)

