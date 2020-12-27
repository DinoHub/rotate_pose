#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Rotate trajectory.
"""

import os
import argparse
import numpy as np
import math as m

def Rx(theta):
  return np.array([[ 1, 0           , 0           ],
                   [ 0, m.cos(theta),-m.sin(theta)],
                   [ 0, m.sin(theta), m.cos(theta)]])

def Ry(theta):
  return np.array([[ m.cos(theta), 0, m.sin(theta)],
                   [ 0           , 1, 0           ],
                   [-m.sin(theta), 0, m.cos(theta)]])

def Rz(theta):
  return np.array([[ m.cos(theta), -m.sin(theta), 0 ],
                   [ m.sin(theta), m.cos(theta) , 0 ],
                   [ 0           , 0            , 1 ]])


def main():
    """Align SLAM coordinate system with ground truth
    """
    parser = argparse.ArgumentParser(description="Align ORB-SLAM results with ground truth according to camera orientation in AirSim.")
    parser.add_argument("filename", help = "Trajectory in TUM format.")
    parser.add_argument("output", help = "Output file.")
    
    parser.add_argument("roll", help="Camera Roll.")
    parser.add_argument("pitch", help="Camera Pitch.")
    parser.add_argument("yaw", help="Camera Yaw.")

    args = parser.parse_args()

    roll = float(args.roll)*m.pi/180
    pitch = float(args.pitch)*m.pi/180
    yaw = float(args.yaw)*m.pi/180

    file = open(args.filename, "r")
    newFile = open(args.output, "w")
    
    for line in file:
        values = line.split()
        x = float(values[3])
        y = float(values[1])
        z = float(values[2])
        position =  np.array([[x],[y],[z]])
        position = Rx(roll) @ Ry(pitch) @ Rz(yaw) @ position

        newFile.write("%s %s %s %s %s %s %s %s\n" %(values[0], position[0,0], position[1,0], position[2,0], values[4], values[5], values[6], values[7]))

    file.close
    newFile.close
    print("Saved as " + args.output)

    return

if __name__ == '__main__':
    main()
