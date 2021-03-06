import pygame,random,time
from pygame.locals import *

class Button():#based on the code from my previous attempt at a button
    def __init__(self, rect, command, text = "", Fsize = 12):
        self.rect = rect
        self.command = command
        self.text = text
        self.Fsize = Fsize
        self.colour = (255,255,255)

    def pressButton(self):
        self.command()

    def showButton(self,surface):#stick in an if statement so that it's not shown twice
        pygame.draw.rect(surface, self.colour, self.rect)
        font = pygame.font.Font('freesansbold.ttf',self.Fsize)
        msgSurfObj = font.render(self.text, False, pygame.color.Color(0,0,0))
        msgRectObj = msgSurfObj.get_rect()
        msgRectObj.center = (self.rect[0] + int(self.rect[2]/2), self.rect[1] + int(self.rect[3]/2))
        surface.blit(msgSurfObj, msgRectObj)

    def get_Xs(self):#the start and end of the x co-ords where button is
        return self.rect[0],self.rect[0]+self.rect[2]
    def get_Ys(self):
        return self.rect[1],self.rect[1]+self.rect[3]

    def checkPress(self,mX,mY):#mouseX and mouseY
        co_ords = [self.get_Xs(),self.get_Ys()]
        if co_ords[0][0] < mX < co_ords[0][1]:
            if co_ords[1][0] < mY < co_ords[1][1]:
                return True
    

class SwitchB(Button):#boom some ineritence
    def __init__(self, rect, switch, text = "", Fsize = 12):
        self.rect = rect
        if isinstance(switch, bool):
            self.switch = switch
            self.onColour = pygame.color.Color(0,255,0)
            self.offColour = pygame.color.Color(255,0,0)
            self.colour = self.offColour
            self.text = text
        elif isinstance(switch, list):
            self.switch = switch
            self.colour = pygame.color.Color(0,0,255)
            self.l = len(switch)
            self.stateN = 0
            self.colourA = []#stick in a comprehension so set the colours
            if isinstance(text,list):
                if len(text) == len(switch):
                    self.text = text
                else:
                    print("text array must be the same length as the switch array")
                    self.text = ''
            else:
                self.text = text
        else:
            raise TypeError('switch must be a bool type or a list type or a function')
        self.Fsize = Fsize

    def pressButton(self):
        if isinstance(self.switch, bool):
            self.switch = not self.switch
        else:
            self.stateN += 1
            if self.stateN == self.l:
                self.stateN = 0
                

    def getState(self):
        if isinstance(self.switch, bool):
            return self.switch
        else:
            return self.switch[self.stateN]
            
        
    def showButton(self,surface):
        if isinstance(self.switch, bool):
            if self.switch:
                colour = self.onColour
            else:
                colour = self.offColour
        else:
            if len(self.colourA) == self.l:
                colour = self.colourA[self.stateN]
            else:
                colour = self.colour
        pygame.draw.rect(surface, colour, self.rect)
        if len(self.text) > 0:
            font = pygame.font.Font('freesansbold.ttf',self.Fsize)
            if type(self.text) == list:
                msgSurfObj = font.render(self.text[self.stateN],False,pygame.color.Color(0,0,0))
            else:
                msgSurfObj = font.render(self.text, False, pygame.color.Color(0,0,0))
            msgRectObj = msgSurfObj.get_rect()
            msgRectObj.center = (self.rect[0] + int(self.rect[2]/2), self.rect[1] + int(self.rect[3]/2))
            windowSurf.blit(msgSurfObj, msgRectObj)


class Card():
    def __init__(self, faceVal, suit,faceN):
        self.faceVal = faceVal
        self.suit = suit
        self.img = ''
        self.faceN = faceN

class Player():
    def __init__(self, name, chips, hand, points):
        self.name = name
        self.chips = chips
        self.hand = hand
        self.points = points
    
    def calcScore(self):
        score = 0
        for i in range(len(self.hand)):
            if 1<self.hand[i].faceN<11:
                score += self.hand[i].faceN
            elif 10<self.hand[i].faceN<14:
                score+=10
            elif self.hand[i].faceN == 1:
                score += aceBs[self.hand[i]].getState()
        return score
    
    def binHand(self,binD):#binDeck
        #cards = [self.hand.pop() for x in range(len(self.hand))]
        for i in range(len(self.hand)):
            binD.append(self.hand.pop())

class Deck():
    def __init__(self,cards):
        self.cards = cards

    def shuffleDeck(self):
        shuffled = []
        orig = [deck[x] for x in range(len(self.cards))]
        for i in range(len(self.cards)):
            rand = random.randint(0,len(self.cards)-1)
            shuffled.append(self.cards[rand])
            self.cards.remove(deck[rand])
        self.cards = shuffled
        #do i want to do anything with orig?

    def dealN(self,target,n):#where target is the hand/table you're dealing to
        dealing = [self.cards.pop() for x in range(n)]
        for i in range(n):
            target.append(dealing[i])
            if dealing[i].faceVal == 'A':
##                """AAAAAHHHHH
##YOU NEED TO DO THINGS HERE
##WELL THINGS HAVE HAPPENED HERE ARE IMPORTANT
##MAKE SURE YOU SORT OUT THE ACES
##THE ACES
##THE ACES
##AAAAAAAAHHHHH"""
##                aceBs[dealing[i]] =  SwitchB((0,0,0,0), [1,11],"umm shouldnt this change?")
##                aceBs[dealing[i]].colourA = [pygame.Color(255,0,0),pygame.Color(0,0,255)]
                aceBs[dealing[i]] = AceButton(dealing[i])        
##class AceBs():
##    def __init__(self,
"""
and i need to figure out how to make this aceBs class
"""

class AceButton(SwitchB):
    def __init__(self,card):
        self.card = card
        self.colourA = [pygame.Color(255,0,0),pygame.Color(0,0,255)]
        self.switch = [1,11]
        self.text = ['1','11']
        self.l = 2
        self.stateN = 0
        self.rect = (0,0,0,0)
        self.Fsize = 12
        #with all this i may aswell have just left it as a SwitchB
##class AceBs():
##    def __init__(self):
##        self.buttons = []
##
##    def addButton(self,aceButton):
##        if isinstance(aceButton, AceButton):
##            self.buttons.append(AceButton)
##        else:
##            print("you can only add summat of Aceutton class")
#don't think it'll work creating AceBs class    



def displayText(surface,text,topLeft):
    textSurf = fontObj.render(str(text), False, colour['green'])
    textRect = textSurf.get_rect()
    textRect.topleft = topLeft
    surface.blit(textSurf, textRect)
    
#shuffled/clean/bin
num = 0
deck = []
suits = ('♠', '❤', '♣', '♦')
CARDWIDTH = 75
CARDHEIGHT = int(3* 145/4)#i hope
#picAddr = 'Playing Cards\\PNG-cards-1.3\\'##if the file is saved in the same file
picAddr = "C:/Users/Akmal/Desktop/Files/games/programs/Playing Cards/PNG-cards-1.3/"#just for now
for i in range(4):
    if i == 0:#this'd be a great place for a case/switch
        blob = 'spades'
    elif i == 1:
        blob = 'hearts'
    elif i == 2:
        blob = 'clubs'
    elif i == 3:
        blob = 'diamonds'
    for j in range(1,14):
            if j == 1:
                face = 'A'
                bob = 'ace'
            elif j == 11:
                face = 'J'
                bob = 'jack'
            elif j == 12:
                face = 'Q'
                bob = 'queen'
            elif j == 13:
                face = 'K'
                bob = 'king'
            else:
                face = str(j)
                bob = face
            deck.append(Card(face,suits[i],j))
            try:
                deck[-1].img = pygame.image.load(picAddr+bob+'_of_'+blob+'.png')
            except pygame.error:
                print("you you haven't saved the pics in a folder called Playing Cards and a folder called PNG-cards-1.3")
                print("copy the exact address of where the pics are saved")
                picAddr = input()
                try:
                    deck[-1].img = pygame.image.load(picAddr+bob+'_of_'+blob+'.png')
                except pygame.error:
                    print("well i tried...")
                    quit()
            #deck[-1].img = pygame.transform.scale(deck[-1].img,(int(deck[-1].img.get_width()/5),int(deck[-1].img.get_height()/5)))
            deck[-1].img = pygame.transform.scale(deck[-1].img, (CARDWIDTH, CARDHEIGHT),)
CLEANDECK = Deck(deck)
shuffledD = Deck(deck)
shuffledD.shuffleDeck()
del bob,blob,face,j,i,picAddr,num,deck
binD = Deck([])






pygame.init()
fpsClock = pygame.time.Clock()
windowSurf = pygame.display.set_mode((960,480))
pygame.display.set_caption("Ver2")
windowW = windowSurf.get_width()
windowH = windowSurf.get_height()

colour = {
    'red' : pygame.Color(255,0,0),
    'green' : pygame.Color(0,255,0),
    'blue' : pygame.Color(0,0,255),
    'white' : pygame.Color(255,255,255),
    'magenta' : pygame.Color(255,0,255),
    'yellow' : pygame.Color(255,255,0),
    'cyan' : pygame.Color(0,255,255),
    'black' : pygame.Color(0,0,0),
    'silver' : pygame.Color(192,192,192)
}
colour2 = {}
file = open ('C:\\Users\\Akmal\\Desktop\\Files\\500+ colours.csv','r')
lines = file.readlines()
file.close
colName = ''
red = 0
green = 0
blue =0
for i in range(1,len(lines)):
    row = lines[i].split(',')
    colName = str(row[0])
    red,green,blue = int(row[4]),int(row[5]),int(row[6])
    colour2[colName] = pygame.color.Color(red,green,blue)
del red,green,blue
fontObj = pygame.font.Font('freesansbold.ttf',32)

mouseX,mouseY = 0,0

#print("how many players")
#playersN = input()
#etc



"""
THIS IS TEMPORARY
CHANGE THIS
THIS IS TEMPORARY
"""
testPlayer = Player("Akmal",100,[],0)

hitB = Button((300,windowH-125,80,40), lambda:shuffledD.dealN(testPlayer.hand, 1), text = "HIT")

aceBs = {}#BUILD ACEbS CLASS


running = True
#i need more than one while loop
#maybe while loops within a for loops
#wow i can stick that for loop in a while loop
#woah
#loopception
while running:
    windowSurf.fill(colour['blue'])

    #for each player +1(computer)
    #maybe use hydrox's PlayerSlot class???
    for p in range(1):#call it p for player
        #use the other for loop once i've got this sorted
        while running:#umm what do i stick here???????????????????????????????
            windowSurf.fill(colour['blue'])#could i change colour for players?
            currentPlayer = testPlayer
            currentHand = currentPlayer.hand
            handSize = len(currentHand)
            for i in range(handSize):
                windowSurf.blit(currentHand[i].img, (10+i*(CARDWIDTH+5), 100))
                if currentHand[i] in aceBs:
                    aceBs[currentHand[i]].rect = (10+i*(CARDWIDTH+5),100+CARDHEIGHT+10,CARDWIDTH,20)
                    aceBs[currentHand[i]].showButton(windowSurf)
                    
            hitB.showButton(windowSurf)

            displayText(windowSurf, currentPlayer.points, (windowW-75,10))

            #temp to keep an eye on remaining cards
            displayText(windowSurf,len(shuffledD.cards),(windowW-75,40))#keep an eye on that 40        may wanna change it

            pygame.display.update()
            fpsClock.tick(30)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_q:
                        pygame.event.post(pygame.event.Event(QUIT))
                elif event.type == QUIT:
                    pygame.quit()
                    running = False
                elif event.type == MOUSEMOTION:
                    mouseX,mouseY = event.pos
                elif event.type == MOUSEBUTTONUP:
                    if hitB.checkPress(mouseX,mouseY):
                        hitB.pressButton()
                        currentPlayer.points = currentPlayer.calcScore()
                    for key in aceBs.keys():
                        if aceBs[key].checkPress(mouseX,mouseY):
                            aceBs[key].pressButton()
                            currentPlayer.points = currentPlayer.calcScore()
        











#end of the program
##that's just here for now
time.sleep(2)
pygame.quit()
