import pygame, Calendar
class Renderer:
    def __init__(self, screenSize, backgroundColor, lineColor, centerPos, square, timePos, datePos, dateFont, textColor): #timePos er clockPos...
        self.backgroundColor = backgroundColor
        self.lineColor = lineColor
        self.centerPos = centerPos
        self.square = square
        self.timePos = timePos
        #self.timeFont = timeFont
        self.datePos = datePos
        self.dateFont = dateFont
        self.textColor = textColor
        self.screen = pygame.display.set_mode(screenSize)
        self.clockImage = pygame.image.load("datclocktest.tga")

        self.zeroImage = pygame.image.load("digit/0.tga")
        self.oneImage = pygame.image.load("digit/1.tga")
        self.twoImage = pygame.image.load("digit/2.tga")
        self.threeImage = pygame.image.load("digit/3.tga")
        self.fourImage = pygame.image.load("digit/4.tga")
        self.fiveImage = pygame.image.load("digit/5.tga")
        self.sixImage = pygame.image.load("digit/6.tga")
        self.sevenImage = pygame.image.load("digit/7.tga")
        self.eightImage = pygame.image.load("digit/8.tga")
        self.nineImage = pygame.image.load("digit/9.tga")

        #alpha paa talla
        self.zeroImage.set_alpha(0)
        self.oneImage.set_alpha(0)
        self.twoImage.set_alpha(0)
        self.threeImage.set_alpha(0)
        self.fourImage.set_alpha(0)
        self.fiveImage.set_alpha(0)
        self.sixImage.set_alpha(0)
        self.sevenImage.set_alpha(0)
        self.eightImage.set_alpha(0)
        self.nineImage.set_alpha(0)

        # bredde paa digit:
        self.digitWidth = self.zeroImage.get_width()

        
    def renderAll(self, lineEndPos, squarePos, time, calendar):

        #endre  bg color
        #self.lighting(time)
        #1. fill screen with background color
        self.screen.fill(self.backgroundColor)
        

        #lag timeText og dateText i selve kallene, egne metoder.


        self.renderTime(time)
         
        #2. Draw the line
        pygame.draw.line(self.screen, self.lineColor, self.centerPos, lineEndPos)
        #3. Draw square
        self.screen.blit(self.square, squarePos)
        #4. Draw clock
        #self.screen.blit(self.timeText(time), self.timePos)
        #5: draw date
        self.screen.blit(self.dateText(calendar), self.datePos)
        #loletelleranna
        pygame.display.flip()

    #def timeText(self, time):
        #timeText = "{:d}:{:d}".format(time[0], time[1])
        #return self.timeFont.render(timeText, 1, self.textColor)
    

    def renderTime(self, time):
        self.screen.blit(self.clockImage, self.timePos)
        initialDist = self.timePos[0] + 20, self.timePos[1] + 34     #20 = distansen fra venstre av klokkebildet til det foerste tallbildet.. 34 = distansen fra toppen av klokkebildet til tallbildet
        midDist = 10 #bredden paa punktene i midten
        #render forste digit:
        self.screen.blit(self.returnDigit(time, 1), initialDist)
        #render andre digit:
        self.screen.blit(self.returnDigit(time, 2), (initialDist[0] + self.digitWidth, initialDist[1]))
        #render tredje digit:
        self.screen.blit(self.returnDigit(time, 3), (initialDist[0] + self.digitWidth *2 + midDist, initialDist[1]))
        #render fjerde digit
        self.screen.blit(self.returnDigit(time, 4), (initialDist[0] + self.digitWidth * 3 +  midDist, initialDist[1]))


    def returnDigit(self, time, n):         #..... konverterer int til string og saa til int igjen for aa finne siffer ved gitt n. Retarded.
        if(n == 1 or n == 2):
            if time[0] <= 9:         #skjekk om tiden har et eller to sifre for gitt n:
                if n == 1:
                    return self.digitByNum(0)
                return self.digitByNum(time[0])
            digitString = str(time[0])[n-1]
        else:
            if time[1] <= 9:         #skjekk om tiden har et eller to sifre for gitt n:
                if n == 3:
                    return self.digitByNum(0)
                return self.digitByNum(time[1])
            digitString = str(time[1])[n-1-2]

        return (self.digitByNum(int(digitString))) 
        
        
    
    
    def digitByNum(self, num):
        if num == 0: return self.zeroImage
        if num == 1: return self.oneImage
        if num == 2: return self.twoImage
        if num == 3: return self.threeImage
        if num == 4: return self.fourImage
        if num == 5: return self.fiveImage
        if num == 6: return self.sixImage
        if num == 7: return self.sevenImage
        if num == 8: return self.eightImage
        if num == 9: return self.nineImage

    def dateText(self, calendar):
        return self.dateFont.render(calendar.toString(), 1, self.textColor)

    def lighting(self, time):                           # !!WARNING!! EYECANCEROUS  !!WARNING!! FUNKER IKKE
        hour = time[0]
        if hour == 0: self.backgroundColor = 255, 0, 255
        elif hour == 1: self.backgroundColor = 255, 0, 217
        elif hour == 2: self.backgroundColor = 255, 0, 179
        elif hour == 3: self.backgroundColor = 255, 0, 141
        elif hour == 4: self.backgroundColor = 255, 0, 103
        elif hour == 5: self.backgroundColor = 255, 0, 75
        elif hour == 6: self.backgroundColor = 255, 0, 64
        elif hour == 7: self.backgroundColor = 255, 20, 75
        elif hour == 8: self.backgroundColor = 255, 45, 103
        elif hour == 9: self.backgroundColor = 255, 90, 141
        elif hour == 10: self.backgroundColor = 255, 145, 179
        elif hour == 11: self.backgroundColor = 255, 200, 217
        elif hour == 12: self.backgroundColor = 255, 255, 255
        elif hour == 13: self.backgroundColor = 255, 200, 255
        elif hour == 14: self.backgroundColor = 255, 144, 255
        elif hour == 15: self.backgroundColor = 255, 108, 255
        elif hour == 16: self.backgroundColor = 255, 72, 255
        elif hour == 17: self.backgroundColor = 255, 36, 255
        elif hour == 18: self.backgroundColor = 255, 0, 255
        elif hour == 19: self.backgroundColor = 255, 0, 255
        elif hour == 20: self.backgroundColor = 255, 0, 255
        elif hour == 21: self.backgroundColor = 255, 0, 255
        elif hour == 22: self.backgroundColor = 255, 0, 255
        elif hour == 23: self.backgroundColor = 255, 0, 255
        elif hour == 24: self.backgroundColor = 255, 0, 255

