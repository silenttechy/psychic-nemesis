"""
BLACKJACK GAME
Author: Akmal Khalil
had some help from the guys in my CS class

https://github.com/silenttechy/psychic-nemesis
NOTE:make sure Deck2 is saved as Deck2 in the same folder as this game
"""
import time, Deck2

def numOfPlayers():
    while True:
        
        print("how many players will there be")
        try:
            n = int(getUserInput())
            #break if n <= 5 else print("You can only have up to 5 players for now")
            if 0 < n <= 5 :
                break
            else:
                print("you can only have 1 to 5 players for now")
        except ValueError:
            print("you didn't enter an interger")
    for i in range(n):
        players.append(['player'+str(i+1), 'I\'ll do the hand here', 100, 0, 0])
    playerNames()
    return n+1
def initHand(deck):
    for i in range(1,len(players)):
        players[i][1] = [deal(deck),deal(deck)]

def deal(deck):
    if isinstance(deck, Deck2.Deck):
        dealt, randNum = deck.randCard()
        deck.remCard(randNum)
        return dealt
    else:
        return 'death'

def getValue(card):
    x = 0
    if isinstance(card, str ):
        try:
            if len(card) == 2:
                x = int(card[0])
            else:
                x = 10
        except ValueError:
            if card[0] == 'A':
                return 1
            else:
                return 10
        return x
    else:
        return 'death'

def aceVal():
    print (" do you want the ace to be 11 or 1")
    done = False
    while done == False:
        opt = getUserInput()
        if (opt == '11') or (opt == '1'):
            done = True
            return opt
        else:
            print("you didn't enter a 11 or 1")
            done = False
def sumVals(cards):
    score = 0
    if isinstance(cards, list):
        for i in range(len(cards)):
            value = getValue(cards[i])
            if 1<value<11:
                score += value
            elif value == 1:
                score += int(aceVal())

        return score
    else:
        return 'death'

def blackjack():
    global players
    print()
    print("NEW HAND")
    time.sleep(0.3)
    for i in range(1, len(players)):
        print(players[i][0], ':')
        players[i][2],players[i][3] = placeBet(players[i][2])
        initHand(deck1)
        print ("Your hand is", players[i][1])
        time.sleep(0.5)
        players[i][4] = sumVals(players[i][1])
        print("your score therefore is:" , players[i][4])
        time.sleep(0.5)
        stand = False
        if players[i][4] == 21:
            stand = True
            print("WINNER WINNER, CHICKEN DINENR")
        while stand == False and players[i][4] < 21:
            if len(players[i][1]) == 2 and players[i][1][0][0]==players[i][1][1][0]:
                stand = splitOpt(players[i][1], stand)
                #need to add the opt to split here
            else:
                stand = hit(players[i][1], stand)
            time.sleep(0.5)
            print ("Your hand is", players[i][1])
            players[i][4] = sumVals(players[i][1])
            time.sleep(0.5)
            print("your score therefore is:" , players[i][4])
            if players[i][4] > 21:
                print ("BUST")
            if players[i][4] == 21:
                print("you must stick with 21")
        print()
        print()
    cHand, cPoints = comBlackjack()
    whoWins(cHand,cPoints)    
    
def hit(cards,thingy):
    #the thingy is going to be stand but i want parameter and argument to be different
    print ("""would you like to:
          (1)hit
          (2)stand""")
    try:
        opt = int(getUserInput())
        if 0<opt<3:
            if opt == 1:
                dealt = deal(deck1)
                cards.append(dealt)
                print ("you recieved: ",dealt)
                return False
            if opt == 2:
                return True
        else:
            print("I dont think you entered a 1 or a 2")
            return False
    except ValueError:
        print("i dont think you typed in a number")
        return False
    
def comBlackjack():
    print("now it's the computers  turn")
    time.sleep(1.5)
    hand = [deal(deck1), deal(deck1)]
    print ("computers hand is: ", hand)
    points = sumValsCom(hand)
    time.sleep(0.4)
    stand = False
    while stand == False:
        points = sumValsCom(hand)
        print("the score therefore is:" , points)
        if len(hand) == 2 and int(points) == 21:
            stand = True
            print ('WINNER WINNER, CHICKEN DINNER')
        else:
            if int(points) > 16:
                print("the computer stands with the hand", hand)
                print ('with a score of', points)
                stand = True
            else:
                dealt = deal(deck1)
                hand.append(dealt)
                print("the hand now is", hand)
        time.sleep(0.9)
    return hand, points
    
def whoWins(cCards, cScore):
    global players
    print()
    print()
    print()
    print()
    time.sleep(1)
    for i in range (1, len(players)):
        print (players[i][0]+ '\'s hand is:')
        print(players[i][1])
        time.sleep(0.5)
    print('The Dealers hand is:')
    print(cCards)
    time.sleep(0.6)
    for i in range(1, len(players)):
        print()
        print(players[i][0], ':')
        if players[i][4] > 21:
            print ("you are BUST so the Dealer wins")
            players[i][3] = 0
            print("you now have", players[i][2], 'chips')
        elif players[i][4] == 21 and len (players[i][1]) == 2:
            print("YOU WIN")
            players[i][2] = players[i][2] + int(players[i][3] * 2.5)
            players[i][3] = 0
            print("you now have", players[i][2],'chips')
        else:
            if players[i][4] > cScore:
                print("YOU WIN")
                players[i][2] = players[i][2] + players[i][3] * 2
                players[i][3] = 0
                print("you now have", players[i][2], 'chips') 
            elif cScore > 21:
                print("YOU WIN")
                players[i][2] = players[i][2] + players[i][3]*2
                players[i][3] = 0
                print("you now have", players[i][2], 'chips')
            else:
                print("YOU LOSE to the dealer")
                players[i][3] = 0
                print("you now have", players[i][2], "chips")

def placeBet(money):
    #calling chips money just so i have summat different in function
    print("you have", money, "chips")
    time.sleep(0.4)
    done = False
    while done == False:
        print("how much would you like to bet?")
        try:
            stake = int(getUserInput())
            if stake >= 20 and stake <= money:
                done = True
            elif stake < 20:
                done = False
                print("that's below the minimum bet")
            elif stake > money:
                print(" you don't have than many chips")
        except ValueError:
            print("you didn't enter an integer")
            done = False
    print ("you have placed a bet of", stake)
    money = money - stake
    return money, stake

def playerNames():
    for i in range(1, len(players)):
        print('enter '+(players[i][0])+'\'s name?')
        name = getUserInput()
        players[i][0] = name
        print("welcome to the game " + name)
        print()
        if name == 'Breithaupt':
            global deck1
            players[i][0] = 'bob'
            players[i][2] = 10000000000
            deck1 = Deck2.Deck(100)
            
#need to define function before main program thing

def sumValsCom(cards):
    score = 0
    cardVals = []
    if isinstance(cards, list):
        for i in range(len(cards)):
            cardVals.append(getValue(cards[i]))
        cardVals.sort()
        if 1 in cardVals:
            if len(cardVals) == 2:
                if cardVals[1] == 1:
                    return 12
                elif cardVals[1] >= 9:
                    #maybe change to 8
                    return cardVals[1] + 11
                else:
                    return cardVals[1] + 1
            else:
                aces = []
                noAScore = 0
                for i in range(cardVals.count(1)):
                    aces.append(1)
                    cardVals.remove(1)
                for i in range(len(cardVals)):
                    noAScore += cardVals[i]
                if max(cardVals)==10:
                    for i in range(len(aces)):
                        noAScore += 1
                    return noAScore
                elif 11>sum(cardVals)>7:
                    if len(aces) == 1:
                        return noAScore+11
                    elif len(aces) == 2 and sum(cardVals) != 10:
                        return noAScore +12
                    elif len(aces) > 2:
                        return noAScore + len(aces)
                else:
                    return noAScore + len(aces)       
        else:
            return sumVals(cards)

def newDeck():
    print("a new deck is being created")
    n = int(input("how many 52's in this deck"))
    #basically what multiplied by 52 for the deck
    #how many decks in the deck
    #need a better way to phrase this
    deck1 = Deck2.Deck(n)

def splitOpt(cards,thingy):
    print("you have two "+cards[0][0]+'s')
    print("would you like to split? Y/N")
    opt = getUserInput().lower()
    if opt == 'y':
        print("i'll work on this later")
        time.sleep(2)
        return hit(cards, thingy)
    else:
        return hit(cards, thingy)
def timeNDate():
    print("Todays date is:", time.gmtime()[2],'/',time.gmtime()[1],'/',time.gmtime()[0])
    print("The time is:", time.gmtime()[3],':',time.gmtime()[4],':',time.gmtime()[5])

def getUserInput():
    inp = input()
    if inp == 'time':
        timeNDate()
    elif inp == 'UP UP DOWN DOWN LEFT RIGHT LEFT RIGHT B A':
        print('KONAMI CODE ENTERED')
        print('hopefully in the future there\'ll be 1000 added to your player')
    return inp

players = [['playerNum', 'hand', 'chips', 'bet', 'score']]
deadPlayers = []
print("this game was created by Akmal Khalil")
print("NOTE: IF TIE, DEALER WINS BY DEFAULT")
time.sleep(0.6)
print("MINIMUM BET IS 20")
time.sleep(0.6)
print("each player begins with 100 chips")
time.sleep(0.6)
print("Every time your score is calculated with an ace,\nyou must tell the computer whether it's a 1 or 11")
time.sleep(0.8)
print()
print("WELCOME TO BLACKJACK")
print()
timeNDate()
time.sleep(1)
for i in range(3):
    print()
deck1 = Deck2.Deck(numOfPlayers())
while True :
    blackjack()
    time.sleep(0.5)

    for i in range(1,len(players)):
        if players[i][2] <20:
            print()
            print(players[i][0] + ', you no longer have enough chips to play')
            print()
            deadPlayers.append(players[i])
    for i in range(len(deadPlayers)):
        if deadPlayers[i] in players:
            players.remove(deadPlayers[i])
    if len(deck1.cardsList) < (len(players)*5):
        print("sorry there are not enough cards left in this deck")
        time.sleep(0.3)
        for i in range(1,len(players)):
            print(players[i][0])
            print("you have ",players[i][2], "chips remaining")
            time.sleep(0.2)
        break
    if len(players) == 1:
        print('NO PLAYERS LEFT')
        break
print()
print()
print("DEAD PLAYERS")
for i in range(len(deadPlayers)):
    print(deadPlayers[i][0])
print("PLAYER WITH CHIPS REMAINING")
for i in range(1,len(players)):
    print(players[i][0])
#well now what can i do


#ok work on split (start with two cards which are same face)
#maybe five card trick if thats a thing in blackjack
    #it may just be in pontoon so i'll need to check that
