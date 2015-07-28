#!/usr/bin/python
import sys
import random
import pygame
import re
from PIL import Image
from pygame.locals import *
def getCards():
    global deck, values, suits
    values = '2 3 4 5 6 7 8 9 10 j q k 1'.split()
    suits = 'c d h s'.split()
    deck = ["%s%s" % (v, s) for v in suits for s in values]
def shuffleDeck():
    global deck
    s = 1
    random.seed()
    while s <= 3: 
        random.seed()
        random.shuffle(deck)
        s += 1
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 512))
    pygame.display.set_caption('5 Card Draw')
    # Fill background
    background = pygame.Surface(screen.get_size())
    background2 = pygame.Surface(screen.get_size())
    background = background.convert()
    background2 = background.convert()
    background.fill((39, 119, 20))
    background2.fill((39, 119, 20))
    card1 = Image.open("cards/%s.png" % (deck[0])) ; card1 = card1.convert("RGBA")
    card2 = Image.open("cards/%s.png" % (deck[1])) ; card2 = card2.convert("RGBA")
    card3 = Image.open("cards/%s.png" % (deck[2])) ; card3 = card3.convert("RGBA")
    card4 = Image.open("cards/%s.png" % (deck[3])) ; card4 = card4.convert("RGBA")
    card5 = Image.open("cards/%s.png" % (deck[4])) ; card5 = card5.convert("RGBA")
    back = Image.open("cards/back.png") ; back = back.convert("RGBA")
    dbb = Image.open("cards/over.png") ; dbb = dbb.convert("RGBA")
    m = card1.mode
    s = card1.size
    data1 = card1.tostring()
    data2 = card2.tostring()
    data3 = card3.tostring()
    data4 = card4.tostring()
    data5 = card5.tostring()
    card1b = pygame.image.fromstring(data1, s, m)
    card2b = pygame.image.fromstring(data2, s, m)
    card3b = pygame.image.fromstring(data3, s, m)
    card4b = pygame.image.fromstring(data4, s, m)
    card5b = pygame.image.fromstring(data5, s, m)
    bm = back.mode
    bs = back.size
    bd = back.tostring()
    bb=b1=b2=b3=b4=b5= pygame.image.fromstring(bd, bs, bm)
    db = dbb.tostring()
    re = pygame.image.fromstring(db, bs, bm)
    background.blit(bb, (700, 350)); background2.blit(bb, (700, 350));
    background.blit(bb, (702, 352)); background2.blit(bb, (702, 352));
    background.blit(bb, (704, 354)); background2.blit(bb, (704, 354));
    background.blit(bb, (706, 356)); background2.blit(bb, (706, 356));
    pos1=pos2=pos3=pos4=pos5=bb.get_rect(topleft=(700, 350))
    def deal(obj, pos, mx, my, obj2):
            for x in range(10):
                screen.blit(background, (0, 0))
                pos = pos.move(mx,  my)
                screen.blit(obj, pos)
                pygame.display.update()
            background.blit(obj2, pos)
            background2.blit(obj, pos)

    def retract(obj, pos, mx, my):
         for x in range(10):
                screen.blit(background2, (0, 0))
                pos = pos.move(mx,  my)
                screen.blit(obj, pos)
                pygame.display.update()
                screen.blit(background2, (0, 0))
    pygame.time.wait(100)
    deal(b1, pos1, -60, -20, card1b)
    deal(b2, pos2, -50, -20, card2b)
    deal(b3, pos3, -40, -20, card3b)
    deal(b4, pos4, -30, -20, card4b)
    deal(b5, pos5, -20, -20, card5b)
    pos1=bb.get_rect(topleft=(100, 150))
    pos2=bb.get_rect(topleft=(200, 150))
    pos3=bb.get_rect(topleft=(300, 150))
    pos4=bb.get_rect(topleft=(400, 150))
    pos5=bb.get_rect(topleft=(500, 150))
    handvalues = " " + deck[0][1:] + " " + deck[1][1:] + " " + deck[2][1:] + " " + deck[3][1:] + " " + deck[4][1:] + " "
    handsuits  = " " + deck[0][:1] + " " + deck[1][:1] + " " + deck[2][:1] + " " + deck[3][:1] + " " + deck[4][:1] + " "
    font = pygame.font.Font(None, 36)
    rf = font.render("ROYAL FLUSH", 1, (0, 255, 255))
    sf = font.render("STRAIGHT FLUSH", 1, (0, 255, 200))
    fk = font.render("FOUR OF A KIND", 1, (0, 255, 150))
    fh = font.render("FULL HOUSE", 1, (0, 255, 100))
    fl = font.render("FLUSH", 1, (0, 255, 75))
    st = font.render("STRAIGHT", 1, (0, 255, 50))
    tk = font.render("THREE OF A KIND", 1, (0, 255, 0))
    tp = font.render("TWO PAIR", 1, (12, 255, 0))
 
    textpos = rf.get_rect(center=(400, 450))
    straights=["[k|q|j|10|9]", "[q|j|10|9|8]", "[j|10|9|8|7]", 
               "[10|9|8|7|6]", "[9|8|7|6|5]" , "[8|7|6|5|4]" , 
               "[7|6|5|4|3]", "[6|5|4|3|2]"]

    def isRoyal():
        global isRoyal
        if handvalues == "a k q j 10":
            if 5 in {handsuits.count('c'), handsuits.count('d'), handsuits.count('s'), handsuits.count('h')}:
                background.blit(rf, textpos)
                isRoyal = (0 == 0)
    def isStraightFlush():
        global isStraightFlush
        if isRoyal: return
        if 5 in {handsuits.count('c'), handsuits.count('d'), handsuits.count('s'), handsuits.count('h')}:
            for x in straights:
                reg = re.compile(x)
                if reg.match(handvalues):
                    background.blit(sf, textpos)
                    isStraightFlush = (0 == 0)
    def isFourKind():
        for x in values:
            if handvalues.count(' ' + x + ' ') == 4:
                background.blit(fk, textpos)
    def isFullHouse():
        for x in values:
            if handvalues.count(' ' + x + ' ') == 3:
                for y in values:
                    if handvalues.count(y) == 2:
                        background.blit(fh, textpos)
                        return
    def isFlush():
        if isRoyal: return
        if isf: return
        if 5 in {handsuits.count('c'), handsuits.count('d'), handsuits.count('s'), handsuits.count('h')}:
            background.blit(fl, textpos)
            return
    def isStraight():
        if isRoyal: return
        if isStraightFlush: return
        for x in straights:
            reg = re.compile(x)
            if reg.match(handvalues):
                background.blit(st, textpos)
                return
    def isThreeKind():
        for x in values:
            if handvalues.count(' ' + x + ' ') == 3:
                background.blit(tk, textpos)
                return
    def isTwoPair():
        global itp
        itp = (0 == 1)
        for x in values:
            if handvalues.count(' ' + x + ' ') == 2:
                firstPair = x
                itp = (0 == 1)
                for y in values:
                    if y is not firstPair:
                        if handvalues.count(y) == 2:
                            background.blit(tp, textpos)
                            itp = (0 == 0)
                            return
    def isPair():
        global ip
        cond = itp
        ip = (0 == 1)
        if not itp:
            for x in values:
                if handvalues.count(' ' + x + ' ') == 2:
                    if x == "k":
                        x = "KING"
                    if x == "q":
                        x = "QUEEN"
                    if x == "j":
                        x = "JACK"
                    if x == "1":
                        x = "ACE"
                    background.blit(font.render("PAIR OF %sS" % (x), 1, (100, 255, 0)), textpos)
                    ip = (0 == 0)
                    if itp:
                        ip = (0 == 0)
                        return
      
    isRoyal()
    isStraightFlush()
    isFourKind()
    isFullHouse()
    isFlush()
    isStraight()
    isThreeKind()
    isTwoPair()
    isPair()
    if not ip and not itp:
            if 'k' in handvalues: background.blit(font.render("KING HIGH", 1, (255, 255, 0)), textpos)
            elif 'q' in handvalues: background.blit(font.render("QUEEN HIGH", 1, (255, 255, 0)), textpos)
            elif 'j' in handvalues: background.blit(font.render("JACK HIGH", 1, (255, 255, 0)), textpos)
            elif '10' in handvalues: background.blit(font.render("10 HIGH", 1, (255, 200, 0)), textpos)
            elif '9' in handvalues: background.blit(font.render("9 HIGH", 1, (255, 150, 0)), textpos)
            elif '8' in handvalues: background.blit(font.render("8 HIGH", 1, (255, 100, 0)), textpos)
            elif '7' in handvalues: background.blit(font.render("7 HIGH", 1, (255, 50, 0)), textpos)
            elif '6' in handvalues: background.blit(font.render("6 HIGH", 1, (255, 0, 0)), textpos)
  

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

	# Event loop
    while 1:
    	for event in pygame.event.get():
                keys = pygame.key.get_pressed()
    		if event.type == QUIT:
    			return
                if event.type == KEYDOWN:
                    screen.blit(background2, (0, 0))
                    if event.key==pygame.K_r:
                        screen.blit(background, (0, 0))
                        pygame.time.wait(100) ; screen.blit(bb, (100, 150)) ; pygame.display.update()
                        pygame.time.wait(100) ; screen.blit(bb, (200, 150)) ; pygame.display.update()
                        pygame.time.wait(100) ; screen.blit(bb, (300, 150)) ; pygame.display.update()
                        pygame.time.wait(100) ; screen.blit(bb, (400, 150)) ; pygame.display.update()
                        pygame.time.wait(100) ; screen.blit(bb, (500, 150)) ; pygame.display.update()

                        background2.blit(re, (100, 150)) ; retract(b1, pos1, 60, 20)
                        background2.blit(re, (200, 150)) ; retract(b2, pos2, 50, 20)
                        background2.blit(re, (300, 150)) ; retract(b3, pos3, 40, 20)
                        background2.blit(re, (400, 150)) ; retract(b4, pos4, 30, 20)
                        background2.blit(re, (500, 150)) ; retract(b5, pos5, 20, 20)
                        getCards()
                        shuffleDeck()
                        main()
	screen.blit(background, (0, 0))
getCards()
shuffleDeck()
if __name__ == '__main__': main()
