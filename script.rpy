# The script of the game goes in this file.

init:
    transform flip:
        xzoom -1.0

init:
    transform midleft:
        xalign 0.18
        yalign 1.0

init:
    transform midright:
        xalign 0.80
        yalign 1.0

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
        # def __getattr__(self, name):
        #     if name == 'bap':
        #         return "#FF8BAF"
        #     elif name == 'fle':
        #         return "#FFB06A"
        #     elif name == 'vi':
        #         return "#6A91FF"
        #     elif name == 'pr':
        #         return "#8569A9"
        #     else:
        #         return "#ffffff"
        #         raise AttributeError(f"'Color' object has no attribute '{name}'")

define col = Colors()

define bap = Character("Бапуся", color=col.bap)
define fle = Character("Флэшмобщик", color=col.fle)
define vi = Character("/выебал/", color=col.vi)
define pr = Character("Пронзатор", color=col.pr)


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene rainbow

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bap at midright
    # show fle at left
    # show vi at right
    # show pr at midleft
    show fle at midleft:
        flip

    # These display lines of dialogue.
 
    fle "Hi Bapusya"

    bap "H-Hi..."
    
    hide fle
    
    bap "/sigh/ He left... \nI'm gonna go too"

    hide bap
    show bap at midright:
        flip

    bap "/leaves/" 

    # This ends the game.

    return
