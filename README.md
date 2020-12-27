# rotate_pose
Aligns SLAM output position output with AirSim groundtruth based on camera orientation and SLAM coordinate system.

# Guide
Input odometry results must be in TUM format.
Roll, pitch, yaw values are based on camera settings set in `~/Documents/settings.json` file

Run using
```
  python3 ~/FILE.py INPUT.txt OUTPUT.txt ROLL PITCH YAW # angle in degrees

```
