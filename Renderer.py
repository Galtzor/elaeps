import pygame
class Renderer:
    def __init__(self, screenSize):
        self.screen = pygame.display.set_mode(screenSize)
        
    def renderAll(self, backgroundColor, lineColor, centerPos, lineEndPos, square, squarePos, timeText, timePos):
        #1. fill screen with background color
        self.screen.fill(backgroundColor)

        #2. Draw the line
        pygame.draw.line(self.screen, lineColor, centerPos, lineEndPos)
        #3. Draw square
        self.screen.blit(square, squarePos)
        #4. Draw clock
        self.screen.blit(timeText, timePos)
        #loletelleranna
        pygame.display.flip()

    
