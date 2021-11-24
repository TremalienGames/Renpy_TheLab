################################################################################
## Game Flags
################################################################################
default visited_lab_robot_room = False
default completed_sceneOne = False
default intro_complete = False
default main_menu_flag = True
default show_dialog = True
default knows_name = False
default met_worker_mech = False
################################################################################
## General Variables
################################################################################
default topics = ["who","where"]
default startinglab_choices = ["door","arrow"]
default robot_room_choices = ["where","how"]
default inventory_list = [""]
default adam_meaning = "Automated Domestic Assault Machine"
default player_position = "sitting"
default what_text = "nothing"
default crawling_image =  "gui/crawling.png"
default standing_image =  "gui/standing.png"
default current_postion_image = crawling_image

################################################################################
## Images
################################################################################
image startingLab = im.Scale("bg_startinglab.png",1280,720)
image robotLab = im.Scale("bg_lab_robotroom.png",1280,720)
image destructionVision = im.Scale("images/scene_one/bg_destruction.png",1280,720)
image robot deactivated = "images/scene_one/robot_deactivated.png"
image robot without arm = "images/scene_one/robot_without_arm.png"
image robot powered down = "images/scene_one/robot_powered_down.png"
image bg_lab_robotroom_empty = im.Scale("images/scene_one/bg_lab_robotroom_empty.png",1280,720)
image bg_lab_robotroom_missing_arm = im.Scale("images/scene_one/bg_lab_robotroom_missing_arm.png",1280,720)
image bg_lab_robotroom_missing_broom = im.Scale("images/scene_one/bg_lab_robotroom_missing_broom.png",1280,720)
image bg_lab_robotroom = im.Scale("images/scene_one/bg_lab_robotroom.png",1280,720)
################################################################################
## Sound Effects
################################################################################
default sfx_glitch = "audio/sfx_glitch.ogg"
default sfx_grunt_effort = "audio/sfx_grunt_effort.ogg"
default sfx_grunt_pain = "audio/sfx_grunt_pain.ogg"
default sfx_electric_glitch = "audio/sfx_electric_glitch.ogg"
default sfx_bionic_wave = "audio/sfx_bionic_wave.ogg"
default sfx_rip_arm = "audio/sfx_rip_arm.ogg"
default sfx_power_down = "audio/sfx_power_down.ogg"
default sfx_med_spray = "audio/sfx_med_spray.ogg"
################################################################################
## Player Stats
################################################################################
default player_health = 20
default player_temperment = 0
default player_corruption = 0
default player_health_text = "beat up"
default player_temperment_text = "content"
default player_corruption_text = "courteous"

label calculate_player_stats:
    if player_health > 40:
        $player_health_text = "healthy"
    elif player_health > 30:
        $player_health_text = "okay"
    elif player_health > 20:
        $player_health_text = "worn down"
    elif player_health > 10:
        $player_health_text = "beat up"
    elif player_health > 5:
        $player_health_text = " in extreme pain"
    else:
        $player_health_text = "near death"

    if player_temperment > 20:
        $player_temperment_text = "happy"
    elif player_temperment > 10:
        $player_temperment_text = "hopeful"
    elif player_temperment >= 0:
        $player_temperment_text = "content"
    elif player_temperment > -5:
        $player_temperment_text = "annoyed"
    elif player_temperment > -10:
        $player_temperment_text = "angry"
    else:
        $player_temperment_text = "furious"

    if player_corruption > 20:
        $player_corruption_text = "self-sacrificing"
    elif player_corruption > 10:
        $player_corruption_text = "helpful"
    elif player_corruption >= 0:
        $player_corruption_text = "courteous"
    elif player_corruption > -5:
        $player_corruption_text = "guarded"
    elif player_corruption > -10:
        $player_corruption_text = "selfish"
    else:
        $player_corruption_text = "self-serving"

    return
