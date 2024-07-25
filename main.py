from frontend.window import VideoWindow
from backend.slam import feature_extractor
import cv2
import time
import yaml
import threading
import open3d as o3d
import open3d.visualization.gui as gui

path = 'data/Replica/office0/results/frame000000.jpg'



# read config
config_path = 'configs/base.yaml'
config = yaml.safe_load(open(config_path))

#Initialize backend
app = o3d.visualization.gui.Application.instance
app.initialize()
renderer = VideoWindow()


def _update_thread(renderer, path):
    image_index = 000000
    while not renderer.is_done:
        time.sleep(0.100)
        for image in range(50):
                time.sleep(0.1)
                image_path = path.replace(str(image_index).zfill(6), str(image).zfill(6))
                print(image_path)
                # Load an image
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                keypoints, descriptors = feature_extractor(image)

                # Draw keypoints on the image (for visualization)
                output_image = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0))

                def render_image():
                    op3d_image = o3d.geometry.Image(output_image)
                    renderer.image_widget.update_image(op3d_image)

                if not renderer.is_done:
                    gui.Application.instance.post_to_main_thread(
                            renderer.window, render_image)

threading.Thread(target=_update_thread,args=(renderer,path)).start()

app.run()