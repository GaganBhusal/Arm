# MuJoCo Robot Arm + Wrist Camera

<img src="Images/model.png" width="48%" />
<img src="Images/cam.png" width="48%" />

Left: 3D view  Right: egocentric camera feed (`hand_cam`)

Camera uses `mode="trackcom"` → always looks forward, never flips, even after full 180°/360° arm rotation.

Run:
```bash
python arm.py
