import qi
import sys, os
import time
import pandas as pd
from anim_settings import *


def naoqi_connect(str_ip='127.0.0.1', n_port=41807):

    naoqi_session = qi.Session()
    try:
        naoqi_session.connect("tcp://" + str_ip + ":" + str(n_port))
        return naoqi_session
    except RuntimeError:
        print("Can't connect to Naoqi")
        sys.exit(1)


def go_2_init(posture_ses):
    posture_ses.goToPosture("StandInit", 0.05)


def load_modules(session):
    motion_ses = session.service("ALMotion")
    aplayer_ses = session.service("ALAnimationPlayer")
    posture_ses = session.service("ALRobotPosture")
    leds_ses = session.service("ALLeds")
    alife_ses = session.service("ALAutonomousLife")

    return motion_ses, aplayer_ses, posture_ses, leds_ses, alife_ses


def init_rest(leds_ses, alife_ses, posture_ses):
    leds_ses.reset("FaceLeds")
    go_2_init(posture_ses)
    alife_ses.setAutonomousAbilityEnabled("BasicAwareness", False)
    alife_ses.setAutonomousAbilityEnabled("ListeningMovement", False)
    alife_ses.setAutonomousAbilityEnabled("SpeakingMovement", False)
    alife_ses.setAutonomousAbilityEnabled("BackgroundMovement", False)
    autoState = alife_ses.getState()
    if autoState != "disabled":  # disable
        alife_ses.setState("disabled")
        posture_ses.goToPosture("StandInit", 0.6)


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]