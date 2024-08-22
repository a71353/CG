import numpy as np
import math
import pathlib
import sys

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig
from geometry.spatula import SpatulaGeometry
from geometry.fork import ForkGeometry
from geometry.frigi import FrigiGeometry
from material.surface import SurfaceMaterial
from material.texture import TextureMaterial
from core_ext.texture import Texture

class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add camera movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)

        #garfo
        fork_geometry = ForkGeometry()
        fork_material = SurfaceMaterial()
        fork_mesh = Mesh(fork_geometry, fork_material)
        fork_mesh.translate(-1.5, 0, 0)
        self.scene.add(fork_mesh)

        #espatula
        spatula_geometry = SpatulaGeometry()
        spatula_material = TextureMaterial(
            texture=Texture(file_name="images/frig.jpg"),
            property_dict={"repeatUV": [10, 10]}
        )
        spatula_mesh = Mesh(spatula_geometry, spatula_material)
        spatula_mesh.translate(1.5, 0, 0)
        self.scene.add(spatula_mesh)

        #frigideira
        frigi_geometry = FrigiGeometry()
        frigi_material = TextureMaterial(
            texture=Texture(file_name="images/st.jpg"),
            property_dict={"repeatUV": [10, 10]}
        )
        frigi_mesh = Mesh(frigi_geometry, frigi_material)
        frigi_mesh.translate(0, 0, 0)
        self.scene.add(frigi_mesh)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0.5, 1, 5])
        self.scene.add(self.rig)
        axes = AxesHelper(axis_length=2)
        self.scene.add(axes)



    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)

Example(screen_size=[800, 600]).run()
