import pygame, Calendar
class Renderer:
    def __init__(self, screenSize, backgroundColor, lineColor, centerPos, square, timePos, timeFont, datePos, dateFont, textColor):
        self.backgroundColor = backgroundColor
        self.lineColor = lineColor
        self.centerPos = centerPos
        self.square = square
        self.timePos = timePos
        self.timeFont = timeFont
        self.datePos = datePos
        self.dateFont = dateFont
        self.textColor = textColor
        self.screen = pygame.display.set_mode(screenSize)

        
    def renderAll(self, lineEndPos, squarePos, time, calendar):
        #1. fill screen with background color
        self.screen.fill(self.backgroundColor)
        
        #lag timeText og dateText i selve kallene, egne metoder.
        
        
        #2. Draw the line
        pygame.draw.line(self.screen, self.lineColor, self.centerPos, lineEndPos)
        #3. Draw square
        self.screen.blit(self.square, squarePos)
        #4. Draw clock
        self.screen.blit(self.timeText(time), self.timePos)
        #5: draw date
        self.screen.blit(self.dateText(calendar), self.datePos)
        #loletelleranna
        pygame.display.flip()

    def timeText(self, time):
        timeText = "{:d}:{:d}".format(time[0], time[1])
        return self.timeFont.render(timeText, 1, self.textColor)
    def dateText(self, calendar):
        return self.dateFont.render(calendar.toString(), 1, self.textColor)
