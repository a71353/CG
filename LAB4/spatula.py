import math

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.spatula import BoxGeometry
from material.surface import SurfaceMaterial


class Example(Base):
    """ Render a basic scene that consists of a spinning cube """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        geometry = BoxGeometry()
        material = SurfaceMaterial(property_dict={"useVertexColors": False, "baseColor": [0.5, 0.5, 0.5]})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)


        self.additional_rotationy = 0
        self.additional_rotationx = 0
    def update(self):
        self.mesh.rotate_y(0.0 + self.additional_rotationy)
        self.mesh.rotate_x(0.0 + self.additional_rotationx)
        self.renderer.render(self.scene, self.camera)

        for keys in self.input.key_pressed_list:
            if keys == 'space':
                self.mesh.rotate_around_point([0, 0, 0], [0, 0.01, 0])
            if keys == '+':
                    self.additional_rotationy += 0.01
                    self.additional_rotationx += 0.01
            if keys == '-':
                    self.additional_rotationy -= 0.01
                    self.additional_rotationx -= 0.01
            if keys == 'up':
                    self.additional_rotationy += 0.01
            if keys == 'down':
                    self.additional_rotationy -= 0.01
            if keys == 'left':
                    self.additional_rotationx -= 0.01
            if keys == 'right':
                    self.additional_rotationx += 0.01

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
