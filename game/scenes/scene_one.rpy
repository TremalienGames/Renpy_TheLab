default seen_broom = False
default is_robot_deactivated = False

label scene_one_phase_one:

    scene bg_startinglab with dissolve
    play music "audio/bgm_scene_one.mp3" fadein 1.0 volume 0.3

    #call screen VideoClip
    if completed_sceneOne:
        show screen onscreen_hud_stats
    $ topics = ["who","where"]
    $ startinglab_choices = ["door","arrow"]

    "What?"
    "Where am I?"
    "How did I get here?"
    shadow neutral "So you are finally awake"
    "Looking around, you see nobody near you."
    "\"Who said that?\""
    shadow neutral "Stop acting like an idiot and listen. \n\nYou
    are not safe here, you need to get out before they come back."
    shadow neutral "They think you are dead. \n\nOnce they find out you aren't, they will stop at nothing to make sure you are. "

label initial_conversation_topics:
    menu:
        "Who are you?" if "who" in topics:
            $ topics.remove("who")
            $topics.append("me")
            shadow "Who I am is unimportant. The question is, do you know who you are?"
            menu:
                "I know exactly who I am. My name is...I...I don't remember.":
                    $ player_temperment -=1
                    call calculate_player_stats
                    shadow "I'm not surprised you are having difficulty remembering, considering what you've been through."
                "To be honest, I can't remember anything, even my own name.":
                    shadow "I'm not surprised you are having difficulty remembering, considering what you've been through."
            jump initial_conversation_topics
        "Where am I?" if "where" in topics:
            shadow "You are where they left you to die."
            $ topics.remove("where")
            $ topics.append("they")
            jump initial_conversation_topics
        "Do you know who I am?" if "me" in topics:
            shadow "You are adam"
            "\"Adam? My name is Adam?\""
            "\"Something feels off about that.\""
            shadow "That is the least of your concerns right now."
            shadow "You need to get out of this place and start looking for answers."
            $ knows_name = True
            $ topics.remove("me")
            jump initial_conversation_topics
        "Who left me here to die?" if "they" in topics:
            shadow "That is an answer I do not have and one I hope you can discover."
            $topics.remove("they")
            jump initial_conversation_topics

label scene_one_phase_two:

    play sound sfx_glitch
    show destructionVision with dissolve
    with Shake((0, 0, 0, 0), 1.8, dist=15)
    hide destructionVision with dissolve
    "\"What the hell was that?\""
    shadow neutral "I'm sure I don't know what you're talking about."
    shadow "Maybe you should stop stalling and start figuring a way out of here."

label startinglab_choices:
    call screen starting_lab_nav
    if _return == "ladder":
        jump pull_on_ladder
    elif _return == "door":
        jump startinglab_door
    elif _return == "arrow":
        jump startinglab_turn_around

label pull_on_ladder:
    if player_position == "standing":
        "I'm already standing. The ladder wont help me get reach the door."
        jump startinglab_choices
    elif "robot_arm" in inventory_list:
        "If I use the arm, I should be able to reach the ladder."
        play sound sfx_grunt_effort
        shadow "Well done. Now you just need to reach the door."
        $player_position = "standing"
        jump startinglab_choices
    elif "broom" in inventory_list:
        "If I use the broom, I should be able to reach the ladder."
        play sound sfx_grunt_effort
        shadow "Well done. Now you just need to reach the door."
        $player_position = "standing"
        jump startinglab_choices
    else:
        "Maybe I can use the ladder to pull myself to my feet."
        play sound sfx_grunt_pain
        with vpunch
        shadow "That looked pretty painful."
        shadow "It seems the ladder is out of your reach."
        $player_temperment -=1
        $player_health -=1
        call calculate_player_stats
        jump startinglab_choices

label startinglab_door:
    "The door is right there. I'll just walk through it."
    if player_position != "standing":
        play sound sfx_grunt_pain
        with vpunch
        shadow "You're in pretty rough shape right now."
        shadow "You're going to need some help standing up."
        $player_temperment -=1
        $player_health -=1
        call calculate_player_stats
        jump startinglab_choices

label startinglab_turn_around:
    jump robotroom_choices

############################### ROBOT ROOM #####################################
label robotroom_choices:

    if "mech_arm" in inventory_list and "broom" in inventory_list:
        show bg_lab_robotroom_empty
    elif "mech_arm" in inventory_list:
        show bg_lab_robotroom_missing_arm
    elif "broom" in inventory_list:
        show bg_lab_robotroom_missing_broom
    else:
        show bg_lab_robotroom

    if visited_lab_robot_room == False:
        shadow "It looks like there is a deactivated automaton here.\n\nMaybe you can find something useful there." with dissolve
        $visited_lab_robot_room = True

    call screen starting_lab_robot_room_nav

    if _return == "broom":
        jump pickup_broom
    elif _return == "robot":
        jump lab_approach_robot
    elif _return == "arrow":
        jump robotroom_turn_around

label pickup_broom:
    if seen_broom == False:
        "There seems to be an old broom back here."
        $seen_broom = True
    else:
        "That broom is still here."
    menu:
        "I should probably leave the broom where it is.":
            pass
        "Maybe I should grab the broom. It may be useful.":
            $inventory_list.append("broom")
    jump robotroom_choices

label lab_approach_robot:
    if is_robot_deactivated == True:
        "I have already destroyed the worker mech. There is nothing more it can do for me."
        jump robotroom_choices
    else:
        jump robotroom_closeup

label robotroom_turn_around:
    hide bg_lab_robotroom_empty
    hide bg_lab_robotroom_missing_arm
    hide bg_lab_robotroom_missing_broom
    hide bg_lab_robotroom
    jump startinglab_choices

############################### ROBOT CLOSE UP #####################################
label robotroom_closeup:

    show bg_lab_robot_closeup with dissolve
    show robot deactivated with dissolve:
        xalign 0.5
        yalign 0.5

    shadow "It looks like a worker mech. This one was probably used to keep this area clean. \n\n
        Of course that was before someone took it apart."
    shadow "You may as well finish the job and take the arm. \n\n It will probably aid you in getting out of here."
    play sound sfx_electric_glitch
    pause 1
    "\"What's happening?\""
    play sound sfx_electric_glitch
    pause 1
    shadow "I guess it's not completely offline yet. \n\n"
    play sound sfx_bionic_wave
    pause 2
    #show new robot image
    worker_mech "Startup sequence initiated...\nAccessing BIOS settings...\nLoading Kernal...\n"
    shadow "You may want to remove the arm before it's fully activated.\n\n"

    menu:
        "Rip off the arm of the unsuspecting mech":
            jump remove_mech_arm
        "Wait for the mech to come online":
            shadow "Why are waiting? It's just a stupid robot.\n\nTake the arm while you still can."
            menu:
                "Take the arm before it's too late.":
                    jump remove_mech_arm
                "Continue waiting.":
                    pass


    worker_mech "Startup process completed successfully.\n\nHow may I assist you?"

    # DO OTHER STUFF
    #"Looks like I've completely destroyed this mech. There is no way it's going to wake up again."
    #$is_robot_deactivated = True
    #hide screen starting_lab_robot_close_up
    jump robotroom_choices

    label remove_mech_arm:
        hide bg_lab_robotroom
        play sound sfx_rip_arm
        pause .7
        with vpunch
        $inventory_list.append("mech_arm")
        hide robot deactivated
        show robot without arm:
            xalign 0.5
            yalign 0.5
        pause 2
        hide robot without arm
        show robot powered down:
            xalign 0.5
            yalign 0.5
        # REPLACE BACKGROUND
        # REMOVE ROBOT IMAGE MAP
        shadow "It appears to be completely deactivated.\n\nIt seems removing the arm was too much for the system to handle."
        shadow "Now it is a truly useless machine."
        hide robot powered down
        hide bg_lab_robot_closeup
        jump robotroom_choices
