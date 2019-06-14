from anim_utils import *
from animDict import gen_anim_list
import pandas as pd

"""
Load a df of postures and display on the simulator without interpolation.
For conditioned animations. Both grid and gaussian sampling. VA or V_only

"""


def main(motion_ses, leds_ses, idAnim):

    nameAnim = gen_anim_list[idAnim]
    script_dir = os.path.dirname(__file__)
    rel_path = 'naoqi_data'
    anim_dir = os.path.join(script_dir, rel_path, nameAnim)

    df = pd.read_csv(anim_dir, index_col=0, skipinitialspace=True)

    df = df.astype('float')
    # if 'valence' in df.columns:
    #     valence = df['valence'].mean()
    #     print("Valence: " + str(valence))
    # print("Anim: " + nameAnim)

    # Add StandInit frame at the end of the animation
    last_idx = len(df)
    df.loc[last_idx, joints_names] = standInit
    df.loc[last_idx, leds_keys] = 1

    df['KneePitch'] = -1.49414
    motion_ses.setStiffnesses("WholeBody", 1)

    # Play animation
    for i in range(df.shape[0]):

        angle_list = df.loc[i, joints_names].tolist()
        leds_list = df.loc[i, leds_keys].tolist()
        rgb_chunks = [leds_list[x * 3:(x + 1) * 3] for x in range((len(leds_list) + 3 - 1) // 3)]

        # 16 LEDs, with a 3 RGBs
        for l in range(16):
            leds_ses.fadeRGB(leds_short[l], rgb_chunks[l][0], rgb_chunks[l][1], rgb_chunks[l][2], 0., _async=True)

        # Motion
        motion_ses.setAngles(joints_names, angle_list, 0.05)
        # TODO: Remove for real robot
        time.sleep(0.04)

    time.sleep(1)
    return nameAnim

