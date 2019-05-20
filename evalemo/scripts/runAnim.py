#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use run Method"""

import qi
import argparse
import sys
import random
import os
from animDict import anim_list
from anim_utils import *


def main(session, idAnim):
    motion_ses, aplayer_ses, posture_ses, leds_ses, alife_ses = load_modules(session)
    # Resting state
    init_rest(leds_ses, alife_ses, posture_ses)
    # motion_service = session.service("ALMotion")
    animation_player_service = session.service("ALAnimationPlayer")
    # posture_service = session.service("ALRobotPosture")
    tabletService = session.service("ALTabletService")
    # leds_service = session.service("ALLeds")

    anim_dir = anim_list[idAnim].split('/')
    nameAnim = anim_dir[len(anim_dir) - 1]
    print("\n=============================    Id of the anim: " + str(idAnim))
    print("\n=============================    Name of anim: " + str(nameAnim) + "\n")

    try:
        tabletService.hideWebview()
    except Exception, e:
        print
        "Error was: ", e
        # play an animation, this will return when the animation is finished
    # animation_player_service.run("animations/Stand/Gestures/Hey_1")
    animation_player_service.run("plymouth-animations-7d137f/" + anim_list[idAnim])

    go_2_init(posture_ses)
    leds_ses.reset("FaceLeds")
    time.sleep(3)

    return nameAnim
