import sys, pygame, Logic, Renderer
pygame.init()

# CONSTANTS #
# --------- #
screenSize = width, height = 1400, 900
center = center_w, center_h =  width/2, height/2
backgroundColor = 50, 20, 30
textColor = 0, 0, 0
distance = 86
lineColor = 200, 255, 255
timePos = 16, 16
#timeFont = pygame.font.Font(None, 64)
dateFont = pygame.font.Font(None, 32)
datePos = (26, 156)
square = pygame.image.load("square.png")

#screen = pygame.display.set_mode(screenSize)


squareSize = square.get_rect().w

#12:00
squarePos = center_w - squareSize / 2, center_h - distance - squareSize / 2
lineEnd = center_w, squarePos[1] + squareSize / 2
pm = True


# INITIALIZE CLASSES ETC. #
# ----------------------- #
renderer = Renderer.Renderer(screenSize, backgroundColor, lineColor, center, square, timePos, datePos, dateFont, textColor)
logic = Logic.Logic(center, distance, squarePos, lineEnd, pm, squareSize, renderer)
# GAME LOOP #
# --------- #
while 1:
    logic.update()

