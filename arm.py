import mujoco
import mujoco.viewer

import cv2

model = mujoco.MjModel.from_xml_path("arm.xml")
data = mujoco.MjData(model)


renderer = mujoco.Renderer(model, height=480, width=480)

cam_id = model.camera('hand_cam').id   

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        
        renderer.update_scene(data, camera="hand_cam")
        img = renderer.render()
        cv2.imshow("Cam", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) == 27: 
            break
        viewer.sync()

