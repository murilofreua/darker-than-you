# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rocha")

image rocha normal = im.Scale("rocha.png", 680, 540)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene centro

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rocha normal at truecenter

    # These display lines of dialogue.

    r "Prazer em conhecê-lo, Dante. Espero que aproveite sua estadia."

    # This ends the game.

    return
