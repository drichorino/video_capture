#!/usr/bin/env python
# coding: utf-8

import cv2
from collections import defaultdict
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import warnings
import glob
import os
warnings.filterwarnings('ignore')


def frames_gen(video_filename):
    try:
        cwd = os.getcwd()
        #print(cwd)
        video_path = cwd+"/"+video_filename
        #print(video_path)
        # Video Capture Using OpenCV
        cap = cv2.VideoCapture(video_path)
        frame_cnt = int(cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        # Use this for accessing the entire video
        index = 1
        for x in range(frame_cnt):
            ret, frame = cap.read()
            if not ret:
                break
            # Get frame timestamp
            frame_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
            # fetch frame every one sec
            if frame_timestamp >= (index * 100.0):
                index = index + 10   # decides the freq. of frames to be saved
                print(f"++ {index}")
                cv2.imwrite(f"{cwd}/video_frames/frame_{index}.png", frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
        print(e.with_traceback)





