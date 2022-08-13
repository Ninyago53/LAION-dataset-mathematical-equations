
######################################################################################
#                                                                                    #
#   This code was created by me (Ninyago).                                           #
#   The code is free to use.                                                         #    
#   The code was written in German except for some small things that are in English. #
#   Have fun :-)                                                                     #
#                                                                                    #    
######################################################################################  

from random import randint
from PIL import Image, ImageFont, ImageDraw
import os

counter = 0
Ordner = 0

while counter < 20000:

### This paragraph randomly creates simple mathematical equations     

    Anzahl_der_Zahlen = randint(1, 3) 
    counter = counter + 1
    if Anzahl_der_Zahlen == 1 or 2:
        Number1 = randint(1, 100)
        Number2 = randint(1, 100)
        Rechnungszeichen = randint(1, 4) 
        if Rechnungszeichen == 1:
            def get_sum(summand_one, summand_two):
                return summand_one + summand_two
            Result = str(Number1) + " + " + str(Number2)
        if Rechnungszeichen == 2:
            def get_sum(summand_one, summand_two):
                return summand_one - summand_two
            Result = str(Number1) + " - " + str(Number2)
        if Rechnungszeichen == 3:
            def get_sum(summand_one, summand_two):
                return summand_one * summand_two
            Result = str(Number1) + " x " + str(Number2)
        if Rechnungszeichen == 4:
            def get_sum(summand_one, summand_two):
                return summand_one / summand_two
            Result = str(Number1) + " ÷ " + str(Number2)
        sum = get_sum(Number1, Number2)

    if Anzahl_der_Zahlen == 3:
        Rechnungszeichen = randint(1, 9)
        Number1 = randint(1, 125)
        Number2 = randint(1, 125)
        Number3 = randint(1, 125)  
        if Rechnungszeichen == 1:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one + summand_two + summand_three
            Result = str(Number1) + " + " + str(Number2) + " + " + str(Number3)
        if Rechnungszeichen == 2:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one + summand_two - summand_three
            Result = str(Number1) + " + " + str(Number2) + " - " + str(Number3)
        if Rechnungszeichen == 3:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one - summand_two + summand_three
            Result = str(Number1) + " - " + str(Number2) + " + " + str(Number3)
        if Rechnungszeichen == 4:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one + summand_two * summand_three
            Result = str(Number1) + " + " + str(Number2) + " x " + str(Number3)
        if Rechnungszeichen == 5:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one + summand_two / summand_three
            Result = str(Number1) + " + " + str(Number2) + " ÷ " + str(Number3)
        if Rechnungszeichen == 6:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one - summand_two / summand_three
            Result = str(Number1) + " - " + str(Number2) + " ÷ " + str(Number3)
        if Rechnungszeichen == 7:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one - summand_two * summand_three
            Result = str(Number1) + " - " + str(Number2) + " x " + str(Number3)
        if Rechnungszeichen == 8:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one * summand_two / summand_three
            Result = str(Number1) + " x " + str(Number2) + " ÷ " + str(Number3)
        if Rechnungszeichen == 9:
            def get_sum2(summand_one, summand_two, summand_three):
                return summand_one / summand_two * summand_three 
            Result = str(Number1) + " ÷ " + str(Number2) + " x " + str(Number3)
        sum = get_sum2(Number1, Number2, Number3)

### This paragraph has created mathematical equations according to a random principle

    draw_1 = randint(1, 212)
    draw_2 = randint(1, 212)
    draw_3 = randint(1, 255)
    draw_4 = randint(1, 255)
    draw_5 = randint(1, 255)
    draw_6 = randint(1, 255)
    draw_7 = randint(1, 255)
    draw_8 = randint(1, 255)
    draw_9 = randint(10, 60)
    draw_10 = randint(2, 7)
    


    if counter == 1:  
        Ordner = Ordner + 10
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample") 
        os.makedirs(str(Ordner))                                                        # create a Folder
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample/" + str(Ordner))
 
 ####
    if counter%10 == 0:
        Ordner = Ordner + 10
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample")
        os.makedirs(str(Ordner))                                                        #  create a Folder
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample/" + str(Ordner))
        print("Folder was created successfully (" + str(Ordner) + ")")

### This paragraph draws the mathematical equation        

        img = Image.new(mode = "RGB", size = (512, 512), color = (draw_3, draw_4, draw_5))
        img.save(str(counter) + ".jpg")
        img = Image.open(str(counter) + ".jpg")
        draw = ImageDraw.Draw(img)
        if draw_10 == 1:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('Giants.ttf', draw_9)
        if draw_10 == 2:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('Authentic Sheldon.ttf', draw_9)
        if draw_10 == 3:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('Chocolatier Artisanal.ttf', draw_9)
        if draw_10 == 4:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('Joystick.ttf', draw_9)
        if draw_10 == 5:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('JustBubble.ttf', draw_9)
        if draw_10 == 6:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('Spiritual Mountain.ttf', draw_9)
        if draw_10 == 6:
            os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
            myFont = ImageFont.truetype('FreeMono.ttf', draw_9)

### This paragraph draws the mathematical equation

### This paragraph writes the mathematical equation into a txt

        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample/" + str(Ordner))    
        draw.text((draw_1, draw_2), str(Result), font=myFont, fill=(draw_6, draw_7, draw_8))
        img.save(str(counter) + ".jpg") 
        task = randint(1, 2)
        if task == 1:
            file = open(str(counter) + ".1.txt", ("w"))
            file.write(str(sum))
            file.close      
        if task == 2:
            file = open(str(counter) + ".1.txt", ("w"))
            file.write(str(Result) + " = " + str(sum))
            file.close
### This paragraph writes the mathematical equation into a txt

### This paragraph draws the mathematical equation            

    img = Image.new(mode = "RGB", size = (512, 512), color = (draw_3, draw_4, draw_5))
    img.save(str(counter) + ".jpg")
    img = Image.open(str(counter) + ".jpg")
    draw = ImageDraw.Draw(img)
    if draw_10 == 1:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('Giants.ttf', draw_9)
    if draw_10 == 2:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('Authentic Sheldon.ttf', draw_9)
    if draw_10 == 3:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('Chocolatier Artisanal.ttf', draw_9)
    if draw_10 == 4:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('Joystick.ttf', draw_9)
    if draw_10 == 5:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('JustBubble.ttf', draw_9)
    if draw_10 == 6:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('Spiritual Mountain.ttf', draw_9)
    if draw_10 == 6:
        os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/fonts")
        myFont = ImageFont.truetype('FreeMono.ttf', draw_9)

### This paragraph draws the mathematical equation        

### This paragraph writes the mathematical equation into a txt

    os.chdir(r"/home/user/Dokumente/Programmieren/LAION/Github/Projekt-1/exsample/" + str(Ordner))
    draw.text((draw_1, draw_2), str(Result), font=myFont, fill=(draw_6, draw_7, draw_8))
    img.save(str(counter) + ".jpg") 
    task = randint(1, 2)
    if task == 1:
        file = open(str(counter) + ".txt", ("w"))
        file.write(str(sum))
        file.close      
    if task == 2:
        file = open(str(counter) + ".txt", ("w"))
        file.write(str(Result) + " = " + str(sum))
        file.close


### Thank you for using this Code!