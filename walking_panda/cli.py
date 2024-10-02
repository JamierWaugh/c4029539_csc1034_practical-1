import panda
import argparse 

def cliproc():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help = "Suppress Rotation"
                        , action= "store_true") #No rotate of camera
    parser.add_argument("--scale",help = "Increase scale"
                        , action="store_true") #Increase scale of panda
    parser.add_argument("--no-walk", help = "Suppress Walking"
                        , action = "store_true") #Stop panda from walking
    parser.add_argument("--baby-panda", help="Loading second panda"
                        ,action = "store_true") #Create mother and child panda
    parser.add_argument("--baby-no-rotate", help="No rotate and baby"
                        ,action = "store_true") #Baby and no rotate
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()