image video_clip = Movie(play="fire.ogv")

screen gameUI_OLD:
    imagebutton auto "UI/stats_%s.png":
        xalign 1.0
        yalign 0.0
        xoffset - 30
        yoffset 30
        action ShowMenu("StatsUI")

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
