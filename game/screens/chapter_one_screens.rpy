

screen starting_lab_nav():
    add "bg_startinglab"
    modal True

    ################################################################## HUD FRAMES
    frame:
        background current_postion_image
        xpos 1170
        ypos 18

    frame:
        background "gui/hud_status.png"
        xpos 860
        yalign 0.025

        vbox:
            xpos 25
            ypos 10
            spacing -20
            text "Physically: [player_health_text]" color "c3cad6" size 25
            text "Emotionally: [player_temperment_text]" color "c3cad6" size 25
            text "Socially: [player_corruption_text]" color "c3cad6" size 25

    #############################################################################

    imagebutton auto "bg_startinglab_vine_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip","Reach for the ladder")
        unhovered SetVariable ("screen_tooltip","")
        action Return("ladder")

    imagebutton auto "bg_startinglab_door_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip","Head for the door")
        unhovered SetVariable ("screen_tooltip","")
        action Return("door")

    imagebutton auto "bg_startinglab_arrow_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip","Arrow")
        unhovered SetVariable ("screen_tooltip","")
        action Return("arrow")






screen starting_lab_robot_room_nav():

    if "mech_arm" in inventory_list and "broom" in inventory_list:
        add "bg_lab_robotroom_empty"
    elif "mech_arm" in inventory_list:
        add "bg_lab_robotroom_missing_arm"
    elif "broom" in inventory_list:
        add "bg_lab_robotroom_missing_broom"
    else:
        add "bg_lab_robotroom"

    modal True

    ################################################################## HUD FRAMES
    frame:
        background current_postion_image
        xpos 1170
        ypos 18

    frame:
        background "gui/hud_status.png"
        xpos 860
        yalign 0.025

        vbox:
            xpos 25
            ypos 10
            spacing -20
            text "Physically: [player_health_text]" color "c3cad6" size 25
            text "Emotionally: [player_temperment_text]" color "c3cad6" size 25
            text "Socially: [player_corruption_text]" color "c3cad6" size 25

    #############################################################################

    if "broom" not in inventory_list:
        imagebutton auto "bg_lab_robotroom_broom_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip","Broom")
            unhovered SetVariable ("screen_tooltip","")
            action Return("broom")

    if "mech_arm" not in inventory_list:
        imagebutton auto "bg_lab_robotroom_robot_%s":
            focus_mask True
            hovered SetVariable("screen_tooltip","Robot")
            unhovered SetVariable ("screen_tooltip","")
            action Return("robot")

    imagebutton auto "bg_lab_robotroom_arrow_%s":
        focus_mask True
        hovered SetVariable("screen_tooltip","Arrow")
        unhovered SetVariable ("screen_tooltip","")
        action Return("arrow")


screen robot_close_up:
    add "bg_lab_robot_closeup"
