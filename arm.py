import mujoco
import mujoco.viewer

import cv2

model = mujoco.MjModel.from_xml_path("arm.xml")
data = mujoco.MjData(model)


renderer = mujoco.Renderer(model, height=480, width=480)
renderer2 = mujoco.Renderer(model, height=480, width=480)


with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        
        renderer.update_scene(data, camera="world_cam")
        renderer2.update_scene(data, camera="hand_cam")
        img = renderer.render()
        img2 = renderer2.render()
        cv2.imshow("Cam", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
        cv2.imshow("Hand", cv2.cvtColor(img2, cv2.COLOR_RGB2BGR))

        if cv2.waitKey(1) == 27: 
            break
        viewer.sync()

