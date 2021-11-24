image video_clip = Movie(play="fire.ogv")

screen StatsUI:

    frame:
        background "gui/hud_status.png"
        xalign .87
        yalign 0.025

        vbox:
            xpos 25
            ypos 10
            spacing -20
            text "Physically: [player_health_text]" color "c3cad6" size 25
            text "Emotionally: [player_temperment_text]" color "c3cad6" size 25
            text "Socially: [player_corruption_text]" color "c3cad6" size 25


screen VideoClip:
    frame:
        xalign .5
        yalign .5
        xsize 500
        vbox:
            xalign .5
            text "video"
            add "video_clip"
            button:
                text "Close"
                action Return()
