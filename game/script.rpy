# The script of the game goes in this file.
#define config.rollback_enabled = False
define config.allow_skipping = False
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 2.0
    pause 2.0
    jump scene_one_phase_one

    # This ends the game.

    return


label splashscreen:
    scene black with dissolve
    pause(1)
    show logo with dissolve
    pause(3)
    hide logo with dissolve
    pause (2)
    return
