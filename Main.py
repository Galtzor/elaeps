import sys, pygame, Logic
pygame.init()

# CONSTANTS #
# --------- #
screenSize = width, height = 1024, 1024
center = center_w, center_h =  width/2, height/2
backgroundColor = 50, 20, 30
textColor = 0, 0, 0
distance = 256
lineColor = 255, 127, 255
timePos = 16, 16
timeFont = pygame.font.Font(None, 128)
square = pygame.image.load("square.png")

#screen = pygame.display.set_mode(screenSize)


squareSize = square.get_rect().w

#12:00
squarePos = center_w - squareSize / 2, center_h - distance - squareSize / 2
timeText = timeFont.render("12:00", 1, textColor)
lineEnd = center_w, squarePos[1] + squareSize / 2
pm = True


# INITIALIZE CLASSES ETC. #
# ----------------------- #

logic = Logic.Logic(screenSize, center, distance, timePos, timeFont, square, squarePos, timeText, backgroundColor, textColor, lineEnd, lineColor, pm, squareSize)

while 1:
    logic.update()
# GAME LOOP #
# --------- #
#while 1:
    #logic.handleShit!
