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
    transform middle:
        xalign 0.5
        yalign 0.5

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
 
    "/типа общаются/"

    fle "Bye Bapusya"

    bap "{i}Oh.{/i} B-Bye..."
    
    hide fle
    
    bap "{i}/sighs/{/i} He left... \nShould I go too?"

    label the_question: 
        e "Should I {i}leave{/i} or should I {i}stay{/i}?"
        call question_selector
        show bap at left with move:
            flip

        menu:
            "Stay":           
                show bap at midleft with move  #SCREEN 4-1
                bap "{i}/sighs/{/i} Okay, maybe I should wait..."
                call ebir_comes
            "Leave":
                show bap at left with ease:  #SCREEN 4-1
                    flipback
                bap "Yeah, I guess I'll leave..."
                hide bap 
                # bap "{b}Yeah{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
            "[repeat_question] Could you repeat the question?":
                jump the_question
        jump end

label ebir_comes:
    show vi at midright
    vi "Hey there. I'm Vi, short for Viebal. Are you alone here?"
    show bap at left with move
    show vi at right with move
    menu:
        "Yeah, I am. My name is Bapusya, nice to meet you, Vi.":           
            show bap happy at midleft with move
            show vi at midright with move
            bap "Yeah, I am. My name is Bapusya, nice to meet you, Vi."
            show vi smirk at midright
            vi "Nice to meet you, Bapusya."
            show 18 at middle 
        "{i}/shrugs/{/i} I'm waiting for someone, sorry.":
            show bap at left with ease:  #SCREEN 4-1
                flipback
            bap "{i}/shrugs/{/i} I'm waiting for someone, sorry."
            vi "Oh, okay."
            hide bap 
            vi "{i}¯\_(-.-)_/¯{/i} Better luck next time."
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

label end:
    "The End!"
    return

