gitscreen StatsUI:

    frame:
        background "gui/hud_status.png"
        xalign 1.0
        yalign 0.0
        xpadding 30
        ypadding 30

        hbox:
            text "[player_health_text]"
            spacing 40

            vbox:
                spacing 10
                text "Health" size 40
                text "Temperment" size 40
                text "Corruption" size 40
                text "Position" size 40

            vbox:
                spacing 10
                text "[player_health]" size 40
                text "[player_temperment]" size 40
                text "[player_corruption]" size 40
                text "[player_position]" size 40


    textbutton "Hide Stats":
        xalign 1.0
        yalign 0.0
        xoffset - 30
        yoffset 30
        action Return()

screen starting_lab_nav():
    add "bg_startinglab"
    modal True

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

    textbutton "View Stats":
        xalign 1.0
        yalign 0.0
        xoffset - 30
        yoffset 30
        action ShowMenu("StatsUI")

    #imagebutton auto "UI/stats_%s.png":
        #xalign 1.0
        #yalign 0.0
        #xoffset - 30
        #yoffset 30
        #action ShowMenu("StatsUI")


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
