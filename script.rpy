# The script of the game goes in this file.

init:
    transform flip:
        xzoom -1.0

init:
    transform flipback:
        xzoom 1.0

init:
    transform midleft:
        xalign 0.18
        yalign 1.0

init:
    transform midright:
        xalign 0.80
        yalign 1.0

# init:
    # transform walk(start, end, tall):
    #     xpos start ypos 0 xanchor 0.5 yanchor 0
    #     linear 0.5 xpos end

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    class Colors:
        bap = ""
        fle = ""
        vi = ""
        pr = ""

        def __init__(self):
            self.bap = "#FF8BAF"
            self.fle = "#FFB06A"
            self.vi = "#6A91FF"
            self.pr = "#8569A9"

define col = Colors()

define bap = Character("Бапуся", color=col.bap)
define fle = Character("Флэшмобщик", color=col.fle)
define vi = Character("/выебал/", color=col.vi)
define pr = Character("Пронзатор", color=col.pr)




# The game starts here.
define e = Character("scolar", color="#F86983")
default question_tally = 0       


label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg rainbow

    show bap at midright
    show fle at midleft:
        flip

    # These display lines of dialogue.
 
    fle "Hi Bapusya"

    bap "H-Hi..."
    
    hide fle
    
    bap "/sigh/ He left... \nShould I go too?"

    # hide bap
    # show bap at midright:
    #     flip

    # bap "/leaves/" 
    
    # hide bap

    # This ends the game.

    label the_question: 
        e "Should I {i}leave{/i} or should I {i}stay{/i}?"
        call question_selector
        show bap at left with move:
            flip

        menu:                                               #SCREEN 3
            "Stay":           
                show bap at midright with move:  #SCREEN 4-1
                    flipback
                # $ animal = 'fox'
                bap "{i}/sigh/{/i}Okay, maybe I should wait..."
            "Leave":                                 #Stay
                # hide bap                   #SCREEN 4-1
                # $ animal = 'dog'
                show bap at left with ease:  #SCREEN 4-1
                    flipback
                bap "Yeah, I guess I'll leave..."
                # hide bap with move
                hide bap 
                # bap "{b}Yeah{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
            "[repeat_question] Could you repeat the question?": #SCREEN 4-3
                jump the_question
        jump end

label question_selector:
    $ NumberGenerator = renpy.random.randint(1, 3)
    if NumberGenerator == 3:
        $ repeat_question = "What?"
    elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
        $ repeat_question = "Say that again?"
    else:
        $ repeat_question = "Huh?"
    # $ repeat_question = renpy.random.choice(["What?", "Say that again?", "Huh?"])
    $ question_tally += 1
    return

label end:                                                  #SCREEN 5
    # play music "audio/renpyallstars.ogg"
    # scene concert1 with vpunch:                             #new scene
    #     zoom 0.55
    "The End!"
    return

