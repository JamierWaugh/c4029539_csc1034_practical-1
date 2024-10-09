import panda
import argparse 

def cliproc(): #Renamed to avoid error with calling imports as names clashed
    parser = argparse.ArgumentParser(prog="walking_panda") #Type below arguments appended to "python walking-panda.py" + arg to run code with argument
    parser.add_argument("--no-rotate", help = "Suppress Rotation"
                        , action= "store_true") #No rotate of camera
    parser.add_argument("--scale",help = "Increase scale"
                        , type=float, default = 1.0) #Increase scale of panda
    parser.add_argument("--no-walk", help = "Suppress Walking"
                        , action = "store_true") #Stop panda from walking
    parser.add_argument("--baby-panda", help="Loading second panda"
                        ,action = "store_true") #Create mother and child panda
    parser.add_argument("--baby-no-rotate", help="No rotate and baby"
                        ,action = "store_true") #Baby and no rotate
    args = parser.parse_args() #Parse all arguments called

    walking = panda.WalkingPanda(**vars(args)) #load all arguments into panda
    walking.run() #run the software