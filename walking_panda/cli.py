import panda
import argparse 

def cliproc():
    parser = argparse.ArgumentParser(prog="walking_panda")
    parser.add_argument("--no-rotate", help = "Suppress Rotation"
                        , action= "store_true")
    args = parser.parse_args()

    walking = panda.WalkingPanda(**vars(args))
    walking.run()