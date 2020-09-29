#!/usr/bin/env python
# coding: utf-8

import argparse
from frames_generation import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generating frames from videos and doing reverse image search of frames')
    parser.add_argument('--video_filename', required = True,help = "Name of video with extension")
    
    args = parser.parse_args()
    frames_gen(args.video_filename)





