import sys, pygame, math, Renderer, Calendar
class Logic:
    def __init__(self, center, distance, squarePos, lineEnd, pm, squareSize, renderer):
        #lag lokale variabler av ALLE CONSTANTS!!
        self.center, self.distance, self.squarePos, self.lineEnd, self.pm, self.squareSize, self.renderer = center, distance, squarePos, lineEnd, pm, squareSize, renderer
        self.calendar = Calendar.Calendar()
        self.date = self.calendar.getDate()
        self.initialize()
        
    def initialize(self):
        self.quadrant = findQuadrant(self.lineEnd, self.center)
        self.pressed = False
        #self.renderer.initialize() trengs denne????
        self.renderAll()
        
        

        

    def renderAll(self):
        self.renderer.renderAll(self.lineEnd, self.squarePos, self.findTime(), self.calendar)
    def update(self):
        self.handleInput()
        self.renderAll()
        

    def handleInput(self):
        e = pygame.event.wait()
        if e.type == pygame.QUIT: sys.exit() #Hvis du trykker på "x" -> quit
        elif self.pressed:
            #lagre forige posisjon, for retningsbestemmelse, midten av klossen. RELATIV TIL CENTER
            old_pos = (self.squarePos[0] + self.squareSize/2) - self.center[0], (self.squarePos[1] + self.squareSize/2) - self.center[1]
            
            mouse_pos = pygame.mouse.get_pos()
            #oppdater posisjon
            self.squarePos = mouse_pos[0] + self.rel_pos[0], mouse_pos[1] + self.rel_pos[1]
            
            #1. finn vektor fra sentrum (i parameters), normaliser vector, gang med distance
            pos_vec = self.normalizeVectorXDist(mouse_pos[0] - self.center[0], mouse_pos[1] - self.center[1])

            self.squarePos = self.checkDirection(pos_vec, old_pos)
            self.squarePos = self.center[0] + (self.squarePos[0] - self.squareSize/2), self.center[1] + (self.squarePos[1] - self.squareSize/2)

            pygame.mouse.set_pos(self.squarePos[0]+self.squareSize/2, self.squarePos[1]+self.squareSize/2)


            self.lineEnd = self.squarePos[0]+self.squareSize/2, self.squarePos[1] + self.squareSize/2
            
            if e.type == pygame.MOUSEBUTTONUP:
                self.pressed = False
                pygame.mouse.set_visible(True)
        else:
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                    #skjekk om klikket traff!
                if mouse_pos[0] > self.squarePos[0] and mouse_pos[0] < self.squarePos[0] + self.squareSize and mouse_pos[1] > self.squarePos[1] and mouse_pos[1] < self.squarePos[1] + self.squareSize:
                    self.pressed = True
                    pygame.mouse.set_visible(False)
                        #finn ut hvor på saken klikket traff.
                            # --- DEPRECATED, GANSKE SIKKER PÅ DET GITT. eller dunno, første goaround? enkel løsning sikkert!
                    self.rel_pos = self.squarePos[0] - mouse_pos[0], self.squarePos[1] - mouse_pos[0]


        # SKJEKKER OM FLYTTET GÅR I RIKTIG RETNING, HVIS FEIL RETURNER GAMMELT KOORDINAT.
    def checkDirection(self, A, B): #A er nytt koordinat, B er gammelt, quadrant er en variabel på klassenivå(self.quadrant)
        aX, aY = A[0], A[1]
        bX, bY = B[0], B[1]
        
        #fortegna er feil, har gjort om logikken ettersom y aksen er baklengs i forhold til vanlig. hvis det er vanskelig å skjønne; husk at top left er (0,0), opp er minus, høyre er pluss.
        if self.quadrant == 1:
            if (aY > bY) and (aX >= 0):
                if aY >= 0:
                    self.plusplusQuadrant()
                return A
        elif self.quadrant == 2:
            if (aX < bX) and (aY >= 0):
                if aX <= 0:
                    self.plusplusQuadrant()
                return A
        elif self.quadrant == 3:
            if (aY < bY) and (aX <= 0):
                if aY <= 0:
                    self.plusplusQuadrant()
                return A
        else:
            if (aX > bX) and (aY <= 0):
                if aX >=0:
                    self.plusplusQuadrant()
                return A
        return B

        # LEGG TIL EN PÅ KVADRANTTELLEREN, HVIS 4->1 ENDRE PM->AM-PM OG BEGYNN PÅ 1 IGJEN
    def plusplusQuadrant(self):
        if self.quadrant == 4:
            self.quadrant = 1
            if self.pm:
                self.pm = False     # ERSTATT PM SKJEKKEN MED ET FUNKSJONSKALL FOR aa ENDRE DAG.
                self.calendar.nextDay()
            else: self.pm = True
        else:
            self.quadrant = self.quadrant + 1

        # NORMALISER VEKTOR, GANG DEN MED DISTANSE FRA SENTRUM FOR Å FINNE KOORDINATET.
    def normalizeVectorXDist(self, x, y):
        #bug squashing: kan ikke dele med 0, ergo hverken x eller y kan være 0.
        if x == 0: x = 1
        if y == 0: y = 1
        
        vector_len = math.sqrt(x**2 + y**2)

            #ikke int
        return (x*self.distance/vector_len, y*self.distance/vector_len)
            

    def findTime(self):        # TESTED, WORKING BIATCH
        halfpi  = math.pi / 2

        # 1. finn vektor, gange med -1 for å sleppe mongotenkning. da er Y oppover positiv.
        lcVec = self.lineEnd[0] - self.center[0], (self.lineEnd[1] - self.center[1]) * - 1
        #regn ut vinkelen alpha!
        if self.quadrant == 1 or self.quadrant == 3: # |atan(x/y)| + 0 degrees or + 180 degrees   - radians
            alpha = (self.quadrant - 1) * halfpi + math.fabs(math.atan(lcVec[0]/lcVec[1]))
        else: # |atan(y/x)| + 90 degrees or + 270 degrees   - radians
            alpha = (self.quadrant - 1) * halfpi + math.fabs(math.atan(lcVec[1]/lcVec[0]))

        #konverter til grader
        alpha = math.degrees(alpha)

        # 360/12 = 30 -> vinkel / 30 = time.
        hours = math.floor(alpha / 30)

        # resten bak hours er minutter, * 60 for antall minutter. (10.5 = 10 timer 30 minutter)
        minutes = math.floor(((alpha / 30) - hours) * 60)

        #if pm(12:00 -> 23:59): legg til 12 timer på klokkeutregninga!
        #   (False*x = 0, True * x = x.)
        #   RETURNER (HOURS+12*PM, MINUTES) SOM TUPLE ISTEDET ETTERHVERT.
        """
        print (self.pm)
        time = (hours + 12*self.pm, minutes)
        if self.pm and time[0] < 12:
            self.pm = False
            self.calendar.nextDay()
            print(calendar.toString())
            time[0] = time[0] - 24
        if ((not self.pm) and time[0] >=12):
            self.pm = True #time[0] = timer etter am/pm regning
        
        return time
        """
        return (hours + 12*self.pm, minutes)

# finn kvadrant for gitt koordinat paa timeviseren, kalles bare ved initialiseringen av klassen.
def findQuadrant(lineEnd, center):
    # 1. finn vektor, gange med -1 for å sleppe mongotenkning. da er Y oppover positiv.
    lcVec = x, y = lineEnd[0] - center[0], (lineEnd[1] - center[1]) * - 1

    if x >= 0 and y > 0: return 1
    if x > 0 and y <= 0: return 2
    if x <= 0 and y < 0: return 3
    if x < 0 and y >= 0: return 4
