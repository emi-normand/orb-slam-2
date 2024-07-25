import open3d as o3d
import cv2
import numpy as np
import open3d.visualization.gui as gui
import open3d.visualization.rendering as rendering
import threading
import time

# class Window:
#     def __init__(self, config):
#         self.vis = o3d.visualization.Visualizer()
#         self.vis.create_window()
#         self.image_placeholder = None
#         self.window = gui.Application.instance.create_window(
#             "Open3D - Video Example", 1000, 500)
#         self.window.set_on_layout(self._on_layout)
#         self.window.set_on_close(self._on_close)

#         self.widget3d = gui.SceneWidget()
#         self.widget3d.scene = rendering.Open3DScene(self.window.renderer)
#         self.window.add_child(self.widget3d)
    
#     def _on_layout(self, layout_context):
#         self.widget3d = gui.SceneWidget()
#         self.widget3d.scene = rendering.Open3DScene(self.window.renderer)
#         self.window.add_child(self.widget3d)
    
#     def _on_close(self):
#         self.is_done = True
#         return True  # False would cancel the close

#     def render_image(self,image):
#         # Convert the image to an Open3D image
#         o3d_image = o3d.geometry.Image(image)
#         if self.image_placeholder is None:
#             # If it's the first time, add the image to the visualizer
#             self.image_placeholder = o3d_image
#             self.vis.add_geometry(self.image_placeholder)
#         else:
#             # Update the existing image
#             self.image_placeholder = o3d_image
#             self.vis.update_geometry(self.image_placeholder)
        
#         self.vis.poll_events()
#         self.vis.update_renderer()

class VideoWindow:

    def __init__(self):
        # self.rgb_images = []
        # rgbd_data = o3d.data.SampleRedwoodRGBDImages()
        # for path in rgbd_data.color_paths:
        #     img = o3d.io.read_image(path)
        #     self.rgb_images.append(img)
        # self.depth_images = []
        # for path in rgbd_data.depth_paths:
        #     img = o3d.io.read_image(path)
        #     # The images are pretty dark, so rescale them so that it is
        #     # obvious that this is a depth image, for the sake of the example
        #     img = rescale_greyscale(img)
        #     self.depth_images.append(img)
        # assert (len(self.rgb_images) == len(self.depth_images))

        self.window = gui.Application.instance.create_window(
            "Open3D - Video Example", 1000, 500)
        self.window.set_on_layout(self._on_layout)
        self.window.set_on_close(self._on_close)

        self.image_widget = gui.ImageWidget()
        self.window.add_child(self.image_widget)

        self.is_done = False
        # threading.Thread(target=self._update_thread).start()

    def _on_layout(self, layout_context):
        contentRect = self.window.content_rect
        self.image_widget.frame = gui.Rect(contentRect.x, contentRect.y,
                                       contentRect.width,
                                       contentRect.height)

    def _on_close(self):
        self.is_done = True
        return True  # False would cancel the close
    
    



